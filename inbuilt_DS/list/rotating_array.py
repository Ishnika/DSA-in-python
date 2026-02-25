#Rotating an array by the number of times specified 
def rotate_left(ARR, D):
    D=D%len(ARR)
    lst1=ARR[0:D]
    lst2=ARR[D:len(ARR)]
    lst=lst2+lst1
    return lst
ARR=eval(input("Enter the Array:"))
D=int(input("Enter the number of times to be rotated:"))
print(rotate_left(ARR, D))
