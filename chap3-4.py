import argparse

def sail():
    ship_name = 'Your ship'
    print(f"{ship_name} is setting sail")

def list_ships():
    ships = ['John B', 'Yankee Clipper', 'Pequod']
    print(f"Ships: {','.join(ships)}")

def greet(greeting, name):
    message = f'{greeting} {name}'
    print(message)
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Marintime control')
    subparsers = parser.add_subparsers(dest='func')
    ship_parser = subparsers.add_parser('ships', help='Ship related commands')
    ship_parser.add_argument('command', choices=['list', 'sail'])
    
    sailor_parser = subparsers.add_parser('sailors', help='Talk to a sailor')
    sailor_parser.add_argument('name',help='Sailors name')
    sailor_parser.add_argument('--greeting', '-g', help='Greeting', default='Ahoy there')
    
    args = parser.parse_args()
    
    if args.func == 'sailors':
        greet(args.greeting, args.name)
    elif args.command == 'list':
        list_ships()
    else:
        sail()

# execute in terminal with:
# python chap3-4.py --help
# python chap3-4.py ships --help
# python chap3-4.py ships list
# python chap3-4.py ships sail
# python chap3-4.py sailors John --greeting "Hello, there!" 

