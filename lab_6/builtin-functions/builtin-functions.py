import time, math

# Task 1
nums = [9, 8, 7, 6, 5, 4, 3, 52, 1]
def multiply_list(list):
  res = 1
  for i in list:
    res *= i
  return res
# print(multiply_list(nums))

# Task 2
def count_uppercase(message):
  upper_counter = 0
  lower_counter = 0
  for i in message:
    if 65 <= ord(i) <= 90:
      upper_counter += 1
    if 97 <= ord(i) <= 122:
      lower_counter += 1
      
  return dict(upper=upper_counter, lower=lower_counter)
message = "Show Me How You Feel"
# print(count_uppercase(message))

# Task 3
def isPal(message):
  reverze = str(message)[::-1]
  if str(message) == reverze:
    return True
  else:
    return False
# print(isPal("abba"))
# print(isPal("abdulmuhhamadchert"))

# Task 4
num = int(input())
delay = int(input())

time.sleep(delay / 1000)
result = math.sqrt(num)
print(f"Square root of {num} after {delay} milliseconds is {result}")

# Task 5
t = (True, 1, "hello", 5)
result = all(t)
print(result)