str1 = 'silent'
str2 = 'listen'
def isAnagram1(str1,str2):
    if sorted(str1) == sorted(str2):
        print('Anagram')
    else:
        print('Not Anagram')
isAnagram1(str1,str2)

def isAnagram2(str1,str2):
    cnt=0
    for i in str1:
        for j in str2:
            if i==j:
                cnt+=1
    if len(str1) == cnt:
        print('Anagrams')
    else:
        print('Not anagrams')
isAnagram2(str1,str2)