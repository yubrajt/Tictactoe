def linearsearch(array,n,x):
     for i in range(0,n):
         if(array[i]==x):
             return i
     return -1


array = [2,4,0,1,9,1,2,4,4,4,4,4,5,4,4]
x=4
n= len(array)
result = linearsearch(array,n,x)
if(result == -1):
    print("element not found")
else:
    print("Element found at index:",result)
