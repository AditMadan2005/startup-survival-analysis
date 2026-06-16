import pandas as pd

df = pd.read_csv("startup_survival_clean.csv")

funded_df = df[df["funding_total_usd"].notna()].copy()

print(funded_df.shape)

funded_df.to_csv(
    "startup_survival_funded.csv",
    index=False
)

print("Saved funded dataset")