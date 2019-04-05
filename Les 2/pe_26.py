studentencijfers = [[95, 82, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0]]

def gemiddelde_per_student(studentencijfers):
    list = []
    for item in studentencijfers:
        gemcijfer = sum(item) / len(item)
        list.append(gemcijfer)
    return list

def gemiddelde_van_alle_studenten(studentencijfers):
    gem_alle_studenten = gemiddelde_per_student(studentencijfers)
    gem_aantal = sum(gem_alle_studenten) / len(gem_alle_studenten)
    return gem_aantal

print(gemiddelde_per_student(studentencijfers))

print(gemiddelde_van_alle_studenten(studentencijfers))