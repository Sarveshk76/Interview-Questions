str1 = "anaa"

def isPalindrome1(str1):
    rev = str1[::-1]
    if str1 == rev:
        print('Palindrome')
    else:
        print('Not a Palindrome')
isPalindrome1(str1)

def isPalindrome2(str1):
    rev = ''.join(reversed(str1))
    if str1 == rev:
        print('Palindrome')
    else:
        print('Not a Palindrome')
isPalindrome2(str1)
