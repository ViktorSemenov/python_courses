import json

#data_login = {'ternip': 321}
#with open('log.json', 'w') as f:
    #json.dump(data_login, f)


def register(login, passwd):
    with open('log.json', 'r') as f:
        data_login = json.load(f)
    if login not in data_login.keys():
        data_login[login] = passwd
        with open('log.json', 'w') as f:
            json.dump(data_login, f)
    else:
        print('Такой логин уже существует')

register('ghbdtn', 'hjkdshkjsd')