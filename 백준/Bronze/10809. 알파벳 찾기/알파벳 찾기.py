a = input()
alpha = list(range(97,123)) #아스키 숫자 코드 범위
for b in alpha:
    print(a.find(chr(b))) #chr 아스키코드 숫자 문자열 변환
                          #반대는 ord함수