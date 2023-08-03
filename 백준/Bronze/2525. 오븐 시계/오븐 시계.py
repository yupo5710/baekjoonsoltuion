'''
a,b = map(int,input().split()) #시간 분
c = int(input()) #오븐 가동 시간
n = 0
if c >= 60:
    a += 1
    n = c - 60
    b += n
    if b >= 60:
       a += 1
       b -= 60
    elif a >= 24:
        a -= 24
elif c < 60:
    b += c
    if b >= 60:
        a += 1
        b -= 60
if a >= 24:
    a -= 24
print(a,b)
#이러면 너무 복잡하고 읽기 짜쯩남,시간도 걸림
'''
a,b = map(int,input().split()) #시간 분
c = int(input()) #오븐 가동 시간

a += c // 60 #오븐가동 시간을 60분으로 나누고 몫
b += c % 60 #오븐 가동 시간을 60분으로 나눈 나머지

if b >= 60:
    a += 1
    b -= 60
if a >= 24:
    a -= 24
print(a,b)