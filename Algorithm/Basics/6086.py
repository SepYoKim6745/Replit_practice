n = int(input())
sum = 1
for i in range(2,n) :
  sum += i
  if n <= sum :
    break
print(sum)