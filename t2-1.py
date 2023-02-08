import math

lower = 0
upper = math.pi
sub_int = 11

def func(x):
  return math.sin(x)

def simpson13(func, lower, upper, n):
  h = (upper - lower) / n
  integ = func(lower) + func(upper)
  for i in range(1, n):
    k = lower + i*h
    if i % 2 == 0:
      integ = integ + 2 * func(k)
    else:
      integ = integ + 4 * func(k)
  integ = integ * h / 3
  return integ

res = simpson13(func, lower, upper, sub_int)
print("Result is: %0.6f" % (res))