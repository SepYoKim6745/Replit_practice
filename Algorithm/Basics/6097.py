sy, sx = input().split()
sx = int(sx)+1
sy = int(sy)+1
m = [[0]*sx for _ in range(sy)]

cnt = int(input())

for i in range(cnt) :
  l, d, y, x = input().split()
  l = int(l)
  d = int(d)
  y = int(y)
  x = int(x)

  if d == 0 :
    m[y][x] = 1
    for k in range(x, l+x) :
      m[y][k] = 1
  else :
    m[y][x] = 1
    for k in range(y, l+y) :
      m[k][x] = 1

for i in range(1, sy) :
  for j in range(1, sx) :
    print(m[i][j], end=' ')
  print()