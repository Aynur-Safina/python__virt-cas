
import random


# Список вариантов в категории 1 (Красное/черное)
list_1 = ['красное', 'черное']
print('Добро пожаловать в виртуальное казино!')
print('Вы можете сделать ставку на 1 из 2 категорию:')
print('1. красное-черное')
print('2. прямая ставка (число от 0 до 36)')

bet = int(input('Ваша ставка (введите число): '))   # Ставка пользователя
type = type(bet)  # Проверка ставки на тип данных


# в условии проверяем тип данных (если пользователь ошибочно ввел НЕ число) + если ставка <=0, то игра завершена
if type == int and bet <= 0:
    print('Ваша ставка не может быть принята. Пожалуйста, будьте внимательны при вводе числа (допускается только число, большее чем 0)!')

elif type == int and bet > 0:
    # дальше проверяем ставку:если ставка >0, то пользователь выбирает номер категории           #
    num_cat = int(input('Введите номер категории: '))
    type_cat = type(num_cat)  # Проверка типа данных номера категории

    if type_cat != int:  # отсекаем случаи, если пользователь ввел НЕ число
        print('Ваша ставка не может быть принята. Пожалуйста, будьте внимательны при вводе числа (допускается только число 1 или 2)!')

    else:
        if num_cat == 1:  # категория 1 - ставка на карсное/черное
            choiсe_origin = input(
                'Введите название цвета в формате: "красное" / "черное": ')

            # если пользователь случаной ввел пробел, программа удаляет их
            choiсe_remove = choiсe_origin.replace(' ', '')

            # если пользователь случаной ввел заглавные буквы, программа меняет их на строчные
            choiсe_lower = choiсe_remove.lower()

            # рандомный выбор одного из двух значений из списка list_1 (красное/черное), это будем считать выигрышным вариантом
            rand_list_1 = random.choice(list_1)

            # удаляем из list_1 выигрышный вариант --> оставшийся вариант считаем проигрышным. Нельзя присваивать его новой переменной (выдаст ошибку)
            list_1.remove(rand_list_1)

            # Т.к. проигрышный вариант представлен в виде списка, а не строки, его нужно преобразовать в строку
            losing = ' '.join(list_1)

            if choiсe_lower == rand_list_1:  # Рассматриваем вариант выигрыша
                print(
                    f'Поздравляем!Сыграло {rand_list_1} поле. Ваш выигрыш {bet*2} фантиков')

            elif choiсe_lower == losing:  # Рассматриваем вариант проигрыша
                print(
                    f'Увы, сыграло {rand_list_1} поле. Попробуйте еще раз, удача обязательно улыбнется Вам!')
                # Проверка "на дурака": Рассматриваем вариант, когда пользователь ввел нерелевантное значение (не из list_1)
            else:
                print(
                    'Ваша ставка не может быть принята. Пожалуйста, будьте внимательны при вводе названия цвета.')

        # Если пользователь выбирает Прямые ставки (на конкретное число)
        elif num_cat == 2:

            # Число, на которое ставит пользователь
            digit_us = int(input('Введите число от 0 до 36: '))

            # Рандомное число, которое выдает казино (выигрышное число)
            digit_cas = random.randint(0, 36)

            if digit_us < 0 or digit_us > 36:   # проверка на дурака: если пользователь ввел отрицательное число, или число больше 36
                print(
                    'Ваша ставка не может быть принята. Пожалуйста, будьте внимательны при вводе  числа.')

            elif digit_us == digit_cas:  # Если пользователь выиграл
                print(
                    f'Сыграло число {digit_cas}. Поздравляем! Ваш выигрыш составил {bet*35}')

            else:       # Если пользователь проиграл
                print(
                    f'Увы, сыграло число {digit_cas}. Попробуйте еще раз, удача обязательно улыбнется Вам!')
else:  # отсекаем случаи, если пользователь ошибочно ввел НЕ число
    print('Ваша ставка не может быть принята. Пожалуйста, будьте внимательны при вводе числа (допускается только число)!')
    '''
       можно было еще проверить на тип данных остальные параметры, но не уже терпения не хватило. Это ведь еще и проверять предстоит )))
'''
