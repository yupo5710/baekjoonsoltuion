import sys

arr = []
for i in range(5):  
  a = sys.stdin.readline().rstrip()
  arr.append(a)

for i in range(15): 
  for j in range(5): 
    if i < len(arr[j]):
      print(arr[j][i], end="")