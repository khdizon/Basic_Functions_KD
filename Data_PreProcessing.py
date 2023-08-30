### DATA PREPROCESSING ###
#1 Cleaning 
#2 Missing Values
#3 Scaling
#4 Feature Engineering/Selection

Version  | Date | Author | Notes |
:-------:|:----:|:-------|:-----:|
0.1 |23 July 2023| Ken Dizon | Initial version |

# copy of original data failsafe
df_copy = df.copy()

# Join and Combine a dataset
merge(): To combine the datasets on common column or index or both.
concat(): To combine the datasets across rows or columns.
join(): To combine the datasets on key column or index.

# check missing values
df.isnull().sum()

# Visualize missing values
    #Graphically
missing = df_copy.isnull().sum()
missing = missing[missing > 0]
missing.sort_values(inplace=True)
missing.plot.bar()
    #Numerically
total = df_copy.isnull().sum().sort_values(ascending=False)
percent = (df_copy.isnull().sum()/df.isnull().count()).sort_values(ascending=False)
missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
missing_data.head(20)
or 
df.X1.isnull().sum() # single column
df.X1.isnull().sum() / df.shape[0] * 100


### Working with Pandas
# Rows
df.iloc[0]
df.iloc[[0,3,4,7]]
# Columns
df['X1']
df['X1', 'X2']
    # Columns using index (Row, Column)
df.iloc[5:8, :] #rows 5,6,7 all columns
df.iloc[:, 0:2] #all rows first two columns
# Slices
import string
alpha = string.ascii_letters
alpha[0:5] #first five
alpha[:5] #up to five
alpha[-1] #last character
alpha[-5:] #last five


# Drop columns 
df_copy.drop(columns=['X'], inplace=True)
# Drop rows with missing values
df_copy.dropna()
df_copy.drop(df_copy.index[0], inplace=True) #first row only


# Drop duplicates, if necessary
df_copy.drop_duplicates()


# Fill missing values, if necessary
df_copy.fillna(value)


# Boolean array with comparison opperator to filter df
df['X1'] == 'Category'
# Selecting specific column and value
X1_df = df[df['X1'] == 'Category']
X1_df.head()
or
subset = df[df['X1'] == selected_value]

# If we had some missing X1 values, we might fill those with the median:
df['X1'].fillna(df['X1'].median(), inplace=True)


# Scaling and Cleaning for ML
df['X1'] = df['X1'].replace({'Category 1': 0, 'Category 2': 1, 'Category 3':2})
df['X1']


# Correlation - ML Feature Selection
sns.scatterplot(data=df,x='X1', y='X2',hue='Category n') # specific X and Y
or 
sns.pairplot(df) #all columns
or 
# setting some parameters of the plot to help readability
f, ax = plt.subplots(figsize=(12,10)) 
sns.heatmap(df, vmax = .8, square=True)
or
sns.heatmap(df, cbar=True, annot=True, square=True, fmt='.2f',
            annot_kws={'size':14}, 
            yticklabels=cols.values,
            xticklabels=cols.values)
plt.show
or
#Numpy corrcoef gives a pearson correlation coefficient
'''If there is >30 variables. Choose Y as a ML target variable to try predict Target based on Xs. 
Let's look at the top n variables related to Y.
'''
n = int(input('Enter top n variables related to Y: '))
cols = df.nlargest(n, 'Y')['Y'].index
cm = np.corrcoef(df[cols].values.T)
sns.set(font_scale = 1.25)
f, ax = plt.subplots(figsize=(10,8))
hm = sns.heatmap(cm, cbar=True, annot=True, square=True, fmt='.2f',
                 annot_kws={'size':14},
                 yticklabels=cols.values,
                 xticklabels=cols.values)
plt.show


# Saving cleaned/new_DF
df.to_csv('prepped_Xs_data.csv')
