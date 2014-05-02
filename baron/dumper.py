from .walker import walk, NodeWalkerWorker


def dumps(tree):
    worker = Dumper()
    walk(worker, tree)
    return worker.dump


class Dumper(NodeWalkerWorker):
    def __init__(self):
        self.dump = ''

    def on_constant(self, constant):
        self.dump += constant
        return self.CONTINUE

