from .render import render




class NodeWalker:

    def walk_on_list(self, node):
        stop = False

        pos = None
        for pos, child in enumerate(node):
            stop = self.walk(child)
            if stop:
                break

        stop |= self.on_list(node, pos)
        return stop

    def walk_on_dict(self, node):
        stop = False

        render_pos = None
        render_key = None
        for render_pos, render_key, item in render(node):
            stop = self.walk(item)
            if stop:
                break

        stop |= self.on_dict(node, render_pos, render_key)
        return stop

    def walk_on_constant(self, node):
        return self.on_constant(node)

    def walk(self, node):
        if isinstance(node, list):
            return self.walk_on_list(node)
        elif isinstance(node, dict):
            return self.walk_on_dict(node)
        else:
            return self.walk_on_constant(node)


    def on_list(self, node, pos):
        pass

    def on_dict(self, node, current, target):
        pass

    def on_constant(self, constant):
        pass
