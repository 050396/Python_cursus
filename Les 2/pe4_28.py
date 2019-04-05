list = []
while True:
    getallen = int(input('Geef een getal:'))

    if getallen == 0:
        break

    else:
        list.append(getallen)
        aantalG = len(list)
        somG = sum(list)

print('Er zijn ' + str(aantalG) + ' getallen ingevoerd, de som is: ' + str(somG) )
