cnt = int(input())
n = input().split()
min = 100000
for i in range(cnt) :
  n[i] = int(n[i])
  if min > n[i] : min = n[i]

print(min)