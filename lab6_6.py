
while True:#무한반복문
    try:#
        num=int(input("숫자를 입력하세요:"))#숫자를 입력받습니다
        if num<1 or num>100:
            raise ValueError

    except ValueError:
        print("1과 100사이의 수를 입력해주세요:")
    else:
        print(num)
        break
    finally:
        print("try-exception")
