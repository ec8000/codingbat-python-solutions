# Return True if the string "cat" and "dog" appear the same number of times in the given string.
#
# cat_dog('catdog') → True
# cat_dog('catcat') → False
# cat_dog('1cat1cadodog') → True

def cat_dog(str):
    countcat = 0
    countdog = 0
    for i in range(len(str)):
        if str[i:i+3] == 'cat':
            countcat += 1
        elif str[i:i+3] == 'dog':
            countdog += 1
    return countcat == countdog        

print(cat_dog('catdog'))
print(cat_dog('catcat')) 
print(cat_dog('1cat1cadodog')) 
