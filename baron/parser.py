import errno
import os
import json
import stat
import tempfile
import warnings

from .token import BaronToken

from rply import ParserGenerator
from rply.parser import LRParser
from rply.parsergenerator import LRTable
from rply.errors import ParserGeneratorWarning
from rply.grammar import Grammar
from .utils import BaronError


class ParsingError(BaronError):
    pass


class BaronParserGenerator(ParserGenerator):
    def build(self):
        g = Grammar(self.tokens)

        for level, (assoc, terms) in enumerate(self.precedence, 1):
            for term in terms:
                g.set_precedence(term, assoc, level)

        for prod_name, syms, func, precedence in self.productions:
            g.add_production(prod_name, syms, func, precedence)

        g.set_start()

        for unused_term in g.unused_terminals():
            warnings.warn(
                "Token %r is unused" % unused_term,
                ParserGeneratorWarning,
                stacklevel=2
            )
        for unused_prod in g.unused_productions():
            warnings.warn(
                "Production %r is not reachable" % unused_prod,
                ParserGeneratorWarning,
                stacklevel=2
            )

        g.build_lritems()
        g.compute_first()
        g.compute_follow()

        # win32 temp directories are already per-user
        if os.name == "nt":
            cache_file = os.path.join(
                tempfile.gettempdir(),
                "rply-%s-%s-%s.json" % (self.VERSION, self.cache_id, self.compute_grammar_hash(g))
            )
        else:
            cache_file = os.path.join(
                tempfile.gettempdir(),
                "rply-%s-%s-%s-%s.json" % (self.VERSION, os.getuid(), self.cache_id, self.compute_grammar_hash(g))
            )
        table = None
        if os.path.exists(cache_file):
            with open(cache_file) as f:
                try:
                    data = json.load(f)
                except Exception:
                    os.remove(cache_file)
                    data = None

                if data is not None:
                    stat_result = os.fstat(f.fileno())
                    if (
                        os.name == "nt" or (
                            stat_result.st_uid == os.getuid()
                            and stat.S_IMODE(stat_result.st_mode) == 0o0600
                        )
                    ):
                        if self.data_is_valid(g, data):
                            table = LRTable.from_cache(g, data)

        if table is None:
            table = LRTable.from_grammar(g)
            try:
                fd = os.open(cache_file, os.O_RDWR | os.O_CREAT | os.O_EXCL, 0o0600)
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise
            else:
                with os.fdopen(fd, "w") as f:
                    json.dump(self.serialize_table(table), f)
        # meh :(
        # if table.sr_conflicts:
            # warnings.warn(
                # "%d shift/reduce conflict%s" % (len(table.sr_conflicts), "s" if len(table.sr_conflicts) > 1 else ""),
                # ParserGeneratorWarning,
                # stacklevel=2,
            # )
        # if table.rr_conflicts:
            # warnings.warn(
                # "%d reduce/reduce conflict%s" % (len(table.rr_conflicts), "s" if len(table.rr_conflicts) > 1 else ""),
                # ParserGeneratorWarning,
                # stacklevel=2,
            # )
        return BaronLRParser(table, self.error_handler)


class BaronLRParser(LRParser):
    def parse(self, tokenizer, state=None):
        lookahead = None
        lookaheadstack = []

        statestack = [0]
        symstack = [BaronToken("$end", "$end")]

        current_state = 0

        parsed_file_content = ""

        while True:
            if self.lr_table.default_reductions[current_state]:
                t = self.lr_table.default_reductions[current_state]
                current_state = self._reduce_production(t, symstack, statestack, state)
                continue

            if lookahead is None:
                if lookaheadstack:
                    lookahead = lookaheadstack.pop()
                else:
                    try:
                        lookahead = next(tokenizer)
                    except StopIteration:
                        lookahead = None

                if lookahead is None:
                    lookahead = BaronToken("$end", "$end")
                else:
                    parsed_file_content += lookahead.render()

            ltype = lookahead.gettokentype()
            if ltype in self.lr_table.lr_action[current_state]:
                t = self.lr_table.lr_action[current_state][ltype]
                if t > 0:
                    statestack.append(t)
                    current_state = t
                    symstack.append(lookahead)
                    lookahead = None
                    continue
                elif t < 0:
                    current_state = self._reduce_production(t, symstack, statestack, state)
                    continue
                else:
                    n = symstack[-1]
                    return n
            else:
                debug_output = parsed_file_content.split("\n")
                debug_output = list(zip(range(1, len(debug_output) + 1), debug_output))
                debug_output = debug_output[-8:]
                debug_output = "\n".join(["%4s %s" % (x[0], x[1]) for x in debug_output])
                debug_output += "<---- here"
                debug_output = "Error, got an unexpected token %s here:\n\n" % ltype + debug_output
                debug_output += "\n\nThe token %s should be one of those: %s" % (ltype, ", ".join(sorted(self.lr_table.lr_action[current_state].keys())))
                debug_output += "\n\nBaron has failed to parse this input. If this is valid python code (and by that I mean that the python binary successfully parse this code without any syntax error) (also consider that baron does not yet parse python 3 code integrally) it would be kind if you can extract a snippet of your code that make Baron fails and open a bug here: https://github.com/PyCQA/baron/issues\n\nSorry for the inconvenience."
                raise ParsingError(debug_output)
