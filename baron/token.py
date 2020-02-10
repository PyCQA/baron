from rply.token import BaseBox


class BaronToken(BaseBox):
    """
    Represents a syntactically relevant piece of text.

    :param name: A string describing the kind of text represented.
    :param value: The actual text represented.
    :param source_pos: A :class:`SourcePosition` object representing the
                       position of the first character in the source from which
                       this token was generated.
    """
    def __init__(self, name, value, hidden_tokens_before=None, hidden_tokens_after=None):
        self.name = name
        self.value = value
        self.hidden_tokens_before = list(map(self._translate_tokens_to_ast_node, hidden_tokens_before if hidden_tokens_before else []))
        self.hidden_tokens_after = list(map(self._translate_tokens_to_ast_node, hidden_tokens_after if hidden_tokens_after else []))

    def _translate_tokens_to_ast_node(self, token):
        if token[0] == "ENDL":
            return {
                "type": token[0].lower(),
                "value": token[1],
                "indent": token[3][0][1] if len(token) == 4 and token[3] else "",
                "formatting": list(map(self._translate_tokens_to_ast_node, token[2]) if len(token) >= 3 else []),
            }
        if len(token) >= 3:
            return {
                "type": token[0].lower(),
                "value": token[1],
                "formatting": list(map(self._translate_tokens_to_ast_node, token[2]) if len(token) >= 3 else []),
            }
        if token[0] == "COMMENT":
            return {
                "type": token[0].lower(),
                "value": token[1],
                "formatting": [],
            }
        return {
            "type": token[0].lower(),
            "value": token[1],
        }

    def __repr__(self):
        return "Token(%r, %r, %s, %s)" % (self.name, self.value, self.hidden_tokens_before, self.hidden_tokens_after)

    def __eq__(self, other):
        if not isinstance(other, BaronToken):
            return NotImplemented
        return self.name == other.name and self.value == other.value

    def render(self):
        before = "".join([(x["indent"] if x["type"] == "endl" else "") + x["value"] for x in self.hidden_tokens_before])
        after = "".join([(x["indent"] if x["type"] == "endl" else "") + x["value"] for x in self.hidden_tokens_after])
        # print self.hidden_tokens_before, self.value, self.hidden_tokens_after
        return before + self.value + after

    def gettokentype(self):
        """
        Returns the type or name of the token.
        """
        return self.name

    def getstr(self):
        """
        Returns the string represented by this token.
        """
        return self.value
