# Startup Survival Analysis

## Factors Affecting Startup Survival: A Survival Analysis of Venture-Funded Startups

### Overview

This project investigates the factors associated with startup survival using survival analysis techniques on venture-funded startups from the Crunchbase dataset.

The study applies Kaplan-Meier survival estimation, Log-Rank hypothesis testing, and Cox Proportional Hazards modeling to examine how funding, funding rounds, industry sector, milestones, and startup relationships influence the risk of startup failure.

---

## Research Objectives

* Measure startup survival over time.
* Compare survival across different funding levels.
* Compare survival across funding-round groups.
* Examine survival differences across industries.
* Identify significant predictors of startup failure using Cox regression.

---

## Dataset

**Source:** Crunchbase Startup Dataset (Kaggle)

**Original Dataset Size:** 196,553 startups

**Final Venture-Funded Dataset:** 21,725 startups

### Key Variables

* Startup Status
* Founded Date
* Closed Date
* Funding Total (USD)
* Funding Rounds
* Industry Category
* Country
* Milestones
* Relationships

---

## Methodology

### Survival Analysis

* Kaplan-Meier Estimator
* Log-Rank Test
* Cox Proportional Hazards Model

### Event Definition

Startup closure (`status = closed`)

### Censoring

Operating, acquired, and IPO startups were treated as right-censored observations.

---

## Key Findings

### Funding Level

Startups receiving larger amounts of funding exhibited significantly higher survival probabilities.

### Funding Rounds

Startups completing more funding rounds demonstrated improved survival outcomes.

### Industry Effects

Startup survival differed significantly across industries, with notable differences between software, web, biotech, mobile, enterprise, and e-commerce companies.

### Cox Regression Results

| Variable       | Hazard Ratio |
| -------------- | -----------: |
| Log Funding    |         0.87 |
| Funding Rounds |         0.91 |
| Milestones     |         1.25 |
| Relationships  |         0.90 |

Interpretation:

* Hazard Ratio < 1 → Reduced failure risk
* Hazard Ratio > 1 → Increased failure risk

---

## Statistical Results

### Funding Level Comparison

Log-Rank Test:

* χ² = 258.103
* p = 1.1565 × 10⁻⁵⁵

### Funding Rounds Comparison

Log-Rank Test:

* χ² = 109.907
* p = 1.3614 × 10⁻²⁴

### Industry Comparison

Log-Rank Test:

* χ² = 227.726
* p = 3.2852 × 10⁻⁴⁷

---

## Visualizations

The project includes:

* Overall Kaplan-Meier Survival Curve
* Funding Level Survival Curves
* Funding Rounds Survival Curves
* Industry Survival Curves
* Hazard Ratio Plot
* Dataset Summary Table
* Cox Regression Results Table

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Lifelines

---

## Repository Structure

```text
data/
plots/
code/
report/
```

---

## Report

The complete project report is available in:

```text
report/Startup_Survival_Report.pdf
```

---

## Author

Adit Madan

B.Sc. Computer Science and Statistics

Independent Academic Research Project
