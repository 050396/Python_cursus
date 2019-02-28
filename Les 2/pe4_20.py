infile = open ('Hardlopers.txt', 'a')
from datetime import datetime
s = datetime.strftime(datetime.now(),'%a %d %b %Y %H %M %S')

name = input('Naam hardloper:')
infile.write(s + ' ' + str(name) + '\n')
