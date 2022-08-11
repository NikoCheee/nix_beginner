"""
Дан список из строк. Используя join,
соедините строки так, чтобы они были разделены через запятую.
На выходе должна получиться строка в виде
"my_string1,my_string2,my_string3"
"""

new_list = ['my_string1', 'my_string2', 'my_string3']
a = ','.join(string for string in new_list)
print(a)