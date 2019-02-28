Willekeurig = input('Voer hier een willekeurige zin in:')
def gemiddelde(invoer):
    lst = [len(x) for x in invoer.split()]
    gem = sum(lst) / len(lst)
    return round (gem, 2)
print('De gemiddelde lengte van de woorden is: ' + str(gemiddelde(Willekeurig)))