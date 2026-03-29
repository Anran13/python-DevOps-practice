import click

@click.command()
@click.option('--greeting', default='Hiya', help='Greeting to use')
@click.option('--name', default='Tammy', help='Name of the person to greet')

def greet(greeting, name):
    print(f"{greeting} {name}")

if __name__ == '__main__':
    greet()

# execute in terminal with:
# python chap3-5-1.py --greeting "Hello there" --name "Andy"
# python chap3-5-1.py --help