def iterate_a_lot():
  for i in range(1000):
    for j in range(100):
      j

def iterate_a_little():
  for i in range(10):
    i 


# Reporting
import time
import random
import statistics

def fibonacci(n = 25, fib_memo = {}):
  if n == 0:
    return 0
  if n == 1:
    return 1
  if n not in fib_memo:
    fib_memo[n] = fibonacci(n-1) + fibonacci(n-2)
  return fib_memo[n]

functions = iterate_a_lot, iterate_a_little

# this is just a one line way to make this: {'iterate_a_lot': [], 'iterate_a_little': []}
times = {f.__name__: [] for f in functions}

for func in functions:
  for i in range(500):  # adjust accordingly so whole thing takes a few sec
    t0 = time.time()
    func()
    t1 = time.time()
    times[func.__name__].append((t1 - t0) * 1000)



for name, numbers in times.items():
  print('FUNCTION:', name, 'Used', len(numbers), 'times')
  print('\tMEDIAN', statistics.median(numbers))
  print('\tMEAN  ', statistics.mean(numbers))
  print('\tSTDEV ', statistics.stdev(numbers))