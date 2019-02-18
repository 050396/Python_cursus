Lengte = input('Hoe lang ben je?')
def lang_genoeg (attractie):
    if int(attractie) >= 120:
        print ('Je mag in de attractie.')
    else:
        print ('Sorry, je bent te klein!')
lang_genoeg (Lengte)