import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency

# ==========================================================
# STREAMING PLATFORM USAGE AND ENTERTAINMENT PREFERENCES
# ==========================================================

print("\n" + "=" * 60)
print("   STREAMING PLATFORM USAGE & ENTERTAINMENT")
print("             STATISTICAL ANALYSIS")
print("=" * 60)

# ----------------------------------------------------------
# 1. LOAD DATASET
# ----------------------------------------------------------

file_name = "Streaming_Platform_Usage_Dataset.xlsx"

data = pd.read_excel(file_name)

print("\nDataset loaded successfully!")
print("Number of records analyzed:", len(data))


# ----------------------------------------------------------
# 2. DESCRIPTIVE STATISTICS
# ----------------------------------------------------------

hours = data["Viewing_Hours_Per_Week"]

mean = hours.mean()
median = hours.median()
std_dev = hours.std()
coefficient_variation = (std_dev / mean) * 100

print("\n" + "-" * 60)
print("                 DESCRIPTIVE STATISTICS")
print("-" * 60)

print(f"Mean Viewing Hours          : {mean:.2f} hours")
print(f"Median Viewing Hours        : {median:.2f} hours")
print(f"Standard Deviation          : {std_dev:.2f} hours")
print(f"Coefficient of Variation    : {coefficient_variation:.2f}%")


# ----------------------------------------------------------
# 3. FREQUENCY DISTRIBUTION
# ----------------------------------------------------------

frequency = data["Preferred_Content"].value_counts()

print("\n" + "-" * 60)
print("                 CONTENT PREFERENCE")
print("-" * 60)

for content, count in frequency.items():
    print(f"{content:<25} : {count}")


most_preferred = frequency.idxmax()

print(f"\nMost Preferred Content     : {most_preferred}")


# ----------------------------------------------------------
# 4. CHI-SQUARE TEST
# ----------------------------------------------------------

print("\n" + "-" * 60)
print("                    CHI-SQUARE TEST")
print("-" * 60)

print("\nTesting relationship between:")
print("Age Group and Subscription Status")

table = pd.crosstab(
    data["Age_Group"],
    data["Subscription"]
)

print("\nContingency Table:")
print(table)

chi_square, p_value, degrees_freedom, expected = chi2_contingency(table)

alpha = 0.05

print(f"\nChi-Square Statistic        : {chi_square:.3f}")
print(f"Degrees of Freedom          : {degrees_freedom}")
print(f"P-Value                     : {p_value:.3f}")
print(f"Significance Level           : {alpha}")

if p_value < alpha:
    conclusion = "There IS a significant association."
else:
    conclusion = "There is NO significant association."

print("\nConclusion:")
print(conclusion)


# ----------------------------------------------------------
# 5. GRAPH 1 - VIEWING HOURS
# ----------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.hist(hours, bins=6, edgecolor="black")

plt.title("Distribution of Weekly Viewing Hours")
plt.xlabel("Viewing Hours per Week")
plt.ylabel("Number of Users")

plt.tight_layout()
plt.show()


# ----------------------------------------------------------
# 6. GRAPH 2 - CONTENT PREFERENCE
# ----------------------------------------------------------

plt.figure(figsize=(8, 5))

frequency.plot(kind="bar")

plt.title("Preferred Entertainment Content")
plt.xlabel("Content Type")
plt.ylabel("Number of Users")

plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# ----------------------------------------------------------
# 7. GRAPH 3 - SUBSCRIPTION BY AGE GROUP
# ----------------------------------------------------------

subscription_table = pd.crosstab(
    data["Age_Group"],
    data["Subscription"]
)

subscription_table.plot(
    kind="bar",
    figsize=(8, 5)
)

plt.title("Subscription Status by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Number of Users")

plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# ----------------------------------------------------------
# END
# ----------------------------------------------------------

print("\n" + "=" * 60)
print("             ANALYSIS COMPLETED SUCCESSFULLY")
print("=" * 60)