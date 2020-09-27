n1 = int(input("enter a number between 1 to 3 : "))
if n1 == 1:
    a1 = [1,44,5,2,7,88,9,10,11,66,13,14,3]
    b1 = sorted(a1)
    print(b1)
    f1 = 0
    l1 = len(a1)-1
    x1 = 0
    loc1 = 0
    s1 = int(input("enter a number to search: "))
    m1 = l1//2
    if b1[m1] == s1:
        x1 = 1
        loc1 = m1
    elif s1<b1[m1]:
        f1 = 0
        l1 = m1 
        for i in range(l1):
            if b1[i] == s1 :
                x1 = 1
                loc1 = i
    elif s1>b1[m1]:
        f1 = m1+1
        l1 = len(a1)
        for i in range(l1):
            if b1[i] == s1:
                x1 = 1
                loc1 = i
    if x1 == 1:
        print(str(s1)+" is found at ",loc1)
    else:
        print(str(s1)+" is not found!!!!")
elif n1 == 2:
    def binary(b2,s2):
        f2 = 0
        l2 = len(b2)-1
        x2 = 0
        y2 = 0
        m2 = l2//2
        if b2[m2] == s2:
            x2 = 1
            y2 = m2
        elif s2<b2[m2]:
            f2 = 0
            l2 = m2 
            for i in range(l2):
                if b2[i] == s2 :
                    x2 = 1
                    y2 = i
        elif s2>b2[m2]:
            f2 = m2+1
            l2 = len(b2)
            for i in range(l2):
                if b2[i] == s2:
                    x2 = 1
                    y2 = i
        return y2,x2
    a2 = [1,44,5,2,7,88,9,10,11,66,13,14,3]
    b2 = sorted(a2)
    print(b2)
    s2 = int(input("enter a number to search: "))
    loc2,z2 = binary(b2,s2)
    if z2 == 1:
        print(str(s2)+" is found at ",loc2)
    else:
        print(str(s2)+" is not found!!!!")
elif n1 == 3:
    def binary(b3,s3):
        f3 = 0
        l3 = len(b3)-1
        x3 = 0
        y3 = 0
        m3 = l3//2
        if b3[m3] == s3:
            x3 = 1
            y3 = m3
        elif s3<b3[m3]:
            f3 = 0
            l3 = m3 
            for i in range(l3):
                if b3[i] == s3 :
                    x3 = 1
                    y3 = i
        elif s3>b3[m3]:
            f3 = m3+1
            l3 = len(b3)
            for i in range(l3):
                if b3[i] == s3:
                    x3 = 1
                    y3 = i
        return y3,x3
    a3 = []
    n3 = int(input("enter size of an array : "))
    print("enter "+str(n3)+" numbers ")
    for i in range(n3):
        k3 = int(input())
        a3.append(k3)
    b3 = sorted(a3)
    print(b3)
    s3 = int(input("enter a number to search: "))
    loc3,z3 = binary(b3,s3)
    if z3 == 1:
        print(str(s3)+" is found at ",loc3)
    else:
        print(str(s3)+" is not found!!!!")
else:
    print("error!!! enter a number between 1 to 3")

OUTPUT:
enter a number between 1 to 3 : 1
[1, 2, 3, 5, 7, 9, 10, 11, 13, 14, 44, 66, 88]
enter a number to search: 14
14 is found at  9
