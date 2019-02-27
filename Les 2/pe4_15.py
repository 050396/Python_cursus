Graden_Celsius = float(input('Temperatuur in Celsius:'))
def convert (temperatuureenheid):
    Graden_Fahrenheit = Graden_Celsius * 1.8 + 32
    return Graden_Fahrenheit
print('Temperatuur in Fahrenheit:')

def table(temperatuureenheid):
    print('{:8} {:8}'.format('F', 'C'))
    for i in range(-30, 50, 10):
        print ('{:8} {:8.1f}'.format(i * 1.8 + 32, i))
table(Graden_Celsius)