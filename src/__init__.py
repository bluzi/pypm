import sys
from actions import install, remove, help


def get_action(action, args):
    args = dict(enumerate(args))

    actions = {
        'install': lambda: install.handle(args.get(0)),
        'remove': lambda: remove.handle(args.get(0)),
        'help': lambda: help.handle(),
    }

    action_handler = actions.get(action, lambda: print('no such action {}'.format(action)))

    return action_handler


if len(sys.argv) < 2:
    action = 'help'
    args = []
else:
    _, action, args = sys.argv[0], sys.argv[1], sys.argv[2:]

handle = get_action(action, args)

try:
    handle()
except Exception as e:
    print('Error: {}'.format(str(e)))