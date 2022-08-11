"""
Напишите template строки,который можно будет многократно переиспользовать,
вставляя в него имя и фамилию человека. Используйте метод строки "format".
"""

first_name, second_name = 'Тарас', 'Шевченко'

str1 = f"{first_name} {second_name}"

str2 = "{} {}"
formatted_str2 = str2.format(first_name, second_name)
