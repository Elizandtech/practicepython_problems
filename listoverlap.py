# Write a program that returns a list with only the common elements shared between the two lists; lists are different sizes.
# Generate list random list

import random 
# How can we write a for loop in one line that generates elements and puts it into a list, any list. 
## Instead of append how can I put make the program function in a single line of code within brackets?? Move append to same line as for loop.
# How can we put results into a list

list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
rand_list_1= [random.randint(1,random.randint(120,1000)) for integer in range(random.randint(1,50))]  #generate a list of random numbers
rand_list_2= [random.randint(1,random.randint(200,1000)) for integer in range(random.randint(100, 2000))]


## Substitute list comprehension in the function in the print statement:  print(shared_elements_in_two_lists(rand_list_1,rand_list_2))
print([element for element in set(list1 + list2) if element in list1 and element in list2])
print([element for element in set(rand_list_1 + rand_list_2) if element in rand_list_1 and element in rand_list_2])





# One line for loop:
def generate_random_list(length, value): 
    return [random.randint(1,value) for integer in range(length)]       # list comprehension

def shared_elements_in_two_lists(first, second):
    return [element for element in set(first+second) if element in first and element in second]     # list comprehension with conditionals

#def generate_random_list(length, value):    # Compress code into one line. 
 #   number = list()
  #  for num in range(length):
   #     integer = random.randint(1,value)
    #    number.append(integer)
  #  return(number)


#def shared_elements_in_two_lists(first, second):
 #   number = list()
  #  for element in set(first+second):                           # set() deletes duplicate elements, creates a unique "set" of values.
   #     if element in first and element in second:         # check for common elements
    #        number.append(element)                         # add element that is common
    #return(number)

## Make lists:
list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
#rand_list_1= [random.randint(1,random.randint(120,1000)) for integer in range(random.randint(1,50))]  #generate a list of random numbers
#print(rand_list_1)
#rand_list_2= [random.randint(1,random.randint(200,1000)) for integer in range(random.randint(100, 2000))]
#print(rand_list_2)
#print(shared_elements_in_two_lists(list_1, list_2))




## Code without combining lists...very inefficient!
#if len(list_1) <= len(list_2):
 #   for element in list_2:
 #       if element in list_1 and element not in number:
 #           number.append(element)
  #  print(number)

#else:
   # if len(list_1) >= len(list_2):
  #      for element in list_1:
        #    if element in list_2 and element not in number:
  #              number.append(element)
    #    print(number)

# Make code more efficient:

