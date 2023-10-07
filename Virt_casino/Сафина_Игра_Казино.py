from tkinter import *
from tkinter import messagebox
import random
import time
# window settings
root = Tk()
root.resizable(width=False, height=False)
root.attributes('-alpha', 1) # прозрачность окна

root.geometry('500x500+400+100')
root.title('" PONAROSHKU-Казино"')
root['bg'] = '#bf0606'
root.iconbitmap('icn_r.ico')


# Функции
# Создаем второе окно- для объявления выигрыша/проигрыша
def new_window():
    global count, btn_new_game, us_num, digit_cas, bet, bet_entry, us_entry, lbl_instruction, lbl_win, play_button, num_hl
    def new_game():
        global count, btn_new_game, us_num, digit_cas, bet, bet_entry, us_entry, lbl_instruction, lbl_win, play_button, num_hl
        bet_entry.delete('0', END)
        us_entry.delete('0', END)
        lbl_count.config(text=f'Счет: {count}')
        new_window.destroy()
        var.set(0)

    new_window = Toplevel()
    new_window.resizable(width=False, height=False)
    new_window.attributes('-alpha')  # прозрачность окна
    new_window.geometry('500x500+400+100')
    new_window.title('" PONAROSHKU-Казино"')
    new_window['bg'] = '#bf0606'
    new_window.iconbitmap('icn_r.ico')
    lbl_win = Label(new_window, text='',
                font='Consolas 14',
                fg='black',
                bg='#bf0606',
                justify='center')
    btn_new_game = Button(new_window, text='Новая игра',
                      font='Consolas 14',
                      fg='black',
                      bg='green',
                      justify='center',
                      command=new_game
                      )
    lbl_win.grid(row=0, column=0, padx=30, pady=100)
    btn_new_game.grid(row=1, column=0, padx=50, pady=100)

def r_b():
    lbl_instruction['text']='Выберите Красное или Черное поле'
    red_btn.grid(row=10, column=1,  padx=20, pady=5)
    black_btn.grid(row=10, column=2,  padx=20, pady=5)
    play_button.grid(row=11, column=1, columnspan=2, stick='we', padx=40, pady=15)
    play_button.bind('<Button-1>', play_rb)

def play_rb(event):
    global var_2, value,red, us_rb_origin, us_rb_remove, us_rb_lower, bet, bet_entry, us_entry, lbl_instruction,lbl_win, count
    try:
        bet = int(bet_entry.get())
    except ValueError:
        messagebox.showerror('int_error-1', 'Ваша ставка не может быть принята.\n'
                                            'Допускается только число больше 0!')
        bet_entry.delete('0', END)
    bet = int(bet_entry.get())
    if bet<=count and count>0:
        new_window()
        red = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
        digit_cas = random.randint(0, 36)
        value = int(var_2.get())

        if digit_cas in red:
            if value == 0:
                lbl_win.config(text=f'Поздравляем!Сыграло число {digit_cas} - красное.\n'
                                    f'Ваш выигрыш {(bet * 2)} фантиков\n')
                count = count + bet * 2
            else:
                lbl_win.config(text=f'Увы!Сыграло число {digit_cas} - красное.\n')
                count = count - bet

        elif digit_cas == 0:
            lbl_win.config(text=f'Увы!Сыграло число Zerro.\n')
            count = count - bet

        else:
            if value == 0:
                lbl_win.config(text=f'Увы!Сыграло число  {digit_cas} - черное .\n')
                count = count - bet
            else:
                lbl_win.config(text=f'Поздравляем!Сыграло число {digit_cas} - черное.\n'
                                    f'Ваш выигрыш {(bet * 2)} фантиков\n')
                count = count + bet * 2

    elif bet>count:
        lbl_count.config(text=f'Cчет: {count}')
        messagebox.showerror('error', 'Ваша ставка не может быть принята.\n'
                                  'На счету недостаточно средств!')
        bet_entry.delete('0', END)

def h_l():
    red_btn.destroy()
    black_btn.destroy()
    lbl_instruction.config(text=f'Введите число от 0 до 36: ')
    us_entry.grid(row=10, column=1, columnspan=2, stick='we', padx=40, pady=5)
    play_button.grid(row=11, column=1, columnspan=2, stick='we', padx=40, pady=15)
    play_button.bind('<Button-1>', play_hl)

def play_hl(event):
    global count, btn_new_game, us_num, digit_cas, bet, bet_entry, us_entry, lbl_instruction, lbl_win, play_button, num_hl
    try:
        bet = int(bet_entry.get())
        us_num = int(us_entry.get())
    except ValueError:
        messagebox.showerror('int_error-1', 'Ваша ставка не может быть принята.\n'
                                            'Допускается только число больше 0!')
        bet_entry.delete('0', END)
        us_entry.delete('0', END)

    bet = int(bet_entry.get())
    if bet <= count and count > 0 and 0<=us_num<=36:
        new_window()
        digit_cas = random.randint(0, 36)
        if 0 <= digit_cas <= 18:

            if 0 <= us_num <= 18:
                lbl_win.config(text=f'Сыграло число {digit_cas} - малое число. \n'
                                    f'Поздравляем! Ваш выигрыш составил {bet * 2} фантиков')
                count = count + bet * 2
            elif 19 <= us_num <= 36:
                lbl_win.config(text=f'Увы!Сыграло число {digit_cas} - малое число. \n')
                count = count - bet

        else:
            if 0 <= us_num <= 18:

                lbl_win.config(text=f'Увы!Сыграло число {digit_cas} - малое число. \n'
                               )

                count = count - bet
            elif 19 <= us_num <= 36:
                lbl_win.config(text=f'Сыграло число {digit_cas} - большое число. \n '
                                    f'Поздравляем! Ваш выигрыш составил {bet * 2}')
                count = count + bet * 2


    elif bet>count and 0<=us_num<=36:
        lbl_count.config(text=f'Cчет: {count}')
        messagebox.showerror('error', 'Ваша ставка не может быть принята.\n'
                                      'На счету недостаточно средств!')
        bet_entry.delete('0', END)

    else:
        messagebox.showerror('error', 'Ваша ставка не может быть принята.\n'
                                      )
        us_entry.delete('0', END)


def num():
    red_btn.destroy()
    black_btn.destroy()
    lbl_instruction.config(text=f'Введите число от 0 до 36: ')
    us_entry.grid(row=10, column =1, columnspan=2, stick='we',padx=50, pady=5)
    play_button.grid(row=11,column =1, columnspan=2, stick='we',padx=40, pady=15)
    play_button.bind('<Button-1>', play_num)

def play_num(event):
    global us_num, digit_cas, bet, bet_entry, us_entry, lbl_instruction, lbl_win, play_button, count
    try:
        bet = int(bet_entry.get())
        us_num = int(us_entry.get())
    except ValueError:
        messagebox.showerror('int_error-1',
                             'Ваша ставка не может быть принята.\n'
                             'Допускается только число больше 0!')
        bet_entry.delete('0', END)
        us_entry.delete('0', END)

    bet = int(bet_entry.get())
    us_num = int(us_entry.get())
    if bet <= count and count > 0 and 0<=us_num<=36:
        new_window()
        digit_cas = random.randint(0, 36)

        if us_num == digit_cas:  # Если пользователь выиграл
            lbl_win.config(text=f'Сыграло число {digit_cas}. \n'
                                f'Поздравляем! Ваш выигрыш \n'
                                f'составил {bet * 35} фантиков')
            count = count + bet * 35
        else:
            lbl_win.config(
                text=f'Увы, сыграло число {digit_cas}.\n Попробуйте еще раз,\n удача обязательно улыбнется Вам!')
            count = count - bet

    elif bet>count and 0<=us_num<=36:
        lbl_count.config(text=f'Cчет: {count}')
        messagebox.showerror('error', 'Ваша ставка не может быть принята.\n'
                                      'На счету недостаточно средств!')
        bet_entry.delete('0', END)

    else:
        messagebox.showerror('error', 'Ваша ставка не может быть принята.\n'
                             )
        us_entry.delete('0', END)

# Виджеты

lbl_name = Label (text = 'Игрок: ',
                            font = 'Consolas 12',
                            fg = 'black',
                            bg = '#bf0606')

name_entry = Entry(width= 20,
                   font='Consolas 12',
                   fg='black',
                   bg='white'
                   )
count = 100
lbl_count = Label(text = f'Счет: {count}',
                    width = 10,
                    font = 'Consolas 12',
                    fg = 'black',
                    bg = '#bf0606'
                     )

lbl_welcome = Label(text = 'Добро пожаловать \nв виртуальное казино!',
                            font = 'Consolas 14', # Если в названии шрифта несколько слов
                            # (например, Times New Roman), то слова в названии
                            # писать через нижнее подчеркивание
                            fg = 'black',
                            bg = '#bf0606'
                            )

lbl_choice = Label (text = 'Выберите категорию игры',
                            font = 'Consolas 12', # Если в названии шрифта несколько слов
                            # (например, Times New Roman), то слова в названии
                            # писать через нижнее подчеркивание
                            fg = 'black',
                            bg = '#bf0606',
                            justify='center'
                            )
var = IntVar()
var.set(0)
red_black = Radiobutton (text = 'Красное или Черное',
                         variable= var,
                         value = 1,
                         bg='#bf0606',
                         font='Consolas 12',
                         justify='left',
                         command=r_b
                         )

hight_low = Radiobutton (text = 'Большое или Малое',
                         variable= var,
                         value = 2,
                         bg='#bf0606',
                         font='Consolas 12',
                        justify='left',
                         command=h_l
                         )

number = Radiobutton (text = 'Прямая ставка',
                         variable= var,
                         value = 3,
                        bg='#bf0606',
                        font='Consolas 12',
                        justify='left',
                        command=num
                      )

text_bet = Label(text='Ваша ставка (введите число): ',
                          font='Consolas 12',
                          fg = 'black',
                          bg = '#bf0606',
                          justify='center'
                                         )
bet_entry = Entry( font = "Consolas 12",
            fg ='black',
            bg ='white',
            justify='center',
            relief='solid')


# дополнительное поле ввода после выбора категории игры (сначала оно невидимое, т.к. пустое)
lbl_instruction = Label(text = '',
                            font = 'Consolas 12',
                            fg = 'black',
                            bg = '#bf0606',
                            justify='center')

var_2 = IntVar()
var_2.set(0)
red_btn = Radiobutton (text = 'Красное',
                         variable= var_2,
                         value = 0,
                         bg='#bf0606',
                         font='Consolas 12',
                         justify='left'
                          )

black_btn = Radiobutton (text = 'Черное',
                         variable= var_2,
                         value = 1,
                         bg='#bf0606',
                         font='Consolas 12',
                         justify='left'
                          )

us_entry = Entry(root,
            font = "Consolas 12",
            fg ='black',
            bg ='white',
            justify='center',
            relief='solid')

play_button = Button(root, text='Играть',
                         font='Consolas 16',
                         fg='black',
                         bg='green',
                         justify='center'
                     )

# Распаковка
lbl_name.grid(row=0,column=0,padx=10, pady=10)
name_entry.grid(row=0,column=1,columnspan=2, stick='we', pady=10)
lbl_count.grid(row=0,column=2, columnspan=2,stick='we',pady=10)
lbl_welcome.grid(row=1,column=1, columnspan=3, stick='we', pady=10)
lbl_choice.grid(row=3,column=1, columnspan=3, stick='we', pady=10)
red_black.grid(row=4,column=1, columnspan=3, stick='w',padx=50)
hight_low.grid(row=5,column=1, columnspan=3, stick='w',padx=50)
number.grid(row=6,column=1, columnspan=3, stick='w',padx=50)
text_bet.grid(row=7, column=1,columnspan=3, stick='we', pady=5)
bet_entry.grid(row=8, column=1,columnspan=2, stick='we', padx=50, pady=5)
lbl_instruction.grid(row=9,column=1, columnspan=3, stick='we', pady=10)


root.mainloop()

