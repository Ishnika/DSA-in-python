#to check for a palindrome word 
def is_palindrome(s):
    for i in s:
        if(i.isalnum()==True):
            str1=str1+i.lower()
    str2=str1[::-1]
    if(str1==str2):
        return True
    else:
        return False 
s=input("Enter the string:")
print(is_palindrome(s))
