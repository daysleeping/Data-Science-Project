"""
Stem project -- data science
"""

"""
example provided from teachers:
import pandas as pd
data = pd.read_json('STEM.json')
print(data.columns)
Data1 = data['Stanley Sewage Treatment Work Sodium Hypochlorite dosage (mg/L)']
Data2 = data[['Day','Stonecutters Island Sewage Treatment Work Sodium Hypochlorite dosage (mg/L)', 'Stanley Sewage Treatment Work Sodium Hypochlorite dosage (mg/L)']]
Data2['Total (mg/L)'] = Data2['Stonecutters Island Sewage Treatment Work Sodium Hypochlorite dosage (mg/L)'] + Data2['Stanley Sewage Treatment Work Sodium Hypochlorite dosage (mg/L)']
print(Data2)
"""

# 0. Importing the necessary modules
import pandas as pd
import matplotlib.pyplot as plt
import time

# 1. Data Collecting
data = pd.read_csv('cowid-covid-data.csv')

# 2. Data Processing
useful_data = data[['continent','location','date','total_cases','total_deaths','total_cases_per_million','total_deaths_per_million','total_vaccinations','people_vaccinated','people_fully_vaccinated','population','population_density']]

# 3. Data analysing
useful_data['Death in 100 cases'] = useful_data['total_deaths'] / useful_data['total_cases'] * 100
print(f'All data in the world : \n {useful_data}')

# 4. Data accessing
print('Some country / location may not contain all the data.')
decision = input('Please select a country \n')
print(useful_data.loc[useful_data['location'] == decision])
print('Just simply close the window if you want.')
useful_data.loc[useful_data['location'] == decision].plot()
plt.show()
time.sleep(10)
