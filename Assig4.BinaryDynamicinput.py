def binary(b,s):
    f = 0
    l = len(b)-1
    x = 0
    y = 0
    m = l//2
    if b[m] == s:
        x = 1
        y = m
    elif s<b[m]:
        f = 0
        l = m 
        for i in range(l):
            if b[i] == s :
                x = 1
                y = i
    elif s>b[m]:
        f = m+1
        l = len(b)
        for i in range(l):
            if b[i] == s:
                x = 1
                y = i
    return y,x
a = []
n = int(input("enter size of an array : "))
print("enter "+str(n)+" numbers ")
for i in range(n):
    k = int(input())
    a.append(k)
b = sorted(a)
print(b)
s = int(input("enter a number to search: "))
loc,z = binary(b,s)
if z == 1:
    print(str(s)+" is found at ",loc)
else:
    print(str(s)+" is not found!!!!")
    
OUTPUT:
enter size of an array : 5
enter 5 numbers 
9
4
8
6
0
[0, 4, 6, 8, 9]
enter a number to search: 8
8 is found at  3
    
    
