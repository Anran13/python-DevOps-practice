import sys

def say_it(greeting, name):
    message = f'{greeting} {name}'
    print(message)


if __name__ == '__main__':

    
    greeting = 'Hello'
    name = 'Joe'

    if '--help' in sys.argv:
        help_message = f"Usage: {sys.argv[0]} --name <NAME> --greeting <GREETING>"
        print(help_message)
        sys.exit()

    if '--name' in sys.argv:
        # Get position after name flag
        name_index = sys.argv.index('--name') + 1
        if name_index < len(sys.argv):
            name = sys.argv[name_index]

    if '--greeting' in sys.argv:
        # Get position after greeting flag
        greeting_index = sys.argv.index('--greeting') + 1
        if greeting_index < len(sys.argv):
            greeting = sys.argv[greeting_index]
    
    say_it(greeting, name)

# execute in terminal with:
# python chap3-2.py --name Andy