from .render import RenderWalker


def dumps(tree, strict=False):
    return Dumper(strict=strict).dump(tree)


class Dumper(RenderWalker):
    def before_leaf(self, constant, key):
        self.dump += constant

    def dump(self, tree):
        self.dump = ''
        self.walk(tree)
        return self.dump
