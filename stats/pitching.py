import pandas as pd
import matplotlib.pyplot as plt

from data import games
plays =  games.loc[(games['type'] == 'play'), :]
strike_outs = plays[plays['event'].str.contains('K')]
strike_outs = strike_outs.groupby(['year', 'game_id']).size()
strike_outs = strike_outs.reset_index(name='strike_outs')#grouby to dataframe
#5Apply an Operation to Multiple Columns
strike_outs = strike_outs.loc[:, ['year',  'strike_outs']].apply(pd.to_numeric)
# strike_outs.head()
strike_outs.plot.scatter(x = 'year', y='strike_outs')
plt.legend('Strike_outs')
plt.show()
