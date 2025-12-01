import pandas as pd


df = pd.read_csv("sales.csv")
print("\n DATA LOADED SUCCESSFULLY!\n")
print(df.head())


print("\n DATASET INFORMATION:")
print(df.info())

print("\n STATISTICS:")
print(df.describe())


print("\n MISSING VALUES:")
print(df.isnull().sum())


df["Total_Sales"] = df["Units"] * df["Price"]

total_revenue = df["Total_Sales"].sum()


best_by_units = df.loc[df["Units"].idxmax()]
best_by_revenue = df.loc[df["Total_Sales"].idxmax()]


print("\n---------------------------------------")
print(" FINAL SALES REPORT")
print("---------------------------------------")

print(f"\n TOTAL REVENUE GENERATED: ₹{total_revenue:,}")

print("\n BEST-SELLING PRODUCT (BY UNITS):")
print(best_by_units)

print("\n HIGHEST REVENUE PRODUCT:")
print(best_by_revenue)

print("\n FULL DATAFRAME:")
print(df)
