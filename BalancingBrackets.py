def isBalanced(str1):
    dict1 = {'(':')','[':']','{':'}'}
    stack = []

    for i in str1:
        if i in dict1.keys():
            stack.append(i)
        else:
            if not stack:
                return False

            if dict1[stack.pop()] != i:
                return False

    if stack:
        return False
    return True
str1 = "{[()]}"
if isBalanced(str1):
    print('Balanced')
else:
    print('Not Balanced')
