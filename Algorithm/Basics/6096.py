m = [[0]*20 for _ in range(20)]

for i in range(1, 20) :
  d = input().split()
  for j in range(1, 20) :
    d[j-1] = int(d[j-1])
    m[i][j] = d[j-1]

cnt = int(input())
for i in range(cnt) :
  y, x = input().split()
  x = int(x)
  y = int(y)
  for k in range(1, 20) :
    if m[y][k] == 0 :
      m[y][k] = 1
    else :
      m[y][k] = 0

    if m[k][x] == 0 :
      m[k][x] = 1
    else :
      m[k][x] = 0

for i in range(1,20) :
  for j in range(1,20) :
    print(m[i][j], end = ' ')
  print()