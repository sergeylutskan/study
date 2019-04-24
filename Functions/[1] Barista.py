# If we have a needed ingredients, we make a coffee from Preferences.
# If coffee in Preferences is in start of list, it have a more priority. 

def choose_coffee(preferences):
    global ingridients
    coffee = {'Эспрессо': [1,0,0],
              'Капучино':[1,3,0],
              'Маккиато':[2,1,0],
              'Кофе по-венски':[1,0,2],
              'Латте Маккиато':[1,2,1],
              'Кон Панна':[1,0,1]
              }
    k = False
    for pref in preferences:
        if (ingredients[0] - coffee[pref][0] >= 0) and (ingredients[1] - coffee[pref][1] >= 0) and (ingredients[2] - coffee[pref][2] >= 0):
            ingredients[0] = ingredients[0] - coffee[pref][0]
            ingredients[1] = ingredients[1] - coffee[pref][1]
            ingredients[2] = ingredients[2] - coffee[pref][2]                                            
            k = True
            return pref
            break
    if k == False:
        return 'К сожалению, не можем предложить Вам напиток'

ingredients = [1, 2, 3]
print(choose_coffee("Эспрессо, Капучино, Маккиато, Кофе по-венски, Латте Маккиато, Кон Панна".split(", ")))
print(choose_coffee("Эспрессо, Капучино, Маккиато, Кофе по-венски, Латте Маккиато, Кон Панна".split(", ")))
