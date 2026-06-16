import pandas as pd
import matplotlib.pyplot as plt
from lifelines import KaplanMeierFitter

# Load funded startups only
df = pd.read_csv("startup_survival_funded.csv")

# Create funding groups (quartiles)
df["funding_group"] = pd.qcut(
    df["funding_total_usd"],
    q=4,
    labels=["Low", "Medium-Low", "Medium-High", "High"]
)

# Plot
plt.figure(figsize=(12, 7))

kmf = KaplanMeierFitter()

for group in df["funding_group"].unique():
    subset = df[df["funding_group"] == group]

    kmf.fit(
        subset["survival_time_days"],
        subset["event"],
        label=group
    )

    kmf.plot_survival_function()

plt.title("Startup Survival by Funding Level")
plt.xlabel("Days")
plt.ylabel("Survival Probability")
plt.grid(True)

plt.savefig(
    "plots/funding_levels_km.png",
    dpi=300,
    bbox_inches="tight"
)

print("Saved: plots/funding_levels_km.png")

plt.show()