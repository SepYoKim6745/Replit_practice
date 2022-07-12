n = int(input(), 16)

for i in range(1, 16) :
  print(format(n,'X')+'*'+format(i,'X')+'='+format(n*i, 'X'))