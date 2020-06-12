import pandas as pd
import matplotlib.pyplot as plt
# from stats import data
from data import games

attendance = games.loc[(games['type'] == 'info') & (games['multi2'] == 'attendance'), ['multi3', 'year']]
attendance.columns = ['attendance', 'year']
#6
attendance.loc[:, 'attendance']=pd.to_numeric(attendance.loc[:, 'attendance'])

# plt.figure(figsize=(15,7), kind='bar')
attendance.plot(x='year', y='attendance', figsize=(15,7), kind='bar')
plt.xlabel('Year')
plt.ylabel('Attendance')

plt.axhline(attendance['attendance'].mean(), linestyle = '--', color = 'green')
plt.show
