import pandas as pd
import matplotlib.pyplot as plt

fifa = pd.read_csv('FIFA19.csv')
pd.set_option('display.max_column',None)

fifa.shape
fifa.head()
fifa.columns

# Age
fifa.Age.max()
fifa.Age.median()    
fifa.Age.min(

# Nacionalidade com maior frequencia 
group = fifa.groupby('Nationality')
group['ID'].count().sort_values(ascending=False)
tb_freq_nacao = fifa.groupby('Nationality')['ID'].count().sort_values(ascending=False)
tb_freq_nacao / tb_freq_nacao.sum() 

tb_freq_nacao = fifa.groupby('Potential')['Nationality'].count().sort_values(ascending=False)
tb_freq_nacao / tb_freq_nacao.sum() 

# Atletas de maior potencial
fifa[fifa['Potential'] == fifa['Potential'].max()]['Name']
fifa.loc[:,['Name','Potential']].sort_values('Potential',ascending=False)

# Atletas de maior valor
fifa[fifa['Value'] == fifa['Value'].max()]['Name']
fifa.loc[:,['Name','Value']].sort_values('Value',ascending=False)


salaries = fifa['Value'].str.replace('€', '').str.replace('K','000').str.replace('M','000000').astype(float)
salaries.min()

plt.boxplot(salaries)
plt.show()

