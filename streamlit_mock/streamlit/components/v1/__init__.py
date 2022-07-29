import json


def _render_component(*args, **kwargs):
    print(args)
    print("_render_component: ", kwargs)
    pass


def declare_component(*args, **kwargs):
    return _render_component


class components:
    def register_widget(*args, **kwargs):
        pass
