import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Echo your input')
    parser.add_argument('message', help='Message to echo')
    parser.add_argument('--twice', '-t', help='Do it twice', action='store_true')
    args = parser.parse_args()
    print(args.message)
    if args.twice:
        print(args.message)

# execute in terminal with:
# python chap3-3.py "Hello, World!" --twice
# python chap3-3.py hello --twice
# python chap3-3.py --help