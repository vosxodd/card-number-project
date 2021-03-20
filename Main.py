def is_correct_length(number):
    """Проверка количества цифр в номере карты"""
    if 16 >= len(number) >= 13:
        return True


def correct_number():
    """Проверка номера карты на правильность по алгоритму Ганса Луна"""
    global number
    abc = {i: -i + 8 for i in range(len(number))}     # Цифры проверяемой последовательности нумеруются справа налево, начиная с 1
    number = list(number)
    for i in abc:
        if abc[i] % 2 == 0:                           # Цифры, стоящие на чётных местах, умножаются на 2
            c = int(number[i]) * 2
            if c > 9:                                 # Если в результате такого умножения возникает число больше 9, оно заменяется 
                s = 0                                 # суммой цифр получившегося произведения — однозначным числом, то есть цифрой.
                for char in str(c):
                    s += int(char)                    
                    number[i] = str(s)
            elif c <= 9:                              # Отдельное условие для случая, когда после умножения число меньше 9
                f = int(number[i]) * 2
                number[i] = str(f)
    number = ''.join(number)


def checker(number):
    """Сложение цифр в преобразованном номере и проверка на кратность 10"""
    sum = 0
    for char in number:
        sum += int(char)                              # Все полученные в результате преобразования цифры складываются
    if sum % 10 == 0:                                 # Если сумма кратна 10, то исходные данные верны
        return True


def type_card(number):
    """Определение типа карты по началу её номера"""
    if number[0] == '2':
        print('Это карта Discover')
    elif number[0] == '4':
        print('Это карта Visa')
    elif number[0] == '5':
        print('Это карта MasterCard')
    elif number[0] == '6':
        print('Это карта Национальная платёжная система \"Мир\"')
    elif number[:2] == '37':
        print('Это карта American Express')
    else:
        print('Неправильный номер карты')


def secure():
    """Финальная проверка правильности введённого номера """
    if length == True and check == True:
        return True


number = input()
old_number = number
length = is_correct_length(number)
correct_number()
check = checker(number)
safe = secure()

if safe == True:
    type_card(old_number)
else:
    print('Неправильный номер карты')
