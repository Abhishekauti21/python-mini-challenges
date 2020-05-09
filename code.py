# --------------
#Code starts here
def palindrome_check(num):
  num=str(num)
  return (num[::-1]==num)

#Function to find the smallest palindrome
def palindrome(num):
    while(1):
        num=num+1
        if palindrome_check(num):
            return num


# --------------
#Code starts here
def a_scramble(str_1,str_2):
    result=True
    for i in (str_2.lower()):
        if i not in (str_1.lower()):
            result=False
            break
        str_1=str_1.replace(i,'',1) #Removing the letters from str_1 that are already checked
    
    return (result)


# --------------
#Code starts here
from math import sqrt
def is_perfect_square(x):
     s = sqrt(x)
     return (int(s)*int(s) == x)

def check_fib(num):
    if is_perfect_square((5*num*num) + 4) or is_perfect_square((5*num*num) - 4): 
        return True
    
    return False


# --------------
#Code starts here
def compress(word):
    word=word.lower()
    mist=[]
    l=0
    while(l<len(word)):
        m=word[l]
        j=0
        while(l<len(word) and word[l]==m):
                 j=j+1
                 l=l+1    

        mist.append(m)
        mist.append(str(j))
    
    return ''.join(mist)


# --------------
#Code starts here
def k_distinct(string,k):
    s_list=(set(string.lower()))
    return len(s_list)>=k


