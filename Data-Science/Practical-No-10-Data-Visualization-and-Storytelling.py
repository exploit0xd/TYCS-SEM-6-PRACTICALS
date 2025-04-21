import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------- Load the Dataset -------------------
data = pd.read_csv('DATA_SET.csv')

# ------------------- Boxplot: Sales Distribution by Category -------------------
plt.figure(figsize=(10, 6))
sns.boxplot(x='Category', y='Sales', data=data)
plt.title('Sales Distribution by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.grid(axis='y')  # Add gridlines only to the y-axis
plt.tight_layout()
plt.show()

# ------------------- Scatter Plot: Sales vs. Profit -------------------
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Sales', y='Profit', data=data, hue='Category', palette='Set2')
plt.title('Sales vs. Profit')
plt.xlabel('Sales')
plt.ylabel('Profit')
plt.grid(True)  # Add gridlines to both axes
plt.tight_layout()
plt.show()

# ------------------- Conditional Insights -------------------
median_sales_by_category = data.groupby('Category')['Sales'].median().sort_values(ascending=False)

print("\nInsights:")
if median_sales_by_category.idxmax() == 'Clothing':
    print("- The 'Clothing' category has the highest median sales, followed by others.")
else:
    print(f"- The category with the highest median sales is: {median_sales_by_category.idxmax()}.")

# Check correlation between Sales and Profit
sales_profit_corr = data[['Sales', 'Profit']].corr().iloc[0, 1]
if sales_profit_corr > 0:
    print(f"- There is a positive correlation ({sales_profit_corr:.2f}) between Sales and Profit.")
else:
    print("- No strong positive correlation between Sales and Profit.")

# Check highest sales and corresponding category
max_sales = data['Sales'].max()
max_sales_category = data.loc[data['Sales'].idxmax(), 'Category']
print(f"- The product category with the highest individual sales record is: {max_sales_category}.")
