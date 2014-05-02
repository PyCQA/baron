from .render import render


class NodeWalkerWorker:
    '''Inherit me and overload the methods you want'''
    CONTINUE = False
    STOP = True

    def on_list(self, node, pos):
        return self.CONTINUE

    def on_dict(self, node, render_pos, render_key):
        return self.CONTINUE

    def on_constant(self, constant):
        return self.CONTINUE


class NodeWalker:
    def __init__(self, worker):
        self.worker = worker

    def walk_on_list(self, node):
        stop = False

        pos = None
        for pos, child in enumerate(node):
            stop = self.walk(child)
            if stop:
                break

        stop |= self.worker.on_list(node, pos)
        return stop

    def walk_on_dict(self, node):
        stop = False

        render_pos = None
        render_key = None
        for render_pos, render_key, item in render(node):
            stop = self.walk(item)
            if stop:
                break

        stop |= self.worker.on_dict(node, render_pos, render_key)
        return stop

    def walk_on_constant(self, node):
        return self.worker.on_constant(node)

    def walk(self, node):
        if isinstance(node, list):
            return self.walk_on_list(node)
        elif isinstance(node, dict):
            return self.walk_on_dict(node)
        else:
            return self.walk_on_constant(node)

