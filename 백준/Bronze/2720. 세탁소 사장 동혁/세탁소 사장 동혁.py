
T = int(input())
k1 = 0
k2 = 0
k3 = 0
k4 = 0
p1 = 0
p2 = 0
p3 = 9
for i in range(T):
    arr = [0,0,0,0]
    n = int(input())

    k1 = n//25 #몫
    arr[0] += k1
    p1 = n % 25

    k2 = (p1)//10 
    arr[1] += k2
    p2 = p1 % 10

    k3 = (p2)//5 
    arr[2] += k3
    p3 = p2 % 5

    k4 = (p3) // 1
    arr[3] += k4
    
    for k in arr:
        print(k,end=' ')