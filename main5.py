# Problem Solving

#Last notes for worksheet 

# Do you need to remember or track any values as you solve it? (create a new variable)
# Do you choose to do one action or another based on different situations? (if/else statement with comparisons)
# Do you repeat an action or assessment on each item/letter/number in a pre-defined collection? (for loop)
# Do you want something to continue happening until a certain point is reached? (while loop)

# # Problems to solve

# 1.	Write a function that takes in a string of “Packers” and takes the first and last character of the string, concatenates them together to form a new string variable, then print that string to the console
# a.	Expected outcome: “Ps”




# #create a function
# name = 'Packers'# print(f'{name[0] + name[6]}')  

# variable = str

# def printFirstLast(name):
#         x = print(f'{name[0] + name[6]}')
#         return x 
# #     #We can name the variable type so that it is constant 
# #     #When we call the function  
# printFirstLast('Packers')
# #take in a string
# #take the first and last charachter of the string
# #concatenate the characters   

# # 2.	Peanut Butter Jelly

# #define the range of numbers 
# range1 = range(0,101,1)

# def num_printer(range1):#a.
#     for num in range(0,101,1): 
#         if num % 15 == 0: 
#             print('peanut butter jelly') #d. Had to list first, is this because???? If a number is divisible by 3 and 5, print ‘peanut butter jelly’ instead of the number
#             continue       
#         elif num % 5 == 0: 
#             print('jelly') #c. If a number is divisible by 5, print ‘jelly’ instead of the number
#             continue       
#         elif num % 3 == 0: 
#             print('peanut butter') #b. If a number is divisible by 3, print 'peanut butter’ instead of the number
#             continue #a.	Write a function that prints every number from 0 to 100 to the console

# num_printer(range1)

#We can also create a function and define the variable as a number then introduce the range inside the function
# def dif_printer(new_number):
#     new_number = range(0,101)
#     for x in new_number:
#         print(x)
# new1 = 1
# dif_printer(new1)
# # Use for statement to define variable we are printing to console
# For loop for the initial print to console.
#We will be working with int data type
#We need to define the range of the number set

# 3. Write a function that takes in a single parameter called “word”. This parameter will be a string.

# word = "W,o,r,l,d P,e,a,c,e"

# def singleparam(word):
#     final_result = []
#     for x in word:
#         if "W" in x:
#             final_result.append(x)
#             continue 
#         elif "o" in x: 
#             final_result.append(x)
#             continue
#         elif "r" in x: 
#             final_result.append(x)
#         elif "l" in x: 
#             final_result.append(x)
#             continue 
#         elif "d" in x: 
#             final_result.append(x)
#             continue
#         elif "P" in x: 
#             final_result.append(x)
#             continue
#         elif "e" in x: 
#             final_result.append(x)
#             continue
#         elif "a" in x: 
#             final_result.append(x)
#             continue
#         elif "c" in x: 
#             final_result.append(x)
#             continue    
#         elif "e" in x: 
#             final_result.append(x)
#     else:
#         print(final_result)

# word = "Peace"

# def singleparam(word):
#     final_result = str('')
#     for x in word:
#         if "P" in x: 
#             final_result.append(x)
#             final_result.append(1)
#             continue
#         elif "e" in x: 
#             final_result.append(x)
#             final_result.append(2)
#             continue
#         elif "a" in x: 
#             final_result.append(x)
#             final_result.append(3)
#             continue
#         elif "c" in x: 
#             final_result.append(x)
#             final_result.append(4)
#             continue    
#         elif "e" in x: 
#             final_result.append(x)
#             final_result.append(5)
#     else:
#         print(final_result)




#  def singleParam(word):
#     final_result = 1j
#     for x in word:
#         if 'R' in x:
#             final_result.append[x]
#             final_result.append(0)
#             continue
#         elif 'o' in word:
#             final_result.append(x)
#             final_result.append(1)
#             continue
#         elif 'g' in word:
#             final_result.append(x)
#             final_result.append(2)
#             continue
#         elif 'e' in word:
#             final_result.append(x)
#             final_result.append(3)
#             continue
#         elif 'r' in word:
#             final_result.append(x)
#             final_result.append(4)
#             continue 
#         elif 'T' in word:
#             final_result.append(x)
#             final_result.append(5)
#             continue       
#         elif 'h' in word:
#             final_result.append(x)
#             final_result.append(5)
#             continue   
#         elif 'a' in word:
#             final_result.append(x)
#             final_result.append(7)
#         elif 'd' in word:
#             final_result.append(x)
#             final_result.append(8)
#     else:
#             final_result.append(x)
#             final_result.append(9)
#             print(final_result) 

# word = 'Roger Thad'

# singleParam(word)

# singleparam(word)
# singleparam(word)
# I will come back to the one above
# Maybe we try following instruction and using .append(in a wiser way)
#       
# a.	Inside the function, create a variable called “final_result” and set it equal to an empty string.
# b.	Loop over the letters in the word and append the letter and its index to the final_result variable.
# c.	Print to the terminal the final_result variable.
# d.	Example Input: “World Peace” 
# e.	Example Output: “W0o1r2l3d4 5P6e7a8c9e10”
# word = ["Tonight Tonight"]


# final_result = ['']
# for letters in word:
#     if 'T' in letters:
#         final_result.append[0]
#         print(final_result)
#     else:

# 4.	Write a function that takes in a single parameter called “ingredients”. This parameter will be a List.
# a.	Inside of the function, take user input that asks if the user knows what ingredient they want to search for
# b.	Check the List parameter and see if the user’s input is an element in the List.
# i.	If the ingredient is present, return the string ingredient from the function
# ii.	If the ingredient is not there, ask the user if they want to search again and restart the operation

#write function def

# ingredients = []

# def ingredFunction(ingredients):
#     user_choice = input('Do you know what ingredient you need?    ')
#     if user_choice in ingredients:
#         return ingredients
#     else: 
#         print(f'We dont have that.')
#     user_check = input('Wpuld you like to choose again?  ')
#     if user_choice in ingredients:
#         return ingredients
#     else:
#         print('Thank you')

# ingredients = ['cheese','ketchup','potato']

# ingredFunction(ingredients)



# 5.	Write a function that takes in a list of strings, the logic of the function should reverse the order of the values inside the list then return it back as a new list
# a.	Note: Cannot use list.reverse() for this problem
# i.	Input: [“Yellow”, “Purple”, “Orange”]
# ii.	Output: [“Orange”, “Purple”, “Yellow”]

# strings1 = ['Yellow', 'Purple', 'Orange']

# def myfunction(string1):
#     x,y,z = string1
#     string1 = [x,y,z]
#     print(f'{([z,y,x])}')
#     return string1

# strings1 = ['Yellow', 'Purple', 'Orange']

# myfunction(strings1)    

# 6.	Write a function that takes in a single parameter called ‘names’. 
# a.	When you call the function, pass in a list containing 6 different names. 
# b.	The function should create and return a new list filled with any name from the ‘names’ parameter that contains more than 4 characters.
# c.	Ex Input: [‘Rebecca’, ‘Sam’, ‘Bob’, ‘Dante’, ‘Monica’, ‘Brad’]
# d.	Ex Output: [‘Rebecca’, ‘Dante’, ‘Monica’]


# def namelistfunction(names):
#     list_ofnames = []
#     x = int
#     y = str 
#     for y in names:
#         list_ofnames.append(0)
#         list_ofnames.append(1)
#         list_ofnames.append(2)
#         list_ofnames.append(3)
#         list_ofnames.append(4)
#         list_ofnames.append(5)
#         print(list_ofnames)
#     else:
#         if y in names(6):
#             print(list_ofnames)
#             print(names)
#         return list_ofnames 
    
# names = ['Rebecca', 's', 'Bob', 'Dante', 'Monica', 'Brad']
# namelistfunction(names)
