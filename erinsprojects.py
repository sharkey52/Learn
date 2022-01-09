# erins projects

#create a program that works through people in a dictionary to see who you can pump 

myage = 23

#dictionary
mydict = {'erin':20,'archie':2,'aunie':42}

#create a function that works out the minim age person can smash
def sexytime(age):
    good = age/2
    good+8
    return age

#use a for loop to work though people in the dictionary
for person in mydict:
    age = sexytime (mydict[person])


    #use an if statement to report wether each person can smash or not
    if age < myage:
        print ('get them clothes off')
    else:
        print ('pedo alert!')




