import pandas as pd
import joblib
from pathlib import Path

model_path = Path(__file__).resolve().parent / "model.pkl"
features = ["age", "sex", "smoking_status", "pd_l1", "tmb", "kras_mutated", "egfr_mutated"]

if not model_path.exists():
    raise FileNotFoundError("model.pkl missing")

model = joblib.load(model_path)

def predict_patient(data):
    row = {f: data.get(f, 0) for f in features}
    frame = pd.DataFrame([row])
    proba = model.predict_proba(frame)[0][1]
    return float(proba)
