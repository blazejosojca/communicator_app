import argparse

parser = argparse.ArgumentParser(description="Authentication module",add_help=True)

group = parser.add_argument_group('authentication')

group.add_argument('-u', '--user', dest="username", action="store", help="User name")
group.add_argument('-p', '--password', dest="password", action="store", help="User password")