a = eval(input('Geef lijst met minimaal 10 strings:'))
lst = []
i = 0
for woorden in a:
    if ((len(a[i]) == 4)):
        lst.append(a[i])
    i += 1

print('De nieuw gemaakte lijst met alle vier-letter strings is:' + str(lst))