Afstand = float (input('Afstand in kilometers:'))
Leeftijd = int(input('Wat is uw leeftijd?'))
Weekendrit = (input('Reist u in het weekend? (Ja=True/Nee=False):'))
Wkdrit = 0
if Weekendrit == 'Ja':
    Wkdrit = True
if Weekendrit == 'Nee':
    Wkdrit = False

def standaardprijs (afstandKM):
    if afstandKM > 50:
        tarief = 15 + (0.60 * afstandKM)
    if afstandKM <= 0:
        tarief = 0
    else:
        tarief = 0.80 * Afstand
    return tarief

def ritprijs(Leeftijd, Weekendrit, afstandKM):
    if not Weekendrit and (Leeftijd >= 65 or Leeftijd < 12):
        tarief = standaardprijs(afstandKM) * 0.70
    if Weekendrit and (Leeftijd >= 65 or Leeftijd < 12):
        tarief = standaardprijs(afstandKM) * 0.65
    if Weekendrit and (Leeftijd < 65 or Leeftijd >= 12):
        tarief = standaardprijs(afstandKM) * 0.60
    if not Weekendrit and (Leeftijd < 65 or Leeftijd >= 12):
        tarief = standaardprijs(afstandKM)
    return tarief
print('Uw treinrit kost: €{:0.2f}' .format(round(ritprijs(Leeftijd, Wkdrit, Afstand),2)))