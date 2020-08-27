n1=int(input("Enter the first number:"))
n2=int(input("Enter the second number:"))
n3=int(input("Enter the third number:"))

if(n1<=n2 and n1<=n3):
 print(n1,"is the smallest")
elif(n2<=n1 and n2<=n3):
 print(n2,"is the smallest")
else:
 print(n3,"is the smallest")
 
output: 
 Enter the first number:5
Enter the second number:6
Enter the third number:7
5 is the smallest
