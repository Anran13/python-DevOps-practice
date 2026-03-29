import fire  

def greet(greeting='Hello', name='Tammy'):
    print(f'{greeting} {name}')

def goodbye(goodbye='Bye', name='Tammy'):
    print(f'{goodbye} {name}')

if __name__ == '__main__':
    fire.Fire()

# execute in terminal with:
# python chap3-6-1.py --help