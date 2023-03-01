import argparse

parser = argparse.ArgumentParser()
parser.add_argument("name", help="name of user")
parser.add_argument('-g','--greeting',default='hello',help='optional alternate argument')
args = parser.parse_args()
print('{greeting}', '{name}!'.format(greeting = args.greeting,name = args.name))