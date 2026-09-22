"""
Day 1 - Loops & Iteration
Scenario-based exercises
"""

# ---------------------------------------------------------
# Scenario 1: Print order numbers
# Print order numbers 101 through 105 (inclusive).
# ---------------------------------------------------------
for i in range(101, 106):
    print(i)


# ---------------------------------------------------------
# Scenario 2: Numbered customer list
# Print each customer with a 1-based position number, like:
# 1. Aditi
# 2. Rohan
# 3. Meera
# ---------------------------------------------------------
customers = ["Aditi", "Rohan", "Meera"]

for i, c in enumerate(customers, start=1):
    print(f"{i}. {c}")


# ---------------------------------------------------------
# Scenario 3: Print customer balances
# Print each customer and their balance like:
# C001: 123
# C002: 456
# ---------------------------------------------------------
balances = {"C001": 123, "C002": 456}

for key, value in balances.items():
    print(f"{key}: {value}")


# ---------------------------------------------------------
# Scenario 4: Retry logic
# Simulate retrying a failed API call, max 3 attempts.
# Print "Attempt 1", "Attempt 2", "Attempt 3", then stop.
# ---------------------------------------------------------
n = 1
while n <= 3:
    print(f"Attempt {n}")
    n += 1


# ---------------------------------------------------------
# Scenario 5: Stop at first failed transaction
# Loop through amounts. Print each amount.
# If a negative number is hit, print "Invalid transaction found!"
# and stop the loop entirely.
# ---------------------------------------------------------
amounts = [100, 250, -50, 300]

for amount in amounts:
    if amount < 0:
        print("Invalid transaction found!")
        break
    print(amount)