#erins lists

orangemojito = ['25ml white rum','25ml tripple sec','orange juice','lime juice','mint','lemonade']
mojito = ['50ml white rum','lime juice','lemon juice','lemonade']
pornstar = ['vanilla_vodka','passionfruit juice','sugar syrup']
oldfashioned = ['whiskey','aromatic bitters','sugar syrup']
whiskeysour = ['whiskey','lemon juice','sugar syrup']

recipe = oldfashioned

for item in recipe :
    print(item )

whiskey = 28
vanilla_vodka = 28
white_rum = 28

def whiskey(recipe,whiskey):
    if 'whiskey' in recipe:
        whiskey -=1
        return whiskey

def vanilla_vodka(recipe,vanilla_vodka):
    if 'vanilla_vodka' in recipe:
        vanilla_vodka -=1
        return vanilla_vodka

whiskey = whiskey(recipe,whiskey)
print(bottle)
    

