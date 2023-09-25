s = int(input("Введите сообщение для Алисы:  "))
while True:
    type = type(s)
    print(type)
    if type == int:
        print('Yes')
    s = int(input("Введите сообщение для Алисы:  "))
print('No')
