
num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))

if len(num2) < len(num1):
    temp = num1
    num1 = num2
    num2 = temp

num3 = []

for i in range(len(num1)):
    num3.append(num1[i])
    num3.append(num2[i])

for j in range(len(num1),len(num2)):
    num3.append(num2[j])

print (num3) 
