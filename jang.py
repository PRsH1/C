n1=int(input())
n2=int(input())
result=0
for i in range(1,n1+1):
    if(i%n2==0):
        result+=1

print(result)