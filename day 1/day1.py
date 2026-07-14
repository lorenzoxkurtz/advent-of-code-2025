n=50
p=0
with open ('s.txt') as file:
   s= file.read().splitlines()
for r in s :
  dr= r[0]
  ds=int(r[1:])
  if dr=='L':
    ds=-ds
  n=n+ds
  n=n%100
  if n==0:
     p=p+1

print (p)



