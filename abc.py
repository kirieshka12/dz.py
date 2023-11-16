try1 = 0

while try1 < 3:
    username = input('Введите логин: ')
    password = input('Введите пароль: ')

    if username == 'kirieshka' and password == 'kirieshka997':
        print('Вы успешно авторизировались!')
        break
    else:
        print('Неверно введены данные. Проверьте выключен ли у вас капслок.')
        try1 += 1
