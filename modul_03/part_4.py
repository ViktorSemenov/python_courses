import json

#data_login = {'ternip': 321}
#with open('log.json', 'w') as f:
    #json.dump(data_login, f)

def register(login, passwd):
    with open('log.json', 'r') as f:
        data_login = json.load(f)
    if login not in data_login.keys():
        data_login[login] = passwd
        print('Регистрация прошла успешна')
        with open('log.json', 'w') as f:
            json.dump(data_login, f)
    else:
        print('Такой логин уже существует')

def login_function(login, passwd):
    with open('log.json', 'r') as f:
        data_login = json.load(f)
    if login in data_login.keys():
        if data_login[login] == passwd:
            print('Успешный вход')
        else:
            print('Пароль не верный')
    else:
        print('Логин не верный')


print('Регистрация - введите 1 или Вход - введите 2?')
a = int(input())
if a == 1:
    register(input('Введите логин'),input('Введите пароль'))
elif a == 2:
    login_function(input('Введите логин'), input('Введите пароль'))
else:
    print('Введите 1 или 2')


