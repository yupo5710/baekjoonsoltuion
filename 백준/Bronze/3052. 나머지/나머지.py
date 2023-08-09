'''
arr = []
for i in range(10):
    a = int(input())
    if a%42 not in arr: #arr리스트에 중복된 값이 없으면 출력
        arr.append(a % 42)
print(len(arr))
'''
arr = []
for i in range(10):
    a = int(input())
    arr.append(a % 42)
print(len(set(arr))) #set():중복된 값 자동으로 제외