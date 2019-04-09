from random import randint
def monopolyworp():
    count = 0
    for i in range(1,4):

        x, y = randint(1,6), randint(1,6)
        z = x + y
        if x != y:
            print(x, ' + ', y, ' = ' + str(z))
            break
        elif x == y and count < 2:
            print(x, ' + ', y, ' = ' + str(z) + ' (dubbel)')
            count += 1
        elif count == 2 and x == y:
            print(x, ' + ', y, ' = ' + str(z) + ' (direct naar gevangenis)')
            break

monopolyworp()