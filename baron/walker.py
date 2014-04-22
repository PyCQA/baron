from .render import render


class StopState:
    def __init__(self):
        self.stop = False

    def setStop(self, stop):
        if not self.stop and stop:
            self.stop = True


class NodeWalker:

    def walk_on_list(self, node):
        stop = StopState()
        pos = None
        for pos, child in enumerate(node):
            stop.setStop(self.walk(child))
            if stop.stop:
                break

        stop.setStop(self.on_list(node, pos))
        return stop.stop

    def walk_on_dict(self, node):
        stop = StopState()
        render_pos = None
        render_key = None
        for render_pos, render_key, item in render(node):
            stop.setStop(self.walk(item))
            if stop.stop:
                break

        stop.setStop(self.on_dict(node, render_pos, render_key))
        return stop.stop

    def walk_on_constant(self, node):
        stop = self.on_constant(node)
        return stop

    def __init__(self):
        self.walk_function_based_on_instance = {
                "list": self.walk_on_list,
                "dict": self.walk_on_dict,
                "str": self.walk_on_constant,
            }

    def walk(self, node):
        instance_name = type(node).__name__
        stop = self.walk_function_based_on_instance[instance_name](node)
        return stop


    def on_list(self, node, pos):
        pass

    def on_dict(self, node, current, target):
        pass

    def on_constant(self, constant):
        pass
