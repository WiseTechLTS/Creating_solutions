# Problem Solving

#Last notes for worksheet 

# Do you need to remember or track any values as you solve it? (create a new variable)
# Do you choose to do one action or another based on different situations? (if/else statement with comparisons)
# Do you repeat an action or assessment on each item/letter/number in a pre-defined collection? (for loop)
# Do you want something to continue happening until a certain point is reached? (while loop)

# # Problems to solve

# 1.	Write a function that takes in a string of “Packers” and takes the first and last character of the string, concatenates them together to form a new string variable, then print that string to the console
# a.	Expected outcome: “Ps”




#create a function
# name = 'Packers'
# print(f'{name[0] + name[6]}')  

# variable = str

# def printFirstLast(variable):
#         x = print(f'{variable[0] + variable[6]}')
#         return x 
#     #We can name the variable type so that it is constant 
#     #When we call the function  
# printFirstLast('Packers')
# #take in a string
# #take the first and last charachter of the string
# #concatenate the characters   

# # 2.	Peanut Butter Jelly

# #define the range of numbers 

# def num_printer(range1):#a.
#     for num in range1: 
#         if num % 15 == 0: 
#             print('peanut butter jelly') #d. Had to list first, is this because???? If a number is divisible by 3 and 5, print ‘peanut butter jelly’ instead of the number
#         elif num % 5 == 0: 
#             print('jelly') #c. If a number is divisible by 5, print ‘jelly’ instead of the number
#         elif num % 3 == 0: 
#             print('peanut butter') #b. If a number is divisible by 3, print 'peanut butter’ instead of the number
#         return num #a.	Write a function that prints every number from 0 to 100 to the console

# range1 = range(100)
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

word = ("World Peace")

def singleparam(word):
    final_result = []
    for x in word:
        if "W0" in x:
            final_result.append(x)
            continue 
        elif "o" in x: 
            final_result.append(x)
            continue
        elif "r" in x: 
            final_result.append(x) 
            continue
        elif "l" in x: 
            final_result.append(x)
            continue 
        elif "d" in x: 
            final_result.append(x)
            continue
        elif "P" in x: 
            final_result.append(x)
            continue
        elif "e" in x: 
            final_result.append(x)
            continue
        elif "a" in x: 
            final_result.append(x)
            continue
        elif "c" in x: 
            final_result.append(x)
            continue    
        elif "e" in x: 
            final_result.append(x)
    else:
        print(final_result)


singleparam(word)

# a.	Inside the function, create a variable called “final_result” and set it equal to an empty string.
# b.	Loop over the letters in the word and append the letter and its index to the final_result variable.
# c.	Print to the terminal the final_result variable.
# d.	Example Input: “World Peace” 
# e.	Example Output: “W0o1r2l3d4 5P6e7a8c9e10”
