### DATA EXPLORATION ###

Version  | Date | Author | Notes |
:-------:|:----:|:-------|:-----:|
0.1 |23 July 2023| Ken Dizon | Initial version |

___________

df.head()
df.tail()
df.shape #Rows and Columns (attributes, features)
df.columns

### descriptive stats
df.info() 

# basic histogram
df.hist(column='X1', bins=n)
or
df['X1'].plot.hist()
or
df.hist(figsize=(13, 13)) 
plt.show() 

# summarize data
df.describe()
df.describe().T

# check missing values
df.isnull().sum()

# Count unique values in each categorical column
print("\nUnique Value Counts:")
categorical_columns = df.select_dtypes(include='object').columns
for col in categorical_columns:
    print(f"{col}: {df[col].nunique()}")

or
df.nunique()

# Checking if a specific categorical value is in a column
find_value = input('Enter a categorical value:')
if find_value in df['X1'].values:
    print(f"'{find_value}' exists in the 'X1' column.")
else:
    print(f"'{find_value}' does not exist in the 'X1' column.")

# Create a correlation matrix for numeric columns
correlation_matrix = df.corr()
    # Plot a heatmap to visualize the correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Correlation Matrix Heatmap")
plt.show()


# Boxplot for Outlier Detection for all numeric columns
df.boxplot('X1')
or
plt.figure(figsize=(10, 6))
df.boxplot()
plt.title("Box Plots for Numeric Columns")
plt.xticks(rotation=45)
plt.show()
or
sns.boxplot(data=df, orient='h')

