"""	Дан список из строк. Создайте однострочное решение (при помощи list comprehension),
 которое приведёт к верхнему регистру все строки, содержащие слово 'price')"""


def price_upper_case(strings):
    return [element.upper() if 'price' in element else element for element in strings]


my_list = ['price', 'lsfjprice', '1414price', 'fds', 'ddd', 'lower price']
print(price_upper_case(my_list))
