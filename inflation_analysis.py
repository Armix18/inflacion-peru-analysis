# import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# style configuration
plt.style.use('default')
sns.set_palette('husl')

# load csv dataset
df = pd.read_csv('inflation_analysis.csv', encoding = 'latin-1', sep = ',', header = None, skiprows = 2)

# rename columns
df.columns = ['month_year', 'month_variation']

# change date column name (Ene00 -> 2000-01)
# month dictionary
months = {
    'Ene': '01', 'Feb': '02', 'Mar': '03', 'Abr': '04',
    'May': '05', 'Jun': '06', 'Jul': '07', 'Ago': '08',
    'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'
}

# extract month and year
df['month'] = df['month_year'].str[:3]
df['year'] = df['month_year'].str[3:]

# correct year (00 -> 2000, 01 -> 2001, ...)
df['year'] = df['year'].astype(int)
df['year'] = df['year'].apply(lambda x: 2000 + x if x <=25 else 1900 + x)

# create date column
df['date'] = pd.to_datetime(df['year'].astype(str) + '-' + df['month'].map(months), format = '%Y-%m')

# convert variation to number and clean data
df['month_variation'] = pd.to_numeric(df['month_variation'], errors = 'coerce')

# filter year from 2020
df = df[df['date'] >= '2020-01-01'].copy()

# date sorting
df = df.sort_values('date').reset_index(drop = True)

# view data
print('First 10 rows: \n', df.head(10))
print('\nMonth change statistics (%):')
print(df['month_variation'].describe())

# Graphic 1: Monthly inflation line Food and Energy 2020-2025
ax = df.plot(x = 'date', y = 'month_variation', kind = 'line', marker = 'o', linewidth = 2, color = 'teal')
ax.set_title('Monthly Change in CPI Food and Energy - Metropolitan Lima (2020-2025)')
ax.set_xlabel('Date')
ax.set_ylabel('Month % change')
ax.axhline(y = 0, color = 'gray', linestyle = '--', alpha = 0.7)

plt.savefig('inflacion_mensual_2020_2025.png', dpi=300) 
plt.show()