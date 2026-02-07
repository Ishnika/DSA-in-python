#count the number of words in a string 
def count_words(s):
    lst=s.split()
    count=0
    for i in lst:
        if i.isalpha() :
            count+=1
        else:
            continue
    return count
s=input("Enter the string:")
print(count_words(s))
