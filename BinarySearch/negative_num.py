#A 2D matrix with dimensions m x n, where each row and each column is sorted in non-increasing order.find -VE num
def countNegatives(grid):
    count =0
    for i in grid:
        for j in range(0,len(i)):
            if i[j]<0:
                index_1=j
                sum=len(i)-index_1
                count+=sum
                break
    return count
grid=eval(input("Enter the matrix(as nested list):"))
print(countNegatives(grid))
