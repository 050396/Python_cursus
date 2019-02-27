teller = 0

with open('Kaartnummers.txt') as f:
    for regel in f:
        teller += 1
    print('Deze file telt ' + str(teller) + ' regels')

infile = open('Kaartnummers.txt','r')
lst = []
for lijst in infile.readlines():
    items = lijst.split(',')
    nummer = items [0]
    lst.append (nummer)
grootstenummer = max(lst)
regelnummer = lst.index(grootstenummer) + 1

print('Het grootste kaartnummer is: ' + str(grootstenummer) + ' en dat staat op regel ' + str(regelnummer))