arr = [2,3,5]
for i in range(15):
    num = (arr[i+2] - 1) + arr[i+2]
    arr.append(num)
n = int(input())
T = arr[n] ** 2
print(T)  