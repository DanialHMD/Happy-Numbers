from unittest import skip

"""
A happy number is defined by following:
Starting with any positive integer, replace the number with sum of it's digits,
repeat the process until the number either equals to 1 or it loops in a cycle
which does not include 1.

Those with number 1 are called happy numbers and others are unhappies. :)
"""


def main(n):
  op = []
  while True:
    m = [int(i) for i in str(n)]
    n = 0
    for i in m:
      n = n + i**2
    if n not in op:
      op.append(n)
    else:
      break
  return op[-1]


def loop(number, happies):
  if main(number) != 1:
    skip
  else:
    happies.append(number)  


rounds = int(input("How many happy numbers do you want to find?"))
number = int(input("From where shoud I start?(ENTER NUMBER)"))
happies = []


while len(happies) < rounds:
  loop(number,happies)
  number += 1

print(happies)