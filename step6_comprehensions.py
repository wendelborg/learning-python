# Step 6: List Comprehensions and Generators
# Experiment here before applying to main.py

# Sample data to work with
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

names = ["Alice", "Bob", "Charlie", "Dave", "Eve"]

# --- Exercise 6.1: Basic comprehension ---
# Create a list of all numbers doubled
# C#: numbers.Select(n => n * 2).ToList()
# Your code:
doubled = [n * 2 for n in numbers]

# --- Exercise 6.2: Filtered comprehension ---
# Create a list of only even numbers
# C#: numbers.Where(n => n % 2 == 0).ToList()
# Your code:
evens = [n for n in numbers if n % 2 == 0]

# --- Exercise 6.3: Transform + filter ---
# Create a list of doubled values, but only for numbers greater than 5
# C#: numbers.Where(n => n > 5).Select(n => n * 2).ToList()
# Your code:
big_doubled = [n * 2 for n in numbers if n > 5]

# --- Exercise 6.4: Strings ---
# Create a list of names in uppercase, but only names shorter than 5 characters
# C#: names.Where(n => n.Length < 5).Select(n => n.ToUpper()).ToList()
# Hint: len(s) for length, s.upper() for uppercase
# Your code:
short_upper = [s.upper() for s in names if len(s) < 5]

# --- Exercise 6.5: Counting with sum() ---
# Count how many numbers are greater than 5
# C#: numbers.Count(n => n > 5)
# Hint: sum(1 for ...) — generator inside sum()
# Your code:
count_big = sum(1 for n in numbers if n > 5)

# --- Print results ---
# Uncomment these as you go:
print(f"Doubled: {doubled}")
print(f"Evens: {evens}")
print(f"Big doubled: {big_doubled}")
print(f"Short upper: {short_upper}")
print(f"Count > 5: {count_big}")
