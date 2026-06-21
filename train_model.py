import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("data/final_features.csv")

for col in df.select_dtypes(include="object"):
    df[col] = LabelEncoder().fit_transform(df[col])

X = df.drop(["id", "default_12m"], axis=1)
y = df["default_12m"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier()

model.fit(X_train, y_train)

pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, pred))

import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("data/final_features.csv")

for col in df.select_dtypes(include="object"):
    df[col] = LabelEncoder().fit_transform(df[col])

X = df.drop(["id", "default_12m"], axis=1)
y = df["default_12m"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

joblib.dump(model, "models/risk_model.pkl")

print("Model saved successfully!")