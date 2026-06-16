import pandas as pd
import matplotlib.pyplot as plt
from lifelines import KaplanMeierFitter
from lifelines.statistics import multivariate_logrank_test

# Load data
df = pd.read_csv("startup_survival_funded.csv")

# Keep only startups with funding rounds data
df = df[df["funding_rounds"].notna()].copy()

# Create groups
df["round_group"] = pd.cut(
    df["funding_rounds"],
    bins=[0, 1, 3, 100],
    labels=["1 Round", "2-3 Rounds", "4+ Rounds"]
)

# Plot Kaplan-Meier curves
plt.figure(figsize=(12, 7))

kmf = KaplanMeierFitter()

for group in df["round_group"].dropna().unique():
    subset = df[df["round_group"] == group]

    kmf.fit(
        subset["survival_time_days"],
        subset["event"],
        label=group
    )

    kmf.plot_survival_function()

plt.title("Startup Survival by Funding Rounds")
plt.xlabel("Days")
plt.ylabel("Survival Probability")
plt.grid(True)

plt.savefig(
    "plots/funding_rounds_km.png",
    dpi=300,
    bbox_inches="tight"
)

print("Saved: plots/funding_rounds_km.png")

# Log-rank test
results = multivariate_logrank_test(
    df["survival_time_days"],
    df["round_group"],
    df["event"]
)

print("\nLog-Rank Test:")
print(results.summary)

plt.show()