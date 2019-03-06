jaargetijde = int(input('De hoeveelste maand van het jaar is het?'))
maandnummer = [[3, 4, 5], [6, 7, 8], [9, 10, 11], [12, 1, 2]]
def seizoen (maand):
    if maand in maandnummer [0]:
        print('Het is lente')
    elif maand in maandnummer [1]:
        print('Het is zomer')
    elif maand in maandnummer [2]:
        print('Het is herfst')
    elif maand in maandnummer [3]:
        print('Het is winter')
    return jaargetijde
seizoen (jaargetijde)