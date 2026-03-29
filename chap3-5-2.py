import click

@click.group()
def cli():
    pass

@click.group(help="Commands related to ships")
def ships():
    pass

@ships.command(help="Sail a ship")
def sail():
    ship_name = 'Your ship'
    print(f"{ship_name} is setting sail")

@ships.command(help="List all ships")
def list_ships():
    ships = ['John B', 'Yankee Clipper', 'Pequod']
    print(f"Ships: {','.join(ships)}")

cli.add_command(ships)
@cli.command(help="Talk to a sailor")

@click.option('--greeting', '-g', default='Ahoy there', help='Greeting to use')
@click.option('--name', '-n', default='Sailor', help='Name of the sailor')

def sailors(greeting, name):
    print(f"{greeting} {name}!")

if __name__ == '__main__':
    cli()

# execute in terminal with:
# python chap3-5-2.py --help
# python chap3-5-2.py ships --help
# python chap3-5-2.py ships list-ships
# python chap3-5-2.py ships sail
# python chap3-5-2.py sailors --name John --greeting "Hello, there!"