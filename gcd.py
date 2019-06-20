def computegcd(a,b):
    if b==0:
        return a
    else:
        return computegcd(b,a%b)

num1=int(input('Enter the first value'))
num2=int(input('Enter the second value'))
print(computegcd(num1,num2))
