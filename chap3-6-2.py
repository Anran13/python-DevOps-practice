import fire 

class ships():
    def sail(self):
        ship_name = 'Your ship'
        print(f"{ship_name} is setting sail")

    def list(self):
        ships = ['John B', 'Yankee Clipper', 'Pequod']
        print(f"Ships: {','.join(ships)}") 

def sailors(greeting='Ahoy there', name='Sailor'):
    print(f"{greeting} {name}!")

class cli():
    def __init__(self):
        self.ships = ships()
        self.sailors = sailors

if __name__ == '__main__':
    fire.Fire(cli)

# execute in terminal with:
# python chap3-6-2.py sailors --help
# python chap3-6-2.py ships sail
# python chap3-6-2.py ships list
# python chap3-6-2.py sailors --name John --greeting "Hello, there!"
# python chap3-6-2.py sailors Hiya John -- --interactive