import sys
import argparse
import os

parser = argparse.ArgumentParser(
    description='Дерево файловой системы'
)

parser.add_argument(
    '--folders_only',
    action='store_true'
)

parser.add_argument(
    '-i',
    '--include',
    metavar='VALUE',
    type=str,
    action='store'
)

parser.add_argument(
    '-e',
    '--exclude',
    metavar='VALUE',
    type=str,
    action='store'
)

parser.add_argument(
    '-a',
    '--all',
    action='store_true'
)

parser.add_argument(
    '--full_name',
    action='store_true'
)

parser.add_argument(
    'values',
    metavar='VALUES',
    nargs="+"
)

args = parser.parse_args()

need_dir = args.values[0]

def print_directory(cwd,k):
    os.chdir(cwd)
    for i in range(k):
        print(' ',end='')
    print(cwd[cwd.rfind('/')+1:])
    ways = os.listdir(cwd)
    if (args.folders_only==False):
        for elem in ways:
            if os.path.isfile(cwd+'/'+elem):
                if args.include==None and args.exclude==None:
                    for i in range(k+3):
                        print(' ',end='')
                    print(elem)
                else:
                     if args.exclude==None and args.include!=None:
                         if elem.find(args.include)!=-1:
                             for i in range(k+3):
                                 print(' ',end='')
                             print(elem)
                     if args.exclude!=None and args.include==None:
                         if elem.find(args.exclude)==-1:
                             for i in range(k+3):
                                 print(' ',end='')
                             print(elem)
    for elem in ways:
        if os.path.isdir(cwd+'/'+elem):
            print_directory(cwd+'/'+elem,k+3)
        os.chdir(cwd)
print(need_dir)
print_directory(need_dir,2)