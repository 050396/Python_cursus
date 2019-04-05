cijferlijst = {'Piet': 7, 'Jan': 8.8, 'Klaas': 5, 'Henk': 9.4, 'Eva': 9.8, 'Anna': 6.5, 'Pieter': 4.5, 'Bas': 3}
for key, value in cijferlijst.items():
    if value > 9.0:
        print(key, value)
    else:
        continue