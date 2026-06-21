import pandas as pd

application = pd.read_csv("data/application.csv")

print(application.head())
print(application.shape)
print(application.columns)