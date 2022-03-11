while(1):
    number1=[]
    number2=(input("숫자를 입력하세요:"))
    for x in range(0,len(number2)):
        number1.append(number2[x])
    if number2=='0':
        break
    else:
        print("역:",number2[::-1])
        sum=0
        for i in number2:

            sum+=int(i)
        print("합계:",sum)



