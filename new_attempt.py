# 1.	Write a function that takes in a string of “Packers” and takes the first and last character of the string, concatenates them together to form a new string variable, then print that string to the console
# a.	Expected outcome: “Ps”

# Write a funtion

# word = list("Packers")

# def function_1(word):
#     print(word[0] + word[6])

# function_1(word)

# 2.	Peanut Butter Jelly
# a.	Write a function that prints every number from 0 to 100 to the console
# b.	If a number is divisible by 3, print 'peanut butter’ instead of the number
# c.	If a number is divisible by 5, print ‘jelly’ instead of the number
# d.	If a number is divisible by 3 and 5, print ‘peanut butter jelly’ instead of the number

# def print_pbj():
#     for i in range(1,100):
#         if int(i)%15 ==0:
#             print('peanutbutter jelly')
#         elif int(i)%5 ==0:
#             print('jelly')
#         elif int(i)%3==0:
#             print('peanut butter')
#         else:
#             print(i)

# print_pbj()

# for num in range(0,101,5):
#     print('jelly')
# if num % 15  in range(101):
# # print("peanut butter jelly")
# test



# 3.	Write a function that takes in a single parameter called “word”. This parameter will be a string.
# a.	Inside the function, create a variable called “final_result” and set it equal to an empty string.
# b.	Loop over the letters in the word and append the letter and its index to the final_result variable.
# c.	Print to the terminal the final_result variable.
# d.	Example Input: “World Peace” 
# e.	Example Output: “W0o1r2l3d4 5P6e7a8c9e10”


# word = "word"

# def intake(word):
        #create final_result and set equall to string.
#     final_result = ""
        #create for loop to loop through characters in word.
#     for char in word
#         final_list = []
        # create list to store updated values in. 
#         if 'w' in char:
        # for each character in word append final.list and final.result. 
#             final_list.append(0)
#             final_list.append(char)
#             final_result=final_list
#         elif 'o'  in char:
#             final_list.append(1)
#             final_list.append(char)
#             final_result+=final_list
#         elif 'r' in char:
#             final_list.append(2)
#             final_list.append(char)
#             final_result+=final_list
#         elif 'd' in char:
#             final_list.append(3)
#             final_list.append(char)
#             final_result+=final_list           
#             print(final_result[0:8])
#             print(f'{final_result[0]}{final_result[1]}{final_result[2]}{final_result[3]}{final_result[4]}{final_result[5]}{final_result[6]}{final_result[7]}')
            

# intake(word)

# 4.	Write a function that takes in a single parameter called “ingredients”. This parameter will be a List.
# a.	Inside of the function, take user input that asks if the user knows what ingredient they want to search for
# b.	Check the List parameter and see if the user’s input is an element in the List.
# i.	If the ingredient is present, return the string ingredient from the function
# ii.	If the ingredient is not there, ask the user if they want to search again and restart the operation

# 5.	Write a function that takes in a list of strings, the logic of the function should reverse the order of the values inside the list then return it back as a new list
# a.	Note: Cannot use list.reverse() for this problem
# i.	Input: [“Yellow”, “Purple”, “Orange”]
# ii.	Output: [“Orange”, “Purple”, “Yellow”]



listrings = ['Yellow','Purple','Orange']

def my_function(liststrings):
  for element in listrings:
    listrings.append(0)
    listrings.append(1)
    listrings.append(2)
    new_string=liststrings
    print(f'{[new_string[2],new_string[1],new_string[0]]}')
    return

my_function(listrings)