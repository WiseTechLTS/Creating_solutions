# OOP  
# Objects ^ have - properties and methods
# Has and CAN DO 
# CLASS is a template of an object
# Blueprint has what it can do and what it has
# Object is the actual thing built from the blueprint
# An object is a new type of variable but they can be used the same way# 
# unlimited objects around one classa class does not become and object until it is instantiated 
# 
# Class defined properties (has) can do (methods)# The map is not the state (instantiated)
# 
# Objects hold the state of the object and methods that could be called by the object to perform tasks
# S E L F  parameter is a reference to 'THIS' instance, It is how variables that belong to the class are accessed. Line 16
# CLASS AND OBJECT EXAMPLE 
class Player: # CLASS !!!!INSIDE PLAYER.py!!!!! file:
    def __init__(self):##\\\\\ This is the first function that runs in new instance line 29
        self.name = '' # strings  _ ALL
        self.cards = [] # Lists   | P R O P E R T I E S               ---------Instantiated properties every 'Type Object has'
        self.cash = 0 # integers  _ HAS A relationship to Object
## METHODS (We can create as many methods as we want for our class just like PROPERTIES see line 18
def set_name(self):                         # M E T H O D 
    self.name = input('Enter Player name:') # M E T H O D S that CAN DO for the Object and Class 
    print('Player name: ', self.name)       # --------------- --Creating a function that CAN DO
# The function is the first thing that runs when an instance of the class is created 
# 
# Inside !!!!!!!!---MAIN.py---!!!! file:
from player import Player 
# Once you import the Class aka blueprint file///
class PlayerZero:
    self.area = ''
    self.playerZer []
    self.integer = 0

def player__Zero(self):## M E T H O D S   L I N K E D  T O  I N S T A N C E S  MUST  ALSO HAVE SELF
    self.playerZer = ['list,','of', 'object', 'or', 'tools', 'names', 'etc', 'rock','paper','scissors','FIGHT','NAME']
    for char in self.playerZer: ###
    while len(self.playerZer) == True### 
    if x in self.playerZer:###""############### W H E N  Y O U  A R E  C R E A T I N G  METHODS you can loop through HAS A
        elif y in self.playerZer:###
    else:### 
        self.playerZer == False###
player_one = PLayer() 
# These become OBJECTS made from the CLASS 
player_two = Player
player_two.set_name()
# OBJECTS MADE FROM CLASS MADE FROM HAS AND CAN DO's 
#
# 
# 
#   CLASS      &     OBJECT    EXAMPLE    EXPANDED     
# 
#  !!!!!!!!  INSIDE YOUR PLAYER.py FILE  MEANING YOUR CLASS FILE (ALREADY MADE BLUEPRINT)
# 
class Player:
    def __init__(self, name, buy=in):#######   WE HAVE JUST THE ------I N I T I A L I Z E R ---__init___ CAN INCLUDE PARAMETERS
        self.name = name### THIS IS A HAS A  VARIABLE
        self.cards = []#############  THIS IS A LIST THAT COULD POTENTIALLY HAVE VARIABLES AND STRINGS
        self.cash = buy_in###   THIS IS A FUNCTION PARAMETER THAT COULD HAVE LOOPING QUALITIES 
def wager(self):###
    self.cash -= 10###
# -------------------------- W E    NOW    C A N   !!!  P A S S   OUTSIDE    I N F O   INTO  OUR OBJECT !!!
# ------- WHEN !!!! --- I N S T A N T I A T I N G ---- AN  O B J E C T  WE  C A L L  THE  CLASSES  __init__ function to run (
# (similar to calling other functions)
#
#   You must pass in an A R G U M E N T to fufill its parameters
# !!!!!!!!!!!!!!!     THE    O N L Y  DIFFERENCE  IS THAT ( selF ) DOES NOT NEED TO BE PASSED IN
#     !!!!!!!!!!   INSIDE YOUR MAIN.py FILE  the object you create becomes the self 
#
# 
from player import Player 

player_one = Player("String", 100)
player_two = Player("Name something", 120)
player_three = Player("Radom name", 300)
#####
# 
# 
# 
#    HARD CODED     VS    PASSED IN 
player_one = Player() ###
player_one.set_name() ###
# 
# ###### H A R D  C O D E D ######
class Player: # CLASS !!!!INSIDE PLAYER.py!!!!! file:
    def __init__(self):##\\\\\ This is the first function that runs in new instance line 29
    self.name = '' # strings  _ ALL
    self.cards = [] # Lists   | P R O P E R T I E S               ---------Instantiated properties every 'Type Object has'
    self.cash = 0 # integers  _ HAS A relationship to Object
# 
def set_name = input("enter Player Name...:  ")
    print("Player name")
#
# 
# D O T  N O T A T I O N  after we     Create an I N S T A N C E  
player_one = Player("String", 300)
player_two = ("String", 200)
player_three = ("String", 450)
#   
print(player_one.name)  #output "String"
player_two.wager() ### A C C E S S I N G  another instance of a C L A S S or creating an O B J E C T  DOT NOTATION
print(player_two.cash)### output 200
print(player_three.cash)### output 300
# #########################P A S S E D   IN############################################## 
class Player:
    def __init__(self, name, buy=in):#######   WE HAVE JUST THE ------I N I T I A L I Z E R ---__init___ CAN INCLUDE PARAMETERS
        self.name = name### THIS IS A HAS A  VARIABLE
        self.cards = []#############  THIS IS A LIST THAT COULD POTENTIALLY HAVE VARIABLES AND STRINGS
        self.cash = buy_in###   THIS IS A FUNCTION PARAMETER THAT COULD HAVE LOOPING QUALITIES 
def wager(self):###
    self.cash -= 10###
##
#
#
# INHERITANCE IS AN   IS  A  RELATIONSHIP
#
class Animal:  ###########    PARENT CLASS    """"""""""""""
    def __init__(self):
        self.name = ""
        self.happiness = 0

    def eat(self):
        self.happiness +=5 #
#

from animal import Animal

class Dog(Animal):###################  CHILD CLASS ########### (PARENT CLASS) ##################
    def __init__(self):
        self.breed = ""
        super().__init__()   ###########  The super() function forces the child class to inherit all 
        #################################  instance variables and methods from the parent class
        # ################################  For the Dog class to inherit its members from the parent
        #  ################################   Animal class, it must utilize the super() function
    def wag_tail(self):#################  
        print(self.happiness) ########## It is possible to add instance variables and methods to the child class that are more unique
        self.happiness += 10 ########### I N H E R I T A N C E    is a one way street   
        print(self.happiness) ########## Dog has access to self.breed and wag_tail() Animal the parent class does not

    def set_name(self):
        self.name = input("Assign dog name ")
        print(self.name)
#############################################################################
from dog import Dog                   ################## 
############################################################################
if __name__ == '__main__':
    dog = Dog()        #
dog.eat()              #  Even though eat() method is defined in Animal class you can call eat() due to  INHERITANCE  see line 114
dog.wag_tail()         #
#
#
#   M E T H O D  Overide
class Meal:
    def __init__(self):
        self.servings = 0
    def prepares(self):
        pass
#          VS           #
class Cereal(Meal):
    def __init__(self):
        super().__init__()

    def prepares(self):
        self.servings = 8
        print("Add cereal and milk")

class Lasagna(Meal):
    def __init__(self):
        super().__init__()

    def prepares(self):
        self.servings = 8
        print("Layer pasta and sauce etc...")

#####################################################
#