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
a = [1,4,5,2,7,8,9,10,11,6,3]
b = sorted(a)
print(b)
s = int(input("enter a number to search: "))
loc,z = binary(b,s)
if z == 1:
    print(str(s)+" is found at ",loc)
else:
    print(str(s)+" is not found!!!!")
    
OUTPUT:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
enter a number to search: 11
11 is found at  10
    
