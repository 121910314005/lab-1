import math
x= int(input('Enter First number:'))
y = int(input('Enter Second number:'))
gcd_ans = math.gcd(x, y)
lcm_ans = x * y/ gcd_ans
print(lcm_ans)
print(gcd_ans)

output
Enter First number:10
Enter Second number:20
20.0
10
