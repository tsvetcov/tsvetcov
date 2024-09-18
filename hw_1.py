def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    
    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()

def step2_umbrella():
    print(
        'Утка-маляр взяла зонтик. Она идет по улице. '
        'Вернуться ей домой?'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    
    if options[option]:
        return step3_home()
    return step3_donot_go_home()

def step3_home():
    print(
        'Утка-маляр идет домой. '
    )
    return

def step3_donot_go_home():
    print(
        'Утка-маляр идет дальше. '
        'Она устала. Вернуться ей домой?'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    
    if options[option]:
        return step3_home()
    return step3_donot_go_home()

def step2_no_umbrella():
    print(
        'Утка-маляр не взяла зонтик. Она идет домой. '
    )
    return step3_home()

if __name__ == '__main__':
    step1()

