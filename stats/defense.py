import pandas as pd
import matplotlib.pyplot as plt
from data import games
from frames import  info, events

# plays = games.query( games['type']=='play' &  ~games['event'].str.contains('NP'))
plays = games.query("type == 'play' & event != 'NP'")
#3 col labels
plays.columns = ['type', 'inning', 'team', 'player', 'count', 'pitches', 'event', 'game_id', 'year']
#4 shift dataframe
pa =plays.loc[plays['player'].shift() != plays['player'],  ['year', 'game_id', 'inning', 'team', 'player']]
# 5 Group Plate Appearances
#We need to then calculate the plate appearances for each team for each game.
pa =pa.groupby(['year', 'game_id', 'team']).size().reset_index(name = 'PA')
#6  Set the Index
#In order to calculate the DER of a team, we need to reshape the data by the type of event that happened at each plate appearance.
#The event types need to be the columns of our DataFrame. The unstack() function is perfect for this.
events = events. set_index(['year', 'game_id', 'team', 'event_type'])
#7 unstack the dataframe
events = events.unstack().fillna(0).reset_index()
#8 Manage Column Labels
events.columns = events.columns.droplevel()
events.columns = ['year', 'game_id', 'team', 'BB', 'E', 'H', 'HBP', 'HR', 'ROE', 'SO']
events = rename_axis(None, axis="columns")
#9 Merge - Plate Appearances
events_plus_pa = pd.merge( events, pa, how = 'outer', left_on =['year', 'game_id', 'team'], right_on =['year', 'game_id', 'team'])
#10 Merge - Team
defense = pd.merge(events_plus_pa, info)
#11 Calculate DER
defense.loc[:, 'DER'] = 1 - ((defense['H'] + defense['ROE']) / (defense['PA'] - defense['BB'] -defense['SO'] - defense['HBP'] - defense['HR']))
dense.loc[:, 'year'] = pd.to_numeric(dense['year'])
#12 Reshape With Pivot
der = dense.loc[ defense['year'] >=  1978. ['year', 'defense', 'DER'] ]
der = der.pivot(index ='year', columns ='defense', values = 'DER')
#13 Plot Formatting - xticks
der.plot(x_compat = True, sticks =range(1978, 2018, 4), rot=45)
plt.show()
