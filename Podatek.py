procent1 = 0.1775
procent2 = 0.32
nazwapliku = input('Podaj nazwę pliku: ')
while True:
    try:
        with open(nazwapliku + '.txt', encoding='windows-1250') as f:
            read_data = f.read().split('\n')
        break
    except:
        print('Błędna nazwa pliku, podaj ją jeszcze raz')
        nazwapliku = input('Podaj nazwę pliku: ')


def liczpodatek(przychod):
    # print('Przychód: ', przychod)
    if przychod <= 8000:
        # print('8000')
        kzp = 1360
        podatek = (przychod*procent1)-kzp
        #  print('kzp', kzp)
        # print('podatek',podatek)

    if przychod >= 8001 and przychod < 13000:
        #  print('8000 - 13000')
        kzp = 1420-871.70*(przychod-8000)/5000
        # print('kzp', kzp)
        podatek = (przychod*procent1)-kzp
        # print('podatek',podatek)

    if przychod > 13001 and przychod < 85528:
        # print('13000 - 85528')
        kzp = 548.30
        podatek = (przychod*procent1)-kzp
        # print('kzp', kzp)
        #  print('podatek',podatek)

    if przychod > 85529 and przychod < 127000:
        # print('85528 - 127000')
        kzp = 548.30-(548.30*(przychod-85528)/41472)
        podatek = (15181.22 + ((przychod-85528)*procent2)) - kzp
        # print('kzp', kzp)
        # print('podatek',podatek)

    if przychod > 127000 :
        # print('> 127000')
        podatek = (15181.22 + ((przychod-85528)*procent2))
        # print('podatek', podatek)
    if przychod > 1000000:
        #  print('> 1000000')
        podatek = (15181.22 + ((przychod-85528)*procent2)) + (przychod-1000000)*0.04
        # print('podatek', podatek)
    return podatek

listadozapisu = []

for entry in read_data:
    przychod = entry.split('; ')[1].replace(' zł', '')
    imie = entry.split('; ')[0]
    listadozapisu.append(imie+'; '+str(round(liczpodatek(int(przychod)))) + ' zł')

# print(listadozapisu)

with open('podatek.txt', "w", encoding='windows-1250',) as f:
    for entry in listadozapisu:
        f.write(entry +'\n')
