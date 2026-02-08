#check if two strings are anagram or not 
def is_anagram(s, t):
    str1=""
    str2=""
    for i in s:
        if(i==" "):
            continue 
        else:
            str1+=i
    for i in t:
        if(i==" "):
            continue 
        else:
            str2+=i
    if len(str1)==len(str2):
        lst1=list(str1)
        lst2=list(str2)
        lst1.sort()
        lst2.sort()
        if lst1==lst2 :
            return True 
        else:
            return False    
    else:
        return False 
s=input("Enter the 1st string:")
t=input("Enter the 2nd string:")
print(is_anagram(s, t))
