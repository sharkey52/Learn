orangemojito = {'white rum':'25ml','tripple sec':'25ml','orange juice':'a little bit','lime juice':'a little bit','mint':'a little bit','lemonade':'some'}
mojito = {'white rum':'50ml','lime juice':'a little bit','lemon juice':'a little bit','lemonade':'a little bit'}
pornstar = {'vanilla_vodka':'50ml','passionfruit juice':'a little bit','sugar syrup':'a little bit'}
oldfashioned = {'whiskey','aromatic bitters','sugar syrup'}
whiskeysour = {'whiskey':'50ml','lemon juice':'a little bit','sugar syrup':'a little bit'}

bottles = {'whiskey':28,
        'vanilla vodka':28,
        'white rum':28,
        'tripplesec':28,
        'another drink':28}

recipe = whiskeysour

def checkbottles(bottles,recipe):
    for item in recipe:
        if item in bottles:
            bottles[item] = bottles[item] - 1
            
    return bottles

def printrecipe(recipe):
    print('You will need...:')
    for item in recipe:
        print(recipe[item] + ' of ' + item)


printrecipe(recipe)
bottles = checkbottles(bottles,recipe)

print(bottles)
