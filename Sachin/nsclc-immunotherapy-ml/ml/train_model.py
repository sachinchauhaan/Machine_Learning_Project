import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import joblib

base = Path(__file__).resolve().parent.parent
data_path = base / "data" / "processed" / "processed.csv"
model_path = base / "ml" / "model.pkl"
features = ["age", "sex", "smoking_status", "pd_l1", "tmb", "kras_mutated", "egfr_mutated"]
target = "benefit"

def main():
    if not data_path.exists():
        raise FileNotFoundError("processed.csv missing")
    df = pd.read_csv(data_path)
    if target not in df.columns:
        raise ValueError("benefit column missing")
    X = df[features]
    y = df[target]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    lr = LogisticRegression(max_iter=1000)
    lr.fit(X_train, y_train)
    rf = RandomForestClassifier(n_estimators=200, random_state=42)
    rf.fit(X_train, y_train)
    joblib.dump(rf, model_path)

if __name__ == "__main__":
    main()
