import pandas as pd

order_data = pd.read_csv('./2019-winter-data-set-sheet1.csv')

# Checking the skewness in order amount values
print('Skewness in Order Amount:',order_data['order_amount'].skew())
print('Order Amount Data Description:\n', order_data['order_amount'].describe())

# Checking the skewness in total items values
print('Skewness in total items:',order_data['total_items'].skew())
print('Total Items Data Description:\n', order_data['total_items'].describe())

# Exclude maximum values from the data
normal_order_values = order_data['order_amount'] < 704000
normal_total_items = order_data['total_items'] < 2000
cleaned_data1= order_data[normal_order_values]
cleaned_data2 = order_data[normal_total_items]

# Calculate new AOV without the outliers
print('Adjusted AOV (by Order Amount) = $', round(cleaned_data1['order_amount'].mean(), 2))
print('Adjusted AOV (by Total Items) = $', round(cleaned_data2['order_amount'].mean(), 2))

# Check the shewness in the data again
print("Re-check skewness in cleaned data (by Order Amount):",cleaned_data1['order_amount'].skew())
print("Re-check skewness in cleaned data (by Total Items):",cleaned_data2['total_items'].skew())


# Data are still rightly skewed. The IQR method should be used to eliminate outliers.
Q1 = order_data['order_amount'].quantile(0.25)
Q3 = order_data['order_amount'].quantile(0.75)

IQR = Q3 - Q1

normal_order_values_IQR = (order_data['order_amount'] < (Q3 + 1.5 * IQR)) & (order_data['order_amount'] > (Q1 - 1.5 * IQR))
cleaned_data3 = order_data[normal_order_values_IQR]
print('Adjusted AOV (by IQR) = $', round(cleaned_data3['order_amount'].mean(), 2))
