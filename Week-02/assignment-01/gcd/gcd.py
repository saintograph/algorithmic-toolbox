# Uses python3
def gcd(a, b):
  while b:
    a, b = b, a % b
  return a

input = input()
a, b = map(int, input.split())
print(gcd(a, b))
