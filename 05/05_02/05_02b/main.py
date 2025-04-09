import math
number = 0

def exponent_finder(num):
  i = 0
  while num >= 2**i:
    i+=1
  if num==1:
    return 0
  elif num<1:
    return -1
  return i-1

start = exponent_finder(number)
two_exponents = [start]
residue = number
k = start
while residue>1:
  residue = residue - 2**k
  k = exponent_finder(residue)
  two_exponents.append(k)
max_exp = max(two_exponents)
bin_str = ''
if number>0:
  for exp in reversed(range(max_exp+1)):
    if exp in two_exponents:
      out_num = 1
    else:
      out_num = 0
    bin_str+=str(out_num)
else:
  bin_str = '0'
print(bin_str)





