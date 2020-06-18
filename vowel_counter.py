#This will count the number of vowels in a string

def vcount():

    userstring = input("Type your sentence here: ").lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = 0

    for letter in userstring:
        
        if letter in vowels:

            result += 1
    
    print('\nThere are ' + str(result) + ' vowels in your sentence!')

vcount()