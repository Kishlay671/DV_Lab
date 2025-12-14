import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the single CSV file
data = pd.read_csv("house_prices.csv")

print("Data Shape:", data.shape)
print(data.head())

# Visualize: Living Area vs Sale Price, colored by Overall Quality
sns.scatterplot(data=data, x='GrLivArea', y='SalePrice', hue='OverallQual', palette='coolwarm')
plt.title("Living Area vs Sale Price (colored by Quality)")
plt.show()
