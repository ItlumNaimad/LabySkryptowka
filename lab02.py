#shebang line
#!C:\Program Files\JetBrains\PyCharm 2024.2.3\bin
'''
Nie wiem gdzie mam kompilator w środowisku JETBrainsowym
Więc wklejam adres do PyCharma
'''
# MIEJSCE NA IMPORTY

#STAŁE
CONST: int = 1
INNA_NAZWA: str = 'Wciąż jest stałą'
#ZMIENNE
fajna_liczba = 1.73
#FUNKCJA DO WYŚWIETLENIA NAPISU
def hello() -> None:
    print('Hello World!')
#FUNKCJA MAIN
def main() -> None:
    hello()
    #zmienna globalna w funkcji main
    global zmienna_w_mainie
    zmienna_w_mainie = 7

if __name__ == '__main__':
    main()



