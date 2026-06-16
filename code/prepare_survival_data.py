import pandas as pd

# Load dataset
df = pd.read_csv("companies.csv")

# Keep only startups with a founding date
df = df[df["founded_at"].notna()].copy()

# Convert dates
df["founded_at"] = pd.to_datetime(df["founded_at"])
df["closed_at"] = pd.to_datetime(df["closed_at"])

# Create event variable
# 1 = startup failed (closed)
# 0 = still alive (operating, acquired, IPO)

df["event"] = (df["status"] == "closed").astype(int)

# Today's date for censored observations
today = pd.Timestamp.today()

# Survival end date
df["end_date"] = df["closed_at"]

df.loc[df["event"] == 0, "end_date"] = today

# Calculate survival time in days
df["survival_time_days"] = (
    df["end_date"] - df["founded_at"]
).dt.days

# Remove impossible values
df = df[df["survival_time_days"] > 0]

# Keep only useful columns
survival_df = df[
    [
        "name",
        "status",
        "event",
        "survival_time_days",
        "category_code",
        "country_code",
        "funding_rounds",
        "funding_total_usd",
        "milestones",
        "relationships"
    ]
]

# Save clean dataset
survival_df.to_csv(
    "startup_survival_clean.csv",
    index=False
)

print("Dataset created successfully")
print(survival_df.shape)

print("\nEvent counts:")
print(survival_df["event"].value_counts())