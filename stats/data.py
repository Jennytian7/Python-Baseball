import os
import glob
import pandas as pd

game_files = glob.glob(os.path.join(os.getcwd(), 'games', '*.EVE'))
game_files.sort()

game_frames =[]

for game_file in game_files:
    game_frame = pd.read_csv(game_file, names =['type', 'multi2', 'multi3', 'multi4','multi5', 'multi6', 'event'])
    game_frames.append(game_frame)

# print(type(game_frames))
games = pd.concat(game_frames)
#8 Use the loc[] function to select rows that have a value of ?? in the multi5 column in the games DataFrame.
#Replace ?? with an empty string.
# games.loc[:, ['multi5' =='??'] ]=""
games.loc[games['multi5'] == '??', ['multi5']] = ''
#9
identifiers = games['multi2'].str.extract(r'(.LS(\d{4})\d{5})')
#10
identifiers = identifiers.fillna(method='ffill')
#11 rename colounms
identifiers.columns=['game_id', 'year']
#12 concatenate identifier columns
games = pd.concat([games, identifiers], axis=1,sort=False)
#13 fill NaN value
games = games.fillna(' ')
#14 Categorical Event Type
games.loc[:, 'type'] = pd.Categorical(games.loc[:, 'type'])
# 15 print dataframe
print(games.head(5))
