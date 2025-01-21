# Task 1:
def grams_to_ounces(grams):
    return grams * 28.3495231

# Task 2:
def fahrenheit_to_celsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)

# Task 3:
def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if 2 * chickens + 4 * rabbits == numlegs:
            return chickens, rabbits
    return None, None

# Task 4:
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

# Task 5:
from itertools import permutations

def string_permutations(string):
    return [''.join(p) for p in permutations(string)]

# Task 6:
def reverse_words(sentence):
    return ' '.join(sentence.split()[::-1])

# Task 7:
def has_33(nums):
    return any(nums[i] == 3 and nums[i + 1] == 3 for i in range(len(nums) - 1))

# Task 8:
def spy_game(nums):
    code = [0, 0, 7]
    idx = 0
    for num in nums:
        if num == code[idx]:
            idx += 1
        if idx == len(code):
            return True
    return False

# Task 9:
import math

def sphere_volume(radius):
    return (4 / 3) * math.pi * radius**3

# Task 10:
def unique_elements(array):
    unique = []
    for i in array:
        if i not in unique:
            unique.append(i)
    return unique

# Task 11:
def is_palindrome(string):
    string = string.replace(" ", "").lower()
    return string == string[::-1]

# Task 12:
def histogram(array):
    for n in array:
        print('*' * n)

# Task 13:
import random

def guess_the_number():
    name = input("Hello! What is your name?\n")
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
    number = random.randint(1, 20)
    guesses = 0

    while True:
        guess = int(input("\nTake a guess.\n"))
        guesses += 1
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
            break

# 
with open("task_imports.py", "w") as file:
    file.write("""
from main import grams_to_ounces, solve, filter_prime, reverse_words

# Test grams to ounces
print(grams_to_ounces(100))  # 2834.95

# Test solve function
print(solve(35, 94))  # (23, 12)

# Test filter prime
print(filter_prime([2, 3, 4, 5, 6, 7, 8]))  # [2, 3, 5, 7]

# Test reverse words
print(reverse_words("We are ready"))  # ready are We
""")
