# Exercise 1:
# Given a list as a parameter,write a function that returns a list of numbers that are less than ten 
# For example: Say your input parameter to the function is [1,11,14,5,8,9]...Your output should [1,5,8,9]

random_list = [1,11,14,5,8,9]
sorted_list = sorted(random_list)
print(sorted_list)

low_list = [num for num in sorted_list if num < 10]
print(low_list)

#Exercise 2:
#Write a function that takes in two lists and returns the two lists merged together and sorted
#Hint: You can use the .sort() method

list_1 = [1,2,3,4,5,6]
list_2 = [3,4,5,6,7,8,10]
sorted_list = sorted(list_1 + list_2)
print(sorted_list)