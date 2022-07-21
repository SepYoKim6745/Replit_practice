cnt = int(input())
student = [0] * 24
n = input().split()

for i in range(cnt) :
  n[i] = int(n[i])

for i in range(cnt) :
  student[n[i]] += 1

for i in range(1, 24) :
  print(student[i], end=' ')