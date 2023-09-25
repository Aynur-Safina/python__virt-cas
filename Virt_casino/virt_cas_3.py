
import random

# Список вариантов в категории 1 (Красное/черное)
list_1 = ['красное', 'черное']
print('Добро пожаловать в виртуальное казино!')
print('Вы можете сделать ставку на 1 из 2 категорий:')
print('1. красное-черное')
print('2. прямая ставка (число от 0 до 36)')

bet = int(input('Ваша ставка (введите число): '))   # Ставка пользователя

while True:
    if bet <= 0:  # в условии проверяем ставку:если ставка <=0, то игра завершена
        print('Ваша ставка не может быть принята. Пожалуйста, будьте внимательны при вводе числа (допускается только число, большее чем 0)!')
        bet = int(input('Ваша ставка (введите число): '))

    else:
        # дальше проверяем ставку:если ставка >0, то пользователь выбирает номер категории

        num_cat = int(input('Введите номер категории: '))

        if num_cat == 1:  # категория 1 - ставка на карсное/черное
            choiсe_origin = input(
                'Введите название цвета в формате: "красное" / "черное": ')  # выбор игрока
            # если пользователь ввел пробел, удаляем его
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
                bet = int(
                    input('Сыграем еще раз? Ваша ставка (введите число): '))
            elif choiсe_lower == losing:  # Рассматриваем вариант проигрыша
                print(
                    f'Увы, сыграло {rand_list_1} поле. Попробуйте еще раз, удача обязательно улыбнется Вам!')
                bet = int(
                    input('Сыграем еще раз? Ваша ставка (введите число): '))

            # Проверка "на дурака": Рассматриваем вариант, когда пользователь ввел нерелевантное значение (не из list_1
            else:
                print(
                    'Ваша ставка не может быть принята. Пожалуйста, будьте внимательны при вводе названия цвета.')

        # Если пользователь выбирает Прямые ставки (на конкретное число)
        elif num_cat == 2:
            # Число, на которое ставит пользователь
            # Рандомное число, которое выдает казино (выигрышное число)
            digit_us = int(input('Введите число от 0 до 36: '))
            digit_cas = random.randint(0, 36)

            if digit_us < 0 or digit_us > 36:   # проверка на дурака: если пользователь ввел отрицательное число, или число больше 36
                print(
                    'Ваша ставка не может быть принята. Допускаеются только ввод числа от 0 до 36.')

            elif digit_us == digit_cas:  # Если пользователь выиграл
                print(
                    f'Сыграло число {digit_cas}. Поздравляем! Ваш выигрыш составил {bet*35}')
                bet = int(
                    input('Сыграем еще раз? Ваша ставка (введите число): '))

            else:       # Если пользователь проиграл
                print(
                    f'Увы, сыграло число {digit_cas}. Попробуйте еще раз, удача обязательно улыбнется Вам!')
                bet = int(
                    input('Сыграем еще раз? Ваша ставка (введите число): '))
        else:  # отсекаем случаи, если пользователь ввел не 1, и не 2
            print('Ваша ставка не может быть принята. Пожалуйста, будьте внимательны при вводе числа (допускается только число 1 или 2)!')
            bet = int(input('Ваша ставка (введите число): '))