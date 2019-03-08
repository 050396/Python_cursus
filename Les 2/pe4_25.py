invoer = '5-9-7-1-7-8-3-2-4-8-7-9'
lst = (invoer.split('-'))
getallenreeks = list(map(int, lst))
getallenreeks.sort()
maxlst = max(getallenreeks)
minlst = min(getallenreeks)
countlst = len(getallenreeks)
sumlst = sum(getallenreeks)
gem = sumlst / countlst

print ('Gesorteerde list van ints:' + str(getallenreeks) + '\n' + 'Grootste getal:' + str(maxlst) + ' en kleinste getal:' + str(minlst) + '\n' + 'Aantal getallen:' + str(countlst) + ' en som van de getallen:' + str(sumlst) + '\n' + 'Gemiddelde:' + str(gem))
