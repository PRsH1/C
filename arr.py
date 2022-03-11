number=int(input())
x=1
y=1
sum=2
number2=1
a=2
s=1
string=""
while(1):
    if number2==number:
        if (sum)%2==0:
            for i in range(1,sum):
                    if s>i:
                        continue
                    else:
                            x=sum
                            y=0
                            x=x-i
                            y=y+i
                            string=(str(x))+"/"+(str(y))
                            break
            break
        else:
            for i in range(1,sum):
                if s>i:
                    continue
                else:
                    y=sum
                    x=0
                    y=y-i
                    x=x+i
                    string=(str(x)+"/"+str(y))
                    break

            break

    else:
        number2=number2+1
        if a<sum:
            a=a+1
            x=x+1
            s=s+1
        elif a==sum:
            a=2
            sum=sum+1
            s=1

print(string)