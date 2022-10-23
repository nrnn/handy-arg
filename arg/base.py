class Value:
    def __init__(self, name, default=None, required=False, description=None):
        self.name = name
        self.default = default
        self.required = required
        self.description = description

        self.cur_value = default

    def __call__(self):
        return self.cur_value


class Args:
    def __init__(self):
        pass


ARG = Args()


def init():
    # 1. Load config
    # 2. If "--help" occurs in sys.argv, convert to argparse help format and exit
    pass


def save():
    # Convert all the args into a specific file format (yaml? to be decided.)
    pass


def value(*, name, default=None, required=False, description=None):
    # Main entrance to set arg value.
    pass
