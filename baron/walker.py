from .render import render


def walk(worker, node):
    if isinstance(node, list):
        return walk_on_list(worker, node)
    elif isinstance(node, dict):
        return walk_on_dict(worker, node)
    else:
        return walk_on_constant(worker, node)


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


def walk_on_list(worker, node):
    stop = False

    pos = None
    for pos, child in enumerate(node):
        stop = walk(worker, child)
        if stop:
            break

    stop |= worker.on_list(node, pos)
    return stop


def walk_on_dict(worker, node):
    stop = False

    render_pos = None
    render_key = None
    for render_pos, render_key, child in render(node):
        stop = walk(worker, child)
        if stop:
            break

    stop |= worker.on_dict(node, render_pos, render_key)
    return stop


def walk_on_constant(worker, node):
    return worker.on_constant(node)

