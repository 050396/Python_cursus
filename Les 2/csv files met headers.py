import csv

def makeFile(List, filename):
    with open(filename, 'w', newline='') as csvfile:
        header = ['Artikelnummer', 'Artikelcode', 'Naam', 'Voorraad', 'Prijs']
        filewriter = csv.writer(csvfile, delimiter=';')
        filewriter.writerow(header)

        for Row in List:
            filewriter.writerow(Row)

def readFile(filename):
    with open(filename, 'r') as csvfile:
        filereader = csv.reader(csvfile, delimiter=';')

        next(filereader, None)

        duursteProductPrijs = 0
        duursteProductNaam = ''
        minsteArtikelnummer = ''
        minsteAantal = -1
        totaal = 0
        for row in filereader:
            if float(row[4]) > duursteProductPrijs:
                duursteProductPrijs = float(row[4])
                duursteProductNaam = row[2]

            if int(row[3]) < minsteAantal or minsteAantal == -1 :
                minsteArtikelnummer = row[2]
                minsteAantal = int(row[3])

            totaal += int(row[3])

    print('Het duurste artikel is {} en die kost {} Euro'.format(duursteProductNaam,duursteProductPrijs))
    print('Er zijn slechts {} exemplaren in voorraad van het product met nummer {}'.format(minsteAantal, minsteArtikelnummer))
    print('In totaal hebben wij {} producten in ons magazijn liggen'.format(totaal))

content = [
    [121, 'ABC123', 'Highlight pen', 231, 0.56],
    [123, 'PQR678', 'Nietmachine', 587, 9.99],
    [128, 'ZYX163', 'Bureaulamp', 34, 19.95],
    [137, 'MLK709', 'Monitorstandaard', 66, 32.50],
    [271, 'TRS665', 'Ipad hoes', 155, 19.01]
]

makeFile(content, 'gegevens.csv')
readFile('gegevens.csv')