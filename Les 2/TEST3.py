myfile = open('ticker.txt', 'r')
while True :
        def ticker(filename):
            tickerDict = {}
            for line in filename.readlines():
                bedrijf = line.split(":")[0].rstrip()
                symbool = line.split(":")[1].rstrip()
                tickerDict[bedrijf] = symbool.rstrip()
            return tickerDict

        info = ticker(myfile)
        def getInfo(inp):
            s=''
            for bedrijf , symbool in info.items():
                if inp.upper().rstrip() == bedrijf.upper().rstrip():
                    s = ('Ticker symbol: ' + str(symbool) + '\n')
                    break
                elif inp.upper().rstrip() == symbool.upper().rstrip():
                    s = ('Company name: '+ str(bedrijf))
                    break
                else:
                    s = ('Input not found! ' )
            return s

        inp = input('Enter Company Name: ')
        print(getInfo(inp))
        inpp = input('Enter Ticker Symbol: ')
        print(getInfo(inpp))
        break