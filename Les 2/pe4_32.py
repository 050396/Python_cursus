studenten = {}
while True :
    voornaamStudent = input('Volgende naam: ')
    def namen(nieuwe_student):
        i = 0
        if nieuwe_student == '':
            for item in studenten.items():
                names = list(studenten.keys())
                name = names[i]
                count = studenten[name]
                i+=1
                if int(count) == 1 :
                    print('Er is ' + str(studenten[name]) + ' student met de naam ' + str(name))
                elif int(count) > 1:
                    print('Er zijn ' + str(studenten[name]) + ' studenten met de naam ' + str(name))

        elif nieuwe_student in studenten.keys():
            add= int(studenten[nieuwe_student]) +1
            studenten[nieuwe_student] = add
        elif nieuwe_student not in studenten.keys():
            studenten[nieuwe_student] = 1

    namen(voornaamStudent)