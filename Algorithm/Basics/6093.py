cnt = int(input())
n = input().split()
for i in range(cnt) :
  n[i] = int(n[i])

for i in range(-1, -cnt-1, -1) :
  print(n[i], end=' ')