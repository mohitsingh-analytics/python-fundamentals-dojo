# Scenario 1: Print order numbers
# You need to print order numbers 101 through 105 (inclusive).
# Use range() with start and stop arguments.

for i in range(101, 106):
    print(i)

customer = ["C001", "C002", "C003", "C004", "C005"]

for index, value in enumerate(customer):
    print(f"Index: {index}, Customer ID: {value}")


# Scenario 2: Numbered customer list
# Print each customer with a 1-based position number (not 0-based), like:
# 1. Aditi
# 2. Rohan
# 3. Meera


customer = ["Aditi", "Rohan", "Meera"]
for index, value in enumerate(customer,start=1):
    print(f"{index}. {value}")      


# Scenario 3: Print customer balances
# Given the balances dict, print each customer and their balance like:
# C001: 123
# C002: 456


balances = {"C001": 123, "C002": 456}
for key in balances:
    print(key)

for key,values in balances.items():
    print(key, values)

for value in balances.values():
    print(value)

# Scenario 4: Retry logic
# You're retrying a failed API call, max 3 attempts.
# Print "Attempt 1", "Attempt 2", "Attempt 3", then stop.
# Use a while loop with a counter.

n = 1
while n <= 3:
    print(f"attempt {n}")
    n += 1