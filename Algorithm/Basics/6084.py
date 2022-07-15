h, b, c, s = input().split()
h = int(h)
b = int(b)
c = int(c)
s = int(s)

pcm = ((float(h*b*c*s)/8)/1024)/1024

print(round(pcm, 1), 'MB')