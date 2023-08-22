N = int(input())
house = 1
ret = 1
while N > house:
    house += ret * 6
    ret += 1
print(ret)