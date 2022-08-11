"""
Есть список из случайных чисел и строк. Создайте цикл, итерирующийся до тех пор, пока не встретится число "777".
Если в течении 100 попыток число не будет найдено — остановить цикл и вызвать ошибку с соответсвующим сообщением.
"""


lst = [x for x in range(1000)]
i = 0
for x in lst:
    if x != 777:
        i += 1
    else:
        print('Число віднайдено!')
    if i > 100:
        raise Exception('Число не знайдено')