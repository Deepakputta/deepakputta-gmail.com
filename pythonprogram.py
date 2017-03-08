n=int(input("Enter How Many numbers.."))
print("Enter",n,"Numbers")
sumnegv = sumposv = 0
num = []
for i in range(0, n):
    num.append(int(input()))
for i in range(0, n):
    if(num[i] < 0):
        sumnegv+= num[i]
    else:
        sumposv+= num[i]
print("Sum of Positive NUmbers is",sumposv)
print("Sum of Negative NUmbers is",sumnegv)