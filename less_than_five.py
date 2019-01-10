list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
import random
random_list1 = [random.randint(1, random.randint(10,1500)) for integer in range(random.randint(10, 100))]

# 4) Ask the user for a number and return a list that contains only elements from the original list that are smaller than that number given by the user.
def return_elements_less_than_given_number(N, lst):
    return [element for element in lst if element <N]

input_number = int(input("Give an integer number: "))
#print(return_elements_less_than_given_number(input_number, list1))
print(return_elements_less_than_given_number(input_number, random_list1))

# 3) Write this in one line of Python. - list comprehension
#print([element for element in list1 if element <5])

# 2) Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
#new_list = []
#for element in list1:
   # if element < 5:
       # new_list.append(element)
#print(new_list)


# 1) Take a list and write a program that prints out all the elements of the list that are less than 5.
#for element in list1:
    #if element < 5:
        #print(element)


