#count the number of vowels
def count_vowels(s):
    count=0
    for i in s:
        if(i in ['a','e','i','o','u','A','E','I','O','U']):
            count+=1
    return count
s=input("Enter the string:")
print(count_vowels(s))
