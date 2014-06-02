from .render import RenderWalker


def dumps(tree):
    return Dumper().dump(tree)


class Dumper(RenderWalker):
    def on_leaf(self, constant, pos, key):
        self.dump += constant

    def dump(self, tree):
        self.dump = ''
        self.walk(tree)
        return self.dump
