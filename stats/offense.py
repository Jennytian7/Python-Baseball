import pandas as pd
import matplotlib.pyplot as plt
from data import games
plays = games[games['type']=='play']
plays.columns = ['type', 'inning', 'team', 'player', 'count', 'pitches', 'event', 'game_id',  'year']

#2 Select Only Hits
# Use loc[], str.contains() and the regex '^(?:S(?!B)|D|T|HR)'
# to select the rows where the event column's value starts with S (not SB), D, T, and HR in the plays DataFrame.
hits = plays.loc[plays['event'].str.contains('^(?:S(?!B)|D|T|HR)'), ['inning', 'event']]
# plays[plays['event'].str.contains('K')]

#3 Convert Column Type
# hits.loc[:, 'inning'] = hits.loc[:, 'inning'].apply(pd.to_numeric) #apply used for multiple col
hits.loc[:, 'inning'] = pd.to_numeric(hits.loc[:, 'inning'])

#4 Replace Dictionary
replacements = {r'^S(.*)': 'single',
                r'^D(.*)': 'double',
                r'^T(.*)': 'triple',
                r'^HR(.*)': 'hr'}

#5 Replace Function
hit_type = hits['event'].replace(replacements, regex=True) #Call the replace() function on the hits['event'] column

#6 Add A New Column
hits = hits.assign(hit_type=hit_type) #(new col name, new col)
# #We have previously created new columns using groupby and concatenated DataFrames together.
# This time we will add a new column with assign().
# Below the replace() function, call assign() on the hits DataFrame,
# and pass in the keyword argument with the new column name and the new column hit_type=hit_type.
# Reassign the new resulting DataFrame to hits.

#7 Group By Inning and Hit Type
hits = hits.groupby(['inning', 'hit_type']).size().reset_index(name='count')
# hits = hits.groupby(['inning', 'hit_type']).size()
# hits = hits.reset_index(name='count')#grouby to dataframe

#8 Convert Hit Type to Categorical
hits['hit_type'] = pd.Categorical(hits['hit_type'], ['single', 'double', 'triple', 'hr'])

# 9 Sort Values
# hits = hits.sort_values(by =['inning', 'hit_type'])
hits = hits.sort_values(['inning', 'hit_type'])

# 10 Reshape With Pivot
#We need to reshape the hits DataFrame for plotting.
hits = hits.pivot(index='inning', columns='hit_type', values='count')

#11 Stacked Bar Plot
hits.plot.bar(stacked = True)
plt.show()
#The most appropriate plot for our data is a stacked bar chart.
#To create this type of plot call plot.bar() with stacked set to True on the hits DataFrame.
