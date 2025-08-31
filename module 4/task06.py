import random

N = int(input("How many random points to generate? "))

Inside_Circle = 0

for _ in range(N):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x*x + y*y < 1:
        Inside_Circle += 1

pi_approx = 4 * Inside_Circle / N
print(f"Approximation of pi: {pi_approx}")
