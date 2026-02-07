#to count the number of consonents in a string
def count_consonants(s):
    """
    Function to count the number of consonants in the input string.
    
    Parameters:
    s (str): The input string to check for consonants.
    
    Returns:
    int: The count of consonants in the input string.
    """
    count =0
    for i in s :
        if i.isalpha():
            if(i not in ['a','e','i','o','u','A','E','I','O','U']):
                count+=1
            else:
                continue
    return count
s=input("Enter the string:")
print(count_consonants(s))
