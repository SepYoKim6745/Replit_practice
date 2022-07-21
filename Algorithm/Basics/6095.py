map = [[0]*20 for _ in range(20)]
cnt = int(input())

for i in range(cnt) :
  x, y = input().split()
  x = int(x)
  y = int(y)
  map[x][y] = 1

for i in range(1, 20) :
  for j in range(1, 20) :
    print(map[i][j], end =' ')
  print()