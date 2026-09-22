"""
Day 1 - Loops & Iteration
Reference solutions (same as exercises.py in this case, since Mohit's
attempts matched the reference after correction).
"""

# Scenario 1
for i in range(101, 106):
    print(i)

# Scenario 2
customers = ["Aditi", "Rohan", "Meera"]
for i, c in enumerate(customers, start=1):
    print(f"{i}. {c}")

# Scenario 3
balances = {"C001": 123, "C002": 456}
for key, value in balances.items():
    print(f"{key}: {value}")

# Scenario 4
n = 1
while n <= 3:
    print(f"Attempt {n}")
    n += 1

# Scenario 5
amounts = [100, 250, -50, 300]
for amount in amounts:
    if amount < 0:
        print("Invalid transaction found!")
        break
    print(amount)