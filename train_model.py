import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from feature_extraction import extract_features

df = pd.read_csv("dataset.csv")

X = df['url'].apply(lambda u: extract_features(u)).tolist()
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)

# ✅ Save both model + accuracy
pickle.dump({
    "model": model,
    "accuracy": accuracy
}, open("model.pkl", "wb"))

print("Model + accuracy saved!")