# Реализуйте следующую функцию:
#     add_everything_up, будет складывать числа(int, float) и строки(str)
# Описание функции:
# add_everything_up(a, b) принимает a и b, которые могут быть как числами(int, float), так и строками(str).
# TypeError - когда a и b окажутся разными типами (числом и строкой),
# то возвращать строковое представление этих двух данных вместе (в том же порядке).
# Во всех остальных случаях выполнять стандартные действия.

def add_everything_up(a, b):
    try:
        print(a+b)
    except TypeError as exc:
        print(f'{a}{b}')


add_everything_up(6, 'djk')
add_everything_up('при', 'вет')
add_everything_up(1, 7)
