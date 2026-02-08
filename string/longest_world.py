#return the length of the longest word of the string
def longest_word_length(s):
    lst=s.split()
    max_len=0
    for i in lst :
        if(len(i)>max_len):
            max_len=len(i)
        else :
            continue
    return max_len
s=input("Enter the string:")
print(longest_word_length(s))
