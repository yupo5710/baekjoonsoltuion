N,X = map(int,input().split())
A = list(map(int,input().split()))
for i in range(N):
    if X > A[i]:
        print(A[i],end = ' ') 
# A[i] 뒤에 end를 붙이면 출력이 줄마다 출력되지 않고 같이 출력됨 = ' '은 공백