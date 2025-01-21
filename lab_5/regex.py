import re

with open('row.txt', encoding='utf-8') as file:
    content = file.read()

# Task 1
matches_a_b_star = re.findall(r"a(b*)", content)
print("Matches for 'a' followed by zero or more 'b's:")
print(matches_a_b_star)

# Task 2
matches_a_bb_bbb = re.findall(r"a(b{2,3})", content)
print("\nMatches for 'a' followed by two to three 'b's:")
print(matches_a_bb_bbb)

# Task 3
lowercase_underscore = re.findall(r"[a-z]+_[a-z]+", content)
print("\nSequences of lowercase letters joined with an underscore:")
print(lowercase_underscore)

# Task 4
uppercase_lowercase = re.findall(r"[A-Z][a-z]+", content)
print("\nSequences of one uppercase letter followed by lowercase letters:")
print(uppercase_lowercase)

# Task 5
matches_a_anything_b = re.findall(r"a.*b", content)
print("\nMatches for 'a' followed by anything, ending in 'b':")
print(matches_a_anything_b)

# Task 6
replaced_with_colon = re.sub(r"[ ,\.]", ":", content)
print("\nContent with spaces, commas, and dots replaced with colons:")
print(replaced_with_colon)

# Task 7
def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

snake_case_strings = re.findall(r"[a-z]+(_[a-z]+)+", content)
camel_case_results = [snake_to_camel(s) for s in snake_case_strings]
print("\nSnake case to camel case conversion:")
print(camel_case_results)

# Task 8
split_at_uppercase = re.findall(r'[A-Z][^A-Z]*', content)
print("\nSplit string at uppercase letters:")
print(split_at_uppercase)

# Task 9
spaced_capitals = re.sub(r"(?<!^)(?=[A-Z])", " ", content)
print("\nContent with spaces inserted between capitalized words:")
print(spaced_capitals)

# Task 1
def camel_to_snake(camel_str):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', camel_str).lower()

camel_case_strings = re.findall(r'[A-Za-z]+(?:[A-Z][a-z]*)+', content)
snake_case_results = [camel_to_snake(s) for s in camel_case_strings]
print("\nCamel case to snake case conversion:")
print(snake_case_results)
