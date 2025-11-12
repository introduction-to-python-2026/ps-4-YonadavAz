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
    pass # Replace the `pass` with your code
