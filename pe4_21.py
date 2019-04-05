print('Keuzemenu:\n1: Ik wil weten hoeveel kluizen nog vrij zijn\n2: Ik wil een nieuwe kluis\n3: Ik wil even iets uit mijn kluis halen\n4: Ik geef mijn kluis terug')
keuze = int('Maak een keuze:')

def toon_aantal_kluizen_vrij(aantal):
    infile = open('Kluizen.txt' , 'r')
    lstregels = infile.readlines ()
    aantal_kluizen = len(lstregels)
    return aantal_kluizen
toon_aantal_kluizen_vrij()

def nieuwe_kluis(getal):
    antwoord = ''
    allekluizen = []
    kluisnummers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    infile = open ('Kluizen.txt' , 'r')
    regels = infile.readlines()
    for regel in regels:
        onderdelen = regel.split(';')
        allekluizen.append(onderdelen)
        kluis = int(onderdelen[0])
        kluisnummers.remove(kluis)
    infile.close()
    if (beschikbarekluizen == []):
        antwoord = ('Helaas, er zijn geeen kluizen beschikbaar.')
    elif (beschikbarekluizen != []):
        ww = input('Voer een wachtwoord in' + '\n')
        kluisnr = beschikbarekluizen[0]
        infile = open('Kluizen.txt' , 'a')
        infile.write(kluisnr + ';' + ww + '\n')
        antwoord =('U heeft kluisnummer: ' + kluisnr + ' en uw wachtwoord is: ' + ww)
        infile.close()
    return print(antwoord)

if keuze == 1:
    vrije_kluizen =
    print ('Er zijn nog ' + str(vrije_kluizen) + ' kluizen vrij')
elif keuze == 2:
    nieuwe_kluis
    print (')
elif keuze == 3:
    open_kluis
elif keuze == 4:
    teruggeven_kluis