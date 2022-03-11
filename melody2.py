def ascending(n):
    asc = sorted(n)
    return asc


def descending(n):
    r = sorted(n)
    des = list(reversed(r))
    return des


n = list(input("음계:"))
l = len(n)

if (l == 1):
    print("결과:" + "single")

elif (n == ascending(n) and n == descending(n)):
    print("결과:" + "single")

elif n == ascending(n):
    print("결과:" + "ascending")

elif n == descending(n):
    print("결과:" + "descending")

else:
    print("결과:" + "mixed")