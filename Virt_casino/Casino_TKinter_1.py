import tkinter
from tkinter import *
from tkinter import messagebox
import random

# window settings
root = Tk()
root.resizable(width=False, height=False)
root.attributes('-alpha', 0.9) # прозрачность окна

root.geometry('500x500+400+100')
root.title('" PONAROSHKU-Казино"')
root['bg'] = '#bf0606'
root.iconbitmap('icn_r.ico')

lbl_welcome = Label (text = 'Добро пожаловать в виртуальное казино!',
                            width= 490,
                            font = 'Consolas 16', # Если в названии шрифта несколько слов
                            # (например, Times New Roman), то слова в названии
                            # писать через нижнее подчеркивание
                            fg = 'black',
                            bg = '#bf0606',
                            justify='center',
                            pady=5)
lbl_welcome.pack()

lbl_choice = Label (text = 'Выберите категорию игры',
                            width= 490,
                            font = 'Consolas 14', # Если в названии шрифта несколько слов
                            # (например, Times New Roman), то слова в названии
                            # писать через нижнее подчеркивание
                            fg = 'black',
                            bg = '#bf0606',
                            justify='center',
                            pady=2)
lbl_choice.pack()

def r_b():
    lbl_instruction['text']='Введите название цвета в формате:\n "красное" / "черное" '
    us_entry.pack()
    play_button.pack(pady=10)
    play_button.bind('<Button-1>', play_rb)


def play_rb(event):

    global us_rb_origin, us_rb_remove, us_rb_lower, bet, bet_entry, us_entry, lbl_instruction,lbl_win
    lbl_win.pack()
    try:
        bet = int(bet_entry.get())
    except ValueError:
        messagebox.showerror('int_error-1', 'Ваша ставка не может быть принята.\n'
                                           'Допускается только число больше 0!')
    us_rb_origin=us_entry.get()
   # print(us_rb_origin)
    us_rb_remove =us_rb_origin.replace(' ', '')
    # получаем текст из Ентри , и, если пользователь случаной ввел заглавные буквы, программа меняет их на строчные
    us_rb_lower = us_rb_remove.lower()
    # рандомный выбор одного из двух значений из списка list_1 (красное/черное), это будем считать выигрышным вариантом
    bet = int(bet_entry.get())
    list_rb = ['красное', 'черное']
    rand_list_rb = random.choice(list_rb)
    print("rand_list_rb: ", rand_list_rb)
    # удаляем из list_1 выигрышный вариант --> оставшийся вариант считаем проигрышным. Нельзя присваивать его новой переменной (выдаст ошибку)
    list_rb.remove(rand_list_rb)
    # Т.к. проигрышный вариант представлен в виде списка, а не строки, его нужно преобразовать в строку
    losing = ' '.join(list_rb)
    print('losing', losing)

    if us_rb_lower == rand_list_rb:  # Рассматриваем вариант выигрыша

        lbl_win.config(text = f'Поздравляем!Сыграло {us_rb_lower} поле.\n'
                              f'Ваш выигрыш {str(bet * 2)} фантиков\n')

    elif us_rb_lower == losing:  # Рассматриваем вариант проигрыша

        lbl_win.config(text= f'Увы, сыграло {rand_list_rb} поле.\n Попробуйте еще раз, \n'
                             f'удача обязательно улыбнется Вам!\n')
    else:
         messagebox.showerror('str_error-1', 'Ваша ставка не может быть принята.\n'
'Допускается только значение "красное" или "черное"!')


#После игры очищаем все пол ввода

    #bet_entry.delete(0,END)
    #lbl_instruction['text']=''
    #us_text_entry.destroy()
    #lbl_win['text']=''
    #play_button_rb.destroy()
### Почему не работает messagebox.destroy() ????
def h_l():
    print('2')
    lbl_instruction.config(text=f'Введите число от 0 до 36: ')
    us_entry.pack()
    play_button.pack(pady=10)
    play_button.bind('<Button-1>', play_hl)

def play_hl(event):
    global us_num, digit_cas, bet, bet_entry, us_entry, lbl_instruction, lbl_win, play_button, num_hl
    lbl_win.pack()
    try:
        bet = int(bet_entry.get())
        us_num = int(us_entry.get())
    except ValueError:
        messagebox.showerror('int_error-1', 'Ваша ставка не может быть принята.\n'
                                            'Допускается только число больше 0!')
    us_num = int(us_entry.get())
    digit_cas = random.randint(0, 36)
    if 0<=digit_cas<=18:
        if 0<=us_num<=18:
            lbl_win.config(text=f'Сыграло число {digit_cas} - малое число. \n'
                                f'Поздравляем! Ваш выигрыш составил {bet * 2}')
        elif 19<=us_num<=36:
            lbl_win.config(text=f'Увы!Сыграло число {digit_cas} - малое число. \n')
        else:
            messagebox.showerror('TypeError', 'Ваша ставка не может быть принята.\n '
                                              'Допускается только число от 0 до 36!')
    else:
        if 0<=us_num<=18:
            lbl_win.config(text=f'Увы!Сыграло число {digit_cas} - большое число. \n')
        elif 19<=us_num<=36:
            lbl_win.config(text=f'Сыграло число {digit_cas} - большое число. \n Поздравляем! Ваш выигрыш составил {bet * 2}')
        else:
            messagebox.showerror('TypeError', 'Ваша ставка не может быть принята.\n '
                                              'Допускается только число от 0 до 36!')

def num():

    lbl_instruction.config(text=f'Введите число от 0 до 36: ')
    us_entry.pack()
    play_button.pack(pady=10)
    play_button.bind('<Button-1>', play_num)


def play_num(event):
    global us_num, digit_cas, bet, bet_entry, us_entry, lbl_instruction, lbl_win, play_button
    lbl_win.pack()
    try:
        bet = int(bet_entry.get())
        us_num = int(us_entry.get())
    except ValueError:
        messagebox.showerror('int_error-1', 'Ваша ставка не может быть принята.\n'
                                            'Допускается только число больше 0!')
    us_num = int(us_entry.get())
    digit_cas = random.randint(0, 36)

    if us_num==digit_cas:  # Если пользователь выиграл
        lbl_win.config(text= f'Сыграло число {digit_cas}. \n'
                             f'Поздравляем! Ваш выигрыш составил {bet * 35}')

    elif us_num < 0:
        messagebox.showerror('TypeError', 'Ваша ставка не может быть принята.\n '
                                          'Допускается только число от 0 до 36!')
    elif us_num > 36:
        messagebox.showerror('TypeError', 'Ваша ставка не может быть принята.\n '
                                          'Допускается только число от 0 до 36!')
    else:
        lbl_win.config(text=f'Увы, сыграло число {digit_cas}.\n Попробуйте еще раз,\n удача обязательно улыбнется Вам!')



var = IntVar()
var.set(0)
red_black = Radiobutton (text = 'Красное или Черное',
                         variable= var,
                         value = 0,
                         bg='#bf0606',
                         font='Consolas 12',
                         justify='left',
                         command=r_b
                         )
hight_low = Radiobutton (text = 'Большое или Малое',
                         variable= var,
                         value = 1,
                         bg='#bf0606',
                         font='Consolas 12',
                        justify='left',
                         command=h_l
                         )
number = Radiobutton (text = 'Прямая ставка',
                         variable= var,
                         value = 2,
                        bg='#bf0606',
                        font='Consolas 12',
                        justify='left',
                        command=num
                      )

red_black.pack()
hight_low.pack()
number.pack()


text_bet = Label(text='Ваша ставка (введите число): ',
                            width=50,
                            font='Consolas 14',
                            fg = 'black',
                            bg = '#bf0606',
                            justify='center'
                                         )
text_bet.pack()

bet_entry = Entry(root,
            font = "Comforta 14",
            fg ='black',
            bg ='white',
            justify='center',
            relief='solid',
            width=5)
bet_entry.pack()

# дополнительное поле ввода после выбора категории игры (сначала оно невидимое, т.к. пустое)
lbl_instruction = Label(text = '',
                            width= 490,
                            font = 'Consolas 14', # Если в названии шрифта несколько слов
                            # (например, Times New Roman), то слова в названии
                            # писать через нижнее подчеркивание
                            fg = 'black',
                            bg = '#bf0606',
                            justify='center')
lbl_instruction.pack()

us_entry = Entry(root,
            font = "Comforta 14",
            fg ='black',
            bg ='white',
            justify='center',
            relief='solid',
            width=20)

play_button = Button(root, text='Играть',
                         font='Consolas 16',
                         fg='black',
                         bg='green',
                         justify='center')



lbl_win = Label(text='',
                        width=490,
                        font='Consolas 14',  # Если в названии шрифта несколько слов
                        # (например, Times New Roman), то слова в названии
                        # писать через нижнее подчеркивание
                        fg='black',
                        bg='#bf0606',
                        justify='center')
#lbl_win.pack()
root.mainloop()

'''
#play_button_num = Button(root, text='Играть',
                         font='Consolas 16',
                         fg='black',
                         bg='green',
                         justify='center')

red_black.grid(row=1, column=1)
hight_low.grid(row=2, column=1)
number.grid(row=3, column=1)
def casino (event):

    digit_cas = random.randint(0, 36)
    try:
        bet_1 = bet_entry.get()
        bet = int(bet_1)
        digit_user = digit_entry.get()
        digit = int(digit_user)
    except ValueError:
        messagebox.showerror('Error-1','Можно вводить только число!')
    if bet == 0:
        messagebox.showinfo('Info',' Допускается только число больше 0')

    else:
        if digit < 0 or digit > 36:
            messagebox.showinfo('Допускается только число от 0 до 36.')

        elif digit == digit_cas:
            messagebox.showinfo(f'Сыграло число {digit_cas}.\n'
                            f'Поздравляем! \n'
                            f'Ваш выигрыш составил {bet * 35} фантиков')
        else:
            messagebox.showinfo(f'Увы, сыграло число {digit_cas}.\n'
                            f' Попробуйте еще раз, \n'
                            f'удача обязательно улыбнется Вам!')
            fiasko_button = Button(text = 'Fiasko',font='Consolas 20',
                     fg='black',
                     bg='green',
                     justify='center',
                     pady= 20   )
            fiasko_button.pack()
#Event
#щздаем переменную для вывода текста
text_instruction = Message (text = 'Добро пожаловать в виртуальное казино!\n'
                                   'Вы можете сделать ставку на число от 0 до 36\n',

                            width= 490,
                            font = 'Consolas 14', # Если в названии шрифта несколько слов
                            # (например, Times New Roman), то слова в названии
                            # писать через нижнее подчеркивание
                            fg = 'black',
                            bg = '#bf0606',
                            justify='left')
# Если потом нужно поменять текст, то нужно просто ввести новое значение
# text_instruction['text'] = 'Новый текст'
text_instruction.pack()


text_bet = Label(root, text='Ваша ставка (введите число): ',
                            width=50,
                            font='Consolas 14',
                            fg = 'black',
                            bg = '#bf0606',
                            justify='center')
text_bet.pack()

bet_entry = Entry(root, font = "Comforta 20",
            fg ='black',
            bg ='white',
            justify='center',
            relief='solid',
            width=5)
bet_entry.pack()

text_digit = Label(text='На какое число Вы ставите? ',
                            width=50,
                            font='Consolas 14',
                            fg = 'black',
                            bg = '#bf0606',
                            justify='center')
text_digit.pack()


bet_button = Button (text = "Принять ставку",
                     font = 'Consolas 14',
                     fg = 'black',
                     bg = '#359127',
                     justify = 'center',
                     relief = 'raised')
bet_button.pack()

digit_entry = Entry(root, font="Comforta 20",
                            fg='black',
                            bg='white',
                            justify='center',
                            relief='solid',
                            width=5)

digit_entry.pack()
play_button = Button(root, text='Играть',
                     font='Consolas 20',
                     fg='black',
                     bg='green',
                     justify='center')



#bet_button.bind('<Button-1>', bet_check)
play_button.bind('<Button-1>', casino)


play_button.pack()
'''


