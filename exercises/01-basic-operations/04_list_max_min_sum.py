# Find max, min, and sum of a list
numbers = [4, 12, 5, 70, 1]
print(f"Max: {max(numbers)}")
print(f"Min: {min(numbers)}")
print(f"Sum: {sum(numbers)}")

# Alternative method using for and if
max_val = numbers[0]
min_val = numbers[0]
total = 0
for num in numbers:
    if num > max_val:
        max_val = num
    if num < min_val:
        min_val = num
    total += num

print(f"Max (by loop): {max_val}")
print(f"Min (by loop): {min_val}")
print(f"Sum (by loop): {total}")
