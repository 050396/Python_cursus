infile = open('bedrijfsnaam_tickersymbol.txt', 'a')
bedrijf = input('Naam bedrijf:')
symbool = input ('Ticker-symbool:')
infile.write(str(bedrijf) + ':' + str(symbool) + '\n')
infile.close()

myfile = open('bedrijfsnaam_tickersymbol.txt', 'r')
while True :
        def ticker(filename):
            tickerDict = {}
            for line in myfile.readlines():
                cmp = line.split(":")[0].rstrip()
                code = line.split(":")[1].rstrip()
                tickerDict[cmp] = code.rstrip()
            return tickerDict

        info = ticker(myfile)
        def getInfo(inp):
            s=''
            for cmp , code in info.items():
                if inp.upper().rstrip() == cmp.upper().rstrip():
                    s = ('tickersymbol: ' + str(code) + '\n')
                    break
                elif inp.upper().rstrip() == code.upper().rstrip():
                    s = ('bedrijfsnaam: '+ str(cmp))
                    break
                else:
                    s = ('Input not found! ' )
            return s