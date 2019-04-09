headers = ['Artikelnummer', 'Artikelcode', 'Naam', 'Voorraad', 'Prijs']
artikelen = {
    ('121', 'ABC123', 'Highlight pen', '231', '0.56'),
    ('123','PQR678', 'Nietmachine', '587', '9.99'),
    ('128','ZYX163', 'Bureaulamp', '34', '19.95'),
    ('137','MLK709', 'Monitorstandaard', '66', '32.50'),
    ('271','TRS665', 'Ipad hoes', '155', '19.00')
}

infile=open('artikelen.csv', 'w'):
    infile.truncate()
    infile.write(';'.join(headers))
    infile.write('\n')
    for artikel in artikelen:
        infile.write(';'.join(artikel))
        infile.write('\n')
    infile.close()

infile=open('artikelen.csv', 'r'):
    infile.readline()
    content = infile.readlines()
    artikelen = []
    voorraden = []
    for line in content:
        nummer, code, naam, voorraad, prijs = line.rstrip().split(';')
        artikelen.append((int(nummer), code, naam, int(voorraad), float(prijs)))
        voorraden.append(int(voorraad))

    duursteArtikel = sorted(artikelen, key=lambda x: x[4])[-1]
    print('Het duurste artikel is {} en die kost '
          '{} Euro'.format(duursteArtikel[2], duursteArtikel[4]))

    kleinsteVoorraad = sorted(artikelen, key=lambda x: x[3])[0]
    print('Er zijn slechts {} exemplaren in voorraad van het product '
          'met nummer {}'.format(kleinsteVoorraad[3], kleinsteVoorraad[0]))

    aantal = sum(voorraden)
    print('In totaal hebben wij {} producten in ons magazijn '
          'liggen'.format(aantal))
infile.close()