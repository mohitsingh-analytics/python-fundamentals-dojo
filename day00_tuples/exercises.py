# Scenario 1: Order processing
# A function returns (order_id, status, total_amount).
# Unpack it into three variables and print a formatted summary.

def get_order():
    return (1042, "shipped", 89.99)

# your code here


# Scenario 2: Swap without a temp variable
# You have two customer priority scores. Swap them using tuple unpacking.
score_a = 10
score_b = 25

# your code here


# Scenario 3: Ignoring values you don't need
# A function returns (customer_id, name, email, signup_date).
# You only need customer_id and email. Use _ to ignore the rest.

def get_customer():
    return (501, "Aditi", "aditi@mail.com", "2023-01-15")

# your code here


# Scenario 4: Variable-length unpacking
# A transaction log returns (date, *amounts) where amounts is variable length.
# Unpack date separately, and amounts as a list.

def get_transaction_log():
    return ("2024-03-01", 100, 250, 75, 400)

# your code here


# Scenario 5: Nested unpacking
# A function returns (customer_id, (lat, long)) — customer with location.
# Unpack customer_id, lat, long in one line.

def get_customer_location():
    return (77, (28.7041, 77.1025))

# your code here