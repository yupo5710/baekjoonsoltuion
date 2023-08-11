arr =['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
a= input()
wait= 0

for j in range(len(a)): #입력된 단어 길이 인식
    for i in arr: #배열안에서 변수 i지정 반복
        if a[j] in i: #만약 i안에 j가 있으면
            wait += arr.index(i)+3 #arr의 지표에서 i가 있는 좌표+3초를 더한다

print(wait)