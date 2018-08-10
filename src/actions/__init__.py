from actions import install, remove, help

def get(action, args):
    args = dict(enumerate(args))

    actions = {
        'install': lambda: install.handle(args.get(0)),
        'remove': lambda: remove.handle(args.get(0)),
        'help': lambda: help.handle(),
    }

    handle = actions.get(action, lambda: print('no such action {}'.format(action)))

    return handle