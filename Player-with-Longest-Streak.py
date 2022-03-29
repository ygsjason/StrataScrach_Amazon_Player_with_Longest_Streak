# Import your libraries
import pandas as pd
import numpy as np

# Start writing code
df = players_results

df['pre'] = df['match_result'].shift(1).fillna('NA')
df
df['cpr'] = np.where(((df.match_result == 'W') & (df.pre == 'W')) | ((df.match_result == 'W') & (df.pre == 'L')), 1, 0)
df
#df1 = df.pivot_table(columns = 'player_id', values = 'cpr', aggfunc = 'sum').melt(value_name = 'streak')

#df1[df1.streak == df1.streak.max()]

#Method 2
df1 = df.groupby('player_id', as_index = False).agg({'match_result': 'sum'})

df1['streak']= df1.match_result.str.split('L')

df2 = df1.explode('streak')

df2['n'] = df2.streak.apply(lambda x: len(x))

df2[df2.n == df2.n.max()]

#Method 3
m = df['match_result'].str.upper().ne('W')
t = m.cumsum()
r = m.cumsum()[~m]
s = m.cumsum()[~m].groupby(df['player_id']).value_counts().reset_index(level =1, drop = True)

df3 = s.reset_index()

df3[df3.match_result == df3.match_result.max()]

df4 = s.agg({'player_id': 'idxmax', 'longest_winningstreak':'max'}).to_frame(0).T

#df1['new'] = df1.match_result.apply(lambda x: x.replace('', ',')[1:-1])
#str = 'wwllwwllw'
#str[1:-1]
