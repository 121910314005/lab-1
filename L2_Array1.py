a1 = [1,2,3,4,5];
a2 = [None] * len(a1);
for i in range(0, len(a1)):
 a2[i] = a1[i];

print("Elements of original array: ")
for i in range(0, len(a1)):
  print(a1[i])

print();

print("Elements of new array: ")
for i in range(0,len(a2)):
  print(a2[i])

output:
Elements of original array: 
1
2
3
4
5
Elements of new array: 
1
2
3
4
5
