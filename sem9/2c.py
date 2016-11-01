import argparse
import sys

parser = argparse.ArgumentParser(
    description='Калькулятор'
)

parser .add_argument(
    '-a',
    '--action',
    metavar='VALUE',
    type=str,
    action='store'
)

parser.add_argument(
    # короткое название опции
    '-v',
    # длинное название опции
    '--verbose',
    # парсер сохранит значение True, если встретит эту опцию
    action='store_true',
    # краткое описание опции
)

parser.add_argument(
    # название поля в объекте, где будут сохранены параметры
    'values',
    # название параметров, которое будет отображено в справке
    metavar='VALUES',
    # сообщаем что ожидаются числа с плавающей запятой
    type=float,
    # параметров будет не меньше одного
    nargs='+',
)

args = parser.parse_args()

if not args.action :
    # выводим сообщение об ошибке в стандартный поток вывода ошибок (stderr)
    print(
        'Необходимо указать параметр --mean или --stdev или же оба',
        file=sys.stderr
    )
    # завершаем программу
    sys.exit(-1)

values = [x for x in args.values]

x = 0

if args.action=='+':
    x = values[0]+values[1]
elif args.action=='-':
    x = values[0] - values[1]
elif args.action=='*':
    x = values[0] * values[1]
elif args.action == '/':
    x = values[0] / values[1]

if args.verbose:
    print(values[0],args.action,values[1],'=',x)
else:
    print(x)
