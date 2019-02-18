grondgetallen = [4, 6, 7, -3, -1, 8]
def kwadranten_som(grondgetallen):
    som = 0
    for getal in grondgetallen:
        if getal > 0:
            som += getal ** 2
            return som
    print(kwadranten_som (grondgetallen))

