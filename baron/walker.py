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

    def before_list(self, node):
        return self.CONTINUE

    def after_list(self, node, pos):
        return self.CONTINUE

    def before_dict(self, node):
        return self.CONTINUE

    def after_dict(self, node, render_pos, render_key, key_type):
        return self.CONTINUE

    def on_constant(self, constant):
        return self.CONTINUE


def walk_on_list(worker, node):
    stop = worker.before_list(node)
    if stop:
        return stop

    pos = None
    for pos, child in enumerate(node):
        stop = walk(worker, child)
        if stop:
            break

    stop |= worker.after_list(node, pos)
    return stop


def walk_on_dict(worker, node):
    stop = worker.before_dict(node)
    if stop:
        return stop

    render_pos = None
    render_key = None
    for render_pos, render_key, key_type, child in render(node):
        stop = walk(worker, child)
        if stop:
            break

    stop |= worker.after_dict(node, render_pos, render_key, key_type)
    return stop


def walk_on_constant(worker, node):
    return worker.on_constant(node)

