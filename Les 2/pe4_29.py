while True:
    woord = input('Geef een string van vier letters:')
    if len(woord) == 4:
        print('Inlezen van correcte string: ' + str(woord) + ' is geslaagd.')
        break
    else:
        lengte = len(woord)
        print(str(woord) + ' heeft ' + str(lengte) + ' letters.')