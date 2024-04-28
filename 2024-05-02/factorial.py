# Define factorial() below:
def factorial(n):
  if n == 1:
    return n
  return n * factorial(n - 1)

# Iterative
# def factorial(n):
#   result = 1
#   for i in range(1, n + 1):
#     result *= i
#   return result

print(factorial(13))