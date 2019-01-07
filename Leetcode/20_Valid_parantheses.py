def isValid(s):
    if len(s) % 2 == 1: return False
    dic = {'(': ')', '{': '}', '[': ']'}
    stack = []
    for char in s:
        if char in dic:
            print(char)
            stack.append(char)
        else:
            if not stack or dic[stack.pop()] != char:
                print('False')
    return not stack


isValid('()[]')