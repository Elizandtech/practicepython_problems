## Ask user for string, check if string is a palindrome (i.e. eye) ##
# make into a function...


def check_if_palindrome(string):
    make_same = string.casefold()
    index_value = len(make_same)-1
    
    for char in make_same:
        if len(make_same)<1:
            raise ValueError('Enter key value "" not valid')
        if make_same[-1]=='!' or make_same[-1]=='.' or make_same=='?':
            index_value = index_value-1
            continue

        if make_same[0] != make_same[-1]:
            return 'Not a palindrome'
        

      
        if char ==make_same[index_value]:
            index_value = index_value-1
            
    return "It's a palindrome!"


str_input = input('Type a word or phrase: ')
print(check_if_palindrome(str_input))

