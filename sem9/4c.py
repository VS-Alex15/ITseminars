import sys
import argparse
import os

parser = argparse.ArgumentParser(
    description='Дерево файловой системы'
)

parser .add_argument(
    '--folders-only',
    action='store_true'
)

parser .add_argument(
    '-i',
    '--include',
    metavar='VALUE',
    type=str,
    action='store'
)

parser .add_argument(
    '-e',
    '--exclude',
    metavar='VALUE',
    type=str,
    action='store'
)

parser .add_argument(
    '-a',
    '--all',
    action='store_true'
)

parser .add_argument(
    '--full-name',
    action='store_true'
)

