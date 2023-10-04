import CoinClass as c
#import the code from the coinclass.py file (don't need to put .py), can give alias

# The main function.
def main():
       # Create an object from the Coin class.
       my_coin = c.Coin()   # this creates an instance called 'my_coin' of the class 'Coin()'
       #Use class name + ()
        # ^ creating a weapon from the weapon class (creating the gun). Coin() is the blueprint, becomes the object. Only has 1 attribute rn (sideup) and it's heads

       # Display the side of the coin that is facing up.
       print('This side is up:', my_coin.get_sideup())    # notice you do not have to supply the argument/parameter
                                #will say heads bc of line 11 in coinclass.py
                                #my_coin is the object

       # Toss the coin.
       print('I am going to toss the coin ten times:')
       for count in range(10):
           my_coin.toss()
           #simulates a toss

           my_coin.__sideup = 'Heads' #this line is ignored (would make them all heads) b/c the attribute can't be changed with the __ in front of attribute name. Hide all attributes in class file.
           
           # Display the side of the coin that is facing up.
           print('This side is up:', my_coin.get_sideup())
           #every time, print out new value after the flip

           #calling the toss and get_sideup method

           


       

# Call the main function.

main()
