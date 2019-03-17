print('\n\n')

UNITS_SYMBOLS = ['I', 'V', 'X']
TENS_SYMBOLS = ['X', 'L', 'C']
HUNDREDS_SYMBOLS = ['C', 'D', 'M']
THOUSANDS = ['M'] * 9


def ask_for_number_and_check_validity():  # zapytanie o numer i sprawdzenie czy input jest taki jak oczekujemy
    while True:
        number_str = input('PLease enter a number from 1 to 3999: ')
        try:
            number = int(number_str)
        except ValueError:
            continue
        if number < 1 or number > 3999:
            continue
        else:
            return number_str


number = ask_for_number_and_check_validity()


def change_number_to_reversed_list(number):
    # zmiana numeru na odwrocona liste w celu sprawdzenia cyfr od jednosci
    return [int(i) for i in reversed(number)]

reversed_number_list = change_number_to_reversed_list(number)


def check_digit(reversed_number, symbols, roman_list):  # sprawdzenie pojedynczej cyfry z odwróconej listy i dodanie rzymskiej do nowej listy
    if 0 < reversed_number < 4:
        for j in range(reversed_number):
            roman_list.append(symbols[0])
    elif 5 < reversed_number < 9:
        for j in range(reversed_number - 5):
            roman_list.append(symbols[0])
        roman_list.append(symbols[1])
    elif reversed_number == 4:
        roman_list.append(symbols[1])
        roman_list.append(symbols[0])
    elif reversed_number == 9:
        roman_list.append(symbols[2])
        roman_list.append(symbols[0])
    elif reversed_number == 5:
        roman_list.append(symbols[1])


def check_number_digits_and_add_roman_symbols(reversed_number_list, number):  # stworzenie listy z rzymskimi znakami
    roman_list = []
    for symbols, i in zip([UNITS_SYMBOLS, TENS_SYMBOLS, HUNDREDS_SYMBOLS, THOUSANDS], range(len(number))):
        check_digit(reversed_number_list[i], symbols, roman_list)
    return roman_list


roman_list = check_number_digits_and_add_roman_symbols(reversed_number_list, number)


def change_list_to_roman_number(roman_list):  # odwrócenie listy z rzymskimi znakami i polaczenie elementow w celu stworzenia rzymskiej liczby
    return ''.join(reversed(roman_list))


roman_number = change_list_to_roman_number(roman_list)

print('\n\n')
print('Your Roman Number is:    ' + roman_number)
print('\n\n')
