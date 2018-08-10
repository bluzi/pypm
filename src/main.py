import argparse
import sys
import actions

_, action, args = sys.argv[0], sys.argv[1], sys.argv[2:]

handle = actions.get(action, args)

handle()