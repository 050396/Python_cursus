jaargetijde = int(input('De hoeveelste maand van het jaar is het?'))
lst = [['maart, april, mei'], ['juni, juli, augustus'], ['september, oktober, november'], ['december, januari, februari']]
def seizoen (maand):
    if lst[0:3]:
        print('Het is lente')
    if lst[3:6]:
        print('Het is zomer')
    if lst[6:9]:
        print('Het is herfst')
    if lst[9:12]:
        print('Het is winter')
    return jaargetijde
seizoen (lst)
