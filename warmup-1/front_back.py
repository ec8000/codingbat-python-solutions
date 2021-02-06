# Given a string, return a new string where the first and last chars have been exchanged.
#
# front_back('code') → 'eodc'
# front_back('a') → 'a'
# front_back('ab') → 'ba'

def front_back(str):
    front = str[0]
    back = str[-1]
    mid = str[1:-1]
    if len(str) < 2:
        return str
    return back + mid + front

print(front_back('code'))
print(front_back('a'))
print(front_back('ab'))
