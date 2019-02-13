print('\n\n')

UNITS_SYMBOLS = ['I', 'IV', 'V', 'IX']
TENS_SYMBOLS = ['X', 'XL', 'L', 'XC']
HUNDREDS_SYMBOLS = ['C', 'CD', 'D', 'CM']
THOUSAND = 'M'


def ask_for_number_and_check_validity():  # zapytanie o numer i sprawdzenie czy input jest taki jak oczekujemy
    while True:
        number = input('PLease enter a number from 1 to 3999: ')
        try:
            int(number)
        except ValueError:
            continue
        if int(number) < 1 or int(number) > 3999:
            continue
        else:
            return number


number = ask_for_number_and_check_validity()


def change_number_to_reversed_list(number):
    # zmiana numeru na odwrocona liste w celu sprawdzenia cyfr od jednosci
    number_list = list(number)
    number_list = [int(i) for i in number_list]
    number_list.reverse()
    return number_list


reversed_number_list = change_number_to_reversed_list(number)


def check_digit(reversed_number_list, symbols, i, roman_list):  # sprawdzenie pojedynczej cyfry z odwróconej listy i dodanie rzymskiej do nowej listy
    if 0 < reversed_number_list[i] < 4:
        for j in range(reversed_number_list[i]):
            roman_list.append(symbols[0])
    elif 5 < reversed_number_list[i] < 9:
        for j in range(reversed_number_list[i]-5):
            roman_list.append(symbols[0])
        roman_list.append(symbols[2])
    elif reversed_number_list[i] == 4:
        roman_list.append(symbols[1])
    elif reversed_number_list[i] == 9:
        roman_list.append(symbols[3])
    elif reversed_number_list[i] == 5:
        roman_list.append(symbols[2])


def check_number_digits_and_add_roman_symbols(reversed_number_list, number):  # stworzenie listy z rzymskimi znakami
    roman_list = []
    for i in range(len(number)):
        if i == 0:
            symbols = UNITS_SYMBOLS
            check_digit(reversed_number_list, symbols, i, roman_list)
            i += 1
        elif i == 1:
            symbols = TENS_SYMBOLS
            check_digit(reversed_number_list, symbols, i, roman_list)
            i += 1
        elif i == 2:
            symbols = HUNDREDS_SYMBOLS
            check_digit(reversed_number_list, symbols, i, roman_list)
            i += 1
        elif i == 3:
            thousands = reversed_number_list[i]*THOUSAND
            roman_list.append(thousands)
        else:
            i += 1
    return roman_list


roman_list = check_number_digits_and_add_roman_symbols(reversed_number_list, number)


def change_list_to_roman_number(roman_list):  # odwrócenie listy z rzymskimi znakami i polaczenie elementow w celu stworzenia rzymskiej liczby
    roman_list.reverse()
    roman_number = ''.join(roman_list)
    return roman_number


roman_number = change_list_to_roman_number(roman_list)

print('\n\n')
print('Your Roman Number is:    ' + roman_number)
print('\n\n')
