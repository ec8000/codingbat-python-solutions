# Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3.
# Return n copies of the front;
#
# front_times('Chocolate', 2) 
# front_times('Chocolate', 3) 
# front_times('Abc', 3) 

def front_times(str, n):
    result = ''
    for i in range(n):
        result += str[:3]
    return result

print(front_times('Chocolate', 2))
print(front_times('Chocolate', 3))
print(front_times('Abc', 3))
