def trim(L):
  l=len(L)
  for i in range(0, l):
    if L[i]==" ":
       a=i
    else:
        break
  L=L[a+1:]
  l=len(L)
  print a

  b=0
  for j in range(l-1, -1, -1):
    if L[j]==" ":
       b=j
    else:
       break
  print b
  return L[0:b]

print(trim(" hello  "))