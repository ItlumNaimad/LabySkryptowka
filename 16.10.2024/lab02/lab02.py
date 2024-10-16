#shebaradius=None:\Program Files\JetBrains\PyCharm 2024.2.3\bin
'''
Python sam w pewnym momencie zedytował sheba
'''
# MIEJSCE NA IMPORTY
import sys #import sys dla zad 2
import datetime as dt #dla zad3
from math import pi #dla zad4

#STAŁE

#ZMIENNE

#FUNKCJA DO WYŚWIETLENIA NAPISU
''' ZAD1
def hello() -> None:
    print('Hello World!')
'''
#ZAD 2
def wersja_py() -> None:
    print("Wersja Pythona:", sys.version)
#ZAD 3
def today():
    ''' użyta funkcja odwołuje się do modułu datetime
    w bibliotece datetime (użyłem aliasu dt) i korzysta
    z metody now do pobrania aktualnej daty i godziny
    a za pomocą strftime() mogę formatować sposób pokazywanych
    danych dotyczących czasu
    '''
    rightnow = dt.datetime.now()
    format_1 = rightnow.strftime('%d.%m.%Y %H:%M:%S')
    format_2 = rightnow.strftime('%m.%d.%Y %I:%M:%p')
    format_3 = rightnow.strftime('%A, %d %B %Y %H:%M:%S')

    print("Format DD.MM.YYYY + GODZ.MIN.SEK:", format_1)
    print("Format MM.DD.YYYY + GODZ.MIN AM/PM:", format_2)
    print("Format DZ_TYG, DD.NAZW_MIES YYYY + GODZ.MIN.SEK:", format_3)

def circle_area(radius):
    area=pi*radius^2
#FUNKCJA MAIN
def main() -> None:
    today()

if __name__ == '__main__':
    main()



