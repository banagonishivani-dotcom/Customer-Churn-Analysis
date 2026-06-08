import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

print("Dataset Shape:", df.shape)
print("\nColumns:")
print(df.columns)

# Churn distribution
print("\nChurn Count:")
print(df['Churn'].value_counts())

# Plot churn distribution
df['Churn'].value_counts().plot(kind='bar')
plt.title("Customer Churn Distribution")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")
plt.show()
# Check contract type vs churn
print("\nContract Type vs Churn")
print(pd.crosstab(df['Contract'], df['Churn']))