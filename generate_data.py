import pandas as pd
import numpy as np
import os

# Create data folder
os.makedirs("data", exist_ok=True)

n = 1000

# application.csv
application = pd.DataFrame({
    "id": range(1, n+1),
    "age": np.random.randint(21, 65, n),
    "gender": np.random.choice(["Male", "Female"], n),
    "annual_income": np.random.randint(200000, 2000000, n),
    "loan_amount": np.random.randint(50000, 1000000, n),
    "loan_term": np.random.choice([12, 24, 36, 48, 60], n),
    "employment_type": np.random.choice(["Salaried", "Self-employed"], n),
    "purpose": np.random.choice(["Home", "Car", "Business", "Education"], n),
    "num_dependents": np.random.randint(0, 6, n)
})
application.to_csv("data/application.csv", index=False)

# bureau.csv
bureau = pd.DataFrame({
    "id": range(1, n+1),
    "bureau_score": np.random.randint(300, 900, n),
    "num_of_accounts": np.random.randint(1, 10, n),
    "num_of_open_accounts": np.random.randint(1, 8, n),
    "total_debt": np.random.randint(10000, 1000000, n),
    "delinquencies": np.random.randint(0, 10, n)
})
bureau.to_csv("data/bureau.csv", index=False)

# previous_loans.csv
previous_loans = pd.DataFrame({
    "id": range(1, n+1),
    "num_loans": np.random.randint(0, 10, n),
    "num_defaults": np.random.randint(0, 3, n),
    "total_loan_amount": np.random.randint(50000, 2000000, n),
    "total_repaid_amount": np.random.randint(10000, 1800000, n),
    "avg_dpd": np.random.randint(0, 90, n)
})
previous_loans.to_csv("data/previous_loans.csv", index=False)

# payments.csv
payments = pd.DataFrame({
    "id": range(1, n+1),
    "months_on_book": np.random.randint(1, 60, n),
    "status": np.random.choice(["Paid", "Late"], n),
    "dpd": np.random.randint(0, 90, n),
    "payment_amount": np.random.randint(1000, 100000, n)
})
payments.to_csv("data/payments.csv", index=False)

# credit_card.csv
credit_card = pd.DataFrame({
    "id": range(1, n+1),
    "num_cards": np.random.randint(1, 5, n),
    "credit_limit": np.random.randint(50000, 500000, n),
    "utilization_ratio": np.random.uniform(0, 1, n),
    "max_utilization_ratio": np.random.uniform(0, 1, n),
    "late_payments": np.random.randint(0, 20, n)
})
credit_card.to_csv("data/credit_card.csv", index=False)

# train_labels.csv
train_labels = pd.DataFrame({
    "id": range(1, n+1),
    "default_12m": np.random.choice([0, 1], n, p=[0.85, 0.15])
})
train_labels.to_csv("data/train_labels.csv", index=False)

# test.csv
test = pd.DataFrame({
    "id": range(1001, 1201)
})
test.to_csv("data/test.csv", index=False)

print("All 7 CSV files created successfully!")