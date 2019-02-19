Afstand = float (input('Afstand in kilometers:'))
Leeftijd = int(input('Wat is uw leeftijd?'))
Weekendrit = bool(input('Reist u in het weekend? (Ja=True/Nee=False):'))

def standaardprijs (afstandKM):
    if afstandKM > 50:
        tarief = 15 + (0,60 * afstandKM)
    if afstandKM <= 0:
        tarief = 0
    else:
        tarief = 0,80 * Afstand
    return tarief

def ritprijs(Leeftijd, Weekendrit, afstandKM):
    if Weekendrit == False and 65 <= Leeftijd < 12:
        tarief = float(standaardprijs(afstandKM) * 0.70)
    if Weekendrit == True and 65 <= Leeftijd < 12:
        tarief = float(standaardprijs(afstandKM) * 0.65)
    if Weekendrit == True and 65 > Leeftijd >= 12:
        tarief = float(standaardprijs(afstandKM) * 0.60)
    if Weekendrit == False and 65 > Leeftijd >= 12:
        tarief = float(standaardprijs(afstandKM))
    return float(tarief)
print('Uw treinrit kost: €' + str(float(ritprijs('Leeftijd', 'Weekendrit', 'Afstand'))))