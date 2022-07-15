r, g, b = input().split()
cnt = 0
r= int(r)
g = int(g)
b = int(b)

for i in range(r) :
  for j in range(g) :
    for z in range(b) :
      print(i, j, z)
      cnt+=1

print(cnt)