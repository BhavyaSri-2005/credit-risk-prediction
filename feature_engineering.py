import pandas as pd

df = pd.read_csv("data/final_dataset.csv")

df["debt_income_ratio"] = (
    df["total_debt"] /
    (df["annual_income"] + 1)
)

df["payment_ratio"] = (
    df["total_repaid_amount"] /
    (df["total_loan_amount"] + 1)
)

df.to_csv("data/final_features.csv", index=False)

print("Feature engineering completed!")