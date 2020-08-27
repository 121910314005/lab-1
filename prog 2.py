Date:27/08/2020
print("Enter two numbers")
n1=int(input())
n2=int(input())
if n1>n2:
  gre=n1
else:
  gre=n2
while(True):    
 if gre % n1==0 and gre % n2==0 :
   lcm = gre
   break
   gre = gre+1
print("lcm of is",lcm)   

output
Enter two numbers
4
6
12
