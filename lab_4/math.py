import math

# Task 1
degree = 15
# print(math.radians(degree))

# Task 2
height, base_1, base_2 = list(map(int, input().split()))
# print((1/2) * (base_1 + base_2) * height)

# Task 3
sides, length = list(map(int, input().split()))
# print((sides * length**2) / (4 * math.tan(math.pi / sides)))

# Task 4
length, height = list(map(int, input().split()))
# print(length * height)