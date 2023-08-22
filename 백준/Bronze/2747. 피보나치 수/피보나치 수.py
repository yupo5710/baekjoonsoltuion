arr = [0,1]
T = int(input())
num = 0
for i in range(T):
    num = arr[i] + arr[i+1]
    arr.append(num)
print(arr[T])
