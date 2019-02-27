infile = open('Kluizen.txt', 'w')
infile.close()

Menu = eval(input('1: Ik wil weten hoeveel kluizen nog vrij zijn\n2: Ik wil een nieuwe kluis\n3: Ik wil even iets uit mijn kluis halen\n4: Ik geef mijn kluis terug'))

def toon_aantal_kluizen_vrij(aantal):
    aantal_kluizen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    beschikbaar = ()
    for kluis in aantal_kluizen:
        if kluis in beschikbaar
            beschikbaar += 1
        else:
            beschikbaar += 0
