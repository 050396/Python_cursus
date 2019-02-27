with open('Kaartnummers.txt') as f:
    for regel in f:

        regel1 = regel.split(",")
        kaartnummer = regel1[0]
        naam = (regel1[1].strip())

        print(naam + " heeft kaartnummer: " + kaartnummer)