#program that prints the number of characters in a user's name.
#len() is used to get the number of characters in a string
n = input("What is your name? ")
print(len(n)) #Don't use quotqtion marks with print and len()
print("\n")
#another way to get this done is by puting the funtions inside other functions.
print( len( input("What is your name? ") ) )
