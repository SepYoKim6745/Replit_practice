m = [[0]*11 for _ in range(11)]

for i in range(1, 11) :
  a = input().split()
  for j in range(1, 11) :
    a[j-1] = int(a[j-1])
    m[i][j] = a[j-1]
    if m[i][j] == 2 :
      ey = i
      ex = j

x = 2
y = 2
while 1 :
  if y == 9 and x == 9 : 
    break
  if ey == y and ex == x : 
    break
    
  m[y][x] = 9
  if m[y][x+1] == 1 :
    y+=1
  else :
    x+=1
m[y][x] = 9
for i in range(1, 11) :
  for j in range(1, 11) :
    print(m[i][j], end=' ')
  print()
  
  