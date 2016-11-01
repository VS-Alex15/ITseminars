import sys

for arg in sys.argv[1:]:
    with open(arg) as f:
        print(arg,':')
        for line in f:
            print(line)
        print('\n')
