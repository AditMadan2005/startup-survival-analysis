import pandas as pd
import numpy as np
from lifelines import CoxPHFitter

df = pd.read_csv("startup_survival_funded.csv")

df["log_funding"] = np.log(df["funding_total_usd"])

cox_df = df[
    [
        "survival_time_days",
        "event",
        "log_funding",
        "funding_rounds",
        "milestones",
        "relationships"
    ]
].dropna()

cph = CoxPHFitter()

cph.fit(
    cox_df,
    duration_col="survival_time_days",
    event_col="event"
)

cph.check_assumptions(
    cox_df,
    p_value_threshold=0.05,
    show_plots=False
)