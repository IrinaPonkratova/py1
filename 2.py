# Напишите код, который запрашивает число и сообщает является
# ли оно простым или составным. Используйте правило для проверки:
# “Число является простым, если делится нацело только на единицу
# и на себя”. Сделайте ограничение на ввод отрицательных чисел и
# чисел больше 100 тысяч.

MIN_LIM = 2
MAX_LIM = 100_000

number = int(input(f'введите число от {MIN_LIM} до {MAX_LIM}: '))
medium = number // 2 + 1
for i in range(2, medium):
    if number % i == 0:
        result = 'число составное'
    else:
        result = 'число простое'

print(result)
