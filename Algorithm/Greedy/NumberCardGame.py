n, m = input().split()
n = int(n)
m = int(m)
min = 0
card = [[0]*m for _ in range(n)]
for i in range(n) :
  card[i] = list(map(int, input().split()))
  card[i].sort()
  if min < card[i][0] :
    min = card[i][0]
print(min)

#25분 클리어