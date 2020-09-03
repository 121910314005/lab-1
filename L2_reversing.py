a1 = [1,2,3,4,5];
a2 = [None] * len(a1)
length = len(a1)
for i in range(0,length):
  a2[i] = a1[length-i-1]
print("Elements of original array: ")  
for i in range(0, len(a1)):
 print(a1[i])
print("Elements of new array: " )
for i in range(0, len(a2)):
 print(a2[i])
 
 
 OutPut:
 Elements of original array: 
1
2
3
4
5
Elements of new array: 
5
4
3
2
1
   
