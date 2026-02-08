#to check if a string is a sequence from another string 
def is_subsequence(s, t):
    """
    Function to check if t is a subsequence of s.
    
    Parameters:
    s (str): The original string.
    t (str): The target subsequence string.
    
    Returns:
    bool: True if t is a subsequence of s, False otherwise.
    """
    i=0
    j=0
    while i<len(s) and j<len(t) :
        if s[i]==t[j]:
            j+=1
        i+=1
    if j== len(t):
        return True 
    else:
        return False 
s=input("Enter the string:")
t=input("Enter the sequence you want to check :")
print(is_subsequence(s, t))
