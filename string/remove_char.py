#remove all the repeating characters from the string but keeping the first occurance of the character in the original string 
def remove_duplicates(s):
    str1=""
    for i in s:
        if(i not in str1):
            str1+=i
    return str1 
s= input("Enter the string:")
print(remove_duplicates(s))
