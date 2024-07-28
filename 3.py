# Программа загадывает число от 0 до 1000. Необходимо угадать число
# за 10 попыток. Программа должна подсказывать “больше” или “меньше”
# после каждой попытки. Для генерации случайного числа используйте код:
# from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)

import random


LOWER_LIMIT = 0
UPPER_LIMIT = 1000
COUNT = 10
TRY = 0
num = random.randint(LOWER_LIMIT, UPPER_LIMIT)


# for i in range(1, COUNT + 1):
#     if num == guess:
#         print(f'бинго! вы угадали с {i} попытки')
#         break
#     elif guess > num:
#         print('меньше')
#     elif guess < num:
#         print('больше')
#
# if num != guess:
#     print('все попытки истрачены. сожалею')


while COUNT > 0:
    guess = int(input('угадайте число: '))
    TRY += 1
    COUNT -= 1
    if num == guess:
        print(f'бинго! вы угадали с {TRY} попытки')
        break
    elif guess > num:
        print('меньше')
    elif guess < num:
        print('больше')


if COUNT == 0 and num != guess:
    print(f'все попытки истрачены. сожалею. было загадано число {num}')
