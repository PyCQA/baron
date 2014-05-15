from .render import render


class NodeWalker:
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

    def walk(self, node):
        if isinstance(node, list):
            return self.walk_on_list(node)
        elif isinstance(node, dict):
            return self.walk_on_dict(node)
        else:
            return self.walk_on_constant(node)

    def walk_on_list(self, node):
        stop = self.before_list(node)
        if stop:
            return stop

        pos = None
        for pos, child in enumerate(node):
            stop = self.walk(child)
            if stop:
                break

        stop |= self.after_list(node, pos)
        return stop


    def walk_on_dict(self, node):
        stop = self.before_dict(node)
        if stop:
            return stop

        render_pos = None
        render_key = None
        for render_pos, render_key, key_type, child in render(node):
            stop = self.walk(child)
            if stop:
                break

        stop |= self.after_dict(node, render_pos, render_key, key_type)
        return stop


    def walk_on_constant(self, node):
        return self.on_constant(node)

