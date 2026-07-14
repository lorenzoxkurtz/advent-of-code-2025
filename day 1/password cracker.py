n=50
newpassword=0
p=0
with open ('s.txt') as file:
   s= file.read().splitlines()
for r in s :
  dr= r[0]
  ds=int(r[1:])
  if dr=='L':
    ds=-ds
    xtra=-1
  else:
     xtra=1
  oldn=n
  n=n+ds
  for i in range(oldn*xtra,n*xtra):
     if i%100==0:
       newpassword+=1    
  n= n%100
  if n==0:
     p=p+1

print (p)
print(newpassword)



