invoerstring = input("Voer uw naam, beginstation en eindstation in: ")


def code(invoerstring):
    karakter = ""
    for letters in invoerstring:
        s = ord(letters) + 3
        t = chr(s)
        karakter += t
    print(karakter)

code(invoerstring)