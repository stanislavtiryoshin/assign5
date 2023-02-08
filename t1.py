lower = 0
upper = 1
sub_int = 5
def func(x):
  return pow(x, 3)
def trapezoidal(func, lower, upper, n): 
  h = (upper-lower)/n # step size
  integ = func(lower) + func(upper)
  for i in range(1, n):
    k = lower + i*h
    integ = integ + 2 * func(k)
  integ = integ * h/2
  # result
  return integ

res = trapezoidal(func, lower, upper, sub_int)
print("Result is: %0.6f" % (res))