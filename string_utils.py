def split_before_each_uppercases(formula):
    a= ""
    c = []
    b = 0
    for i in formula:
        if not i.isdigit():
            a += i
        else:
            c.append(int(i))
    f = len(c)
    for x in range(f):
      z = c[x]
      b = b*10+z
    if b == 0:
      b = 1
    return a, b
            


def split_at_first_digit(formula):
    import string
def split_before_each_uppercases(formula):
  upper = string.ascii_uppercase
  a = ""
  b=[]
  for i in range(len(formula)):
    if formula[i] not in upper:
      a+=formula[i]
    else:
      a+=formula[i]
      b.append(a)
      a=""
  return b
