import pandas as pd

app = pd.read_csv("data/application.csv")
bureau = pd.read_csv("data/bureau.csv")
prev = pd.read_csv("data/previous_loans.csv")
pay = pd.read_csv("data/payments.csv")
cc = pd.read_csv("data/credit_card.csv")
labels = pd.read_csv("data/train_labels.csv")

df = app.merge(bureau, on="id")
df = df.merge(prev, on="id")
df = df.merge(pay, on="id")
df = df.merge(cc, on="id")
df = df.merge(labels, on="id")

print(df.head())
print(df.shape)

df.to_csv("data/final_dataset.csv", index=False)

print("Final dataset created successfully!")