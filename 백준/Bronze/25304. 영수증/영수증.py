total =int(input()) #전체 금액
type = int(input()) #물건 종류
sum = 0 #종류의 개수와 합을 구해야 하기 대문에 0으로 지정

for i in range(type): #물건의 종류만큼 반복
    a,b= map(int,input().split()) #a,b 갯수와 금액을 숫자로 지정,split 띄어쓰기
    sum += a * b #sum += a * b => a * b 반복

if sum == total:
    print('Yes')
else:
    print('No')