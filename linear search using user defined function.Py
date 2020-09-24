def linear_search(a,n):
    
    for i in range(len(a)):
        if a[i] == n:
            x = 1
            h = i
    return x,h
        
a = []
m = int(input("enter size of an array : "))
print("enter "+str(m)+" numbers ")
for i in range(m):
    k = int(input())
    a.append(k)
x = 0
n = int(input("enter a number to search : "))
l,loc = linear_search(a,n)
if l == 1:
    print(str(n)+" is found at ",loc)
else:
    print(str(n)+" is not found!!!!")
    
    Output:
enter size of an array : 3
enter 3 numbers 
5
6
7
enter a number to search : 7
7 is found at  2
