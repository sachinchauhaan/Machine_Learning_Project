import pandas as pd
from pathlib import Path

base = Path(__file__).resolve().parent.parent
raw_path = base / "data.csv"
proc_path = base / "data" / "processed" / "processed.csv"

def encode(df):
    df = df.copy()
    df["sex"] = df["sex"].astype(str).str.lower().map({"male": 0, "female": 1})
    df["smoking_status"] = df["smoking_status"].astype(str).str.lower().map({"never": 0, "former": 1, "current": 2})
    df["kras_mutated"] = df["kras_mutated"].astype(float)
    df["egfr_mutated"] = df["egfr_mutated"].astype(float)
    return df

def build_frame(df):
    frame = pd.DataFrame()
    frame["age"] = df["patient_age"]
    frame["sex"] = df["patient_gender"]
    frame["smoking_status"] = df["smoking_history"]
    frame["pd_l1"] = df["PD-L1_expression_level"]
    frame["tmb"] = df["tumor_mutational_burden"]
    frame["kras_mutated"] = df["KRAS_mutation_status"]
    frame["egfr_mutated"] = df["EGFR_mutation_status"]
    frame["benefit"] = ((df["survival_time_months"] >= 18) & (df["immunotherapy_received"] == 1)).astype(int)
    return frame

def main():
    if not raw_path.exists():
        raise FileNotFoundError("data.csv missing")
    df = pd.read_csv(raw_path)
    df = build_frame(df)
    df = df.dropna()
    df = encode(df)
    df = df.dropna()
    proc_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(proc_path, index=False)

if __name__ == "__main__":
    main()
