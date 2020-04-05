import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Show the contentsof a text file.')
    parser.add_argument('-v','--verbose',action='store_true',
                        help='increase output verbosity')
    parser.add_argument('filename',help='the name of the file to read')
    parser.add_argument('-l','--lines',type=int, help='the number of lines to read')
    args = parser.parse_args()
    if args.verbose:
        print("Verbosity turned on")
        print("Opening file")
    with open(args.filename) as file:
        if args.verbose:
            print("File successfully opened!")
        if hasattr(args, 'lines'):
            content = file.readlines()[:args.lines]
        else:
            content = file.readlines()
        for line in content:
            print(line)
