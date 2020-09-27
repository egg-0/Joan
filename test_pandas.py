import pandas as pd

"""
df = pd.DataFrame(columns = ['Discord_ID','Steam_ID'])

print(df)

df.loc[0] = ['123','456']

print(df)

print(df.loc[df['Discord_ID'] == '123', 'Steam_ID'].item())


data = ['550098642871255068', '76561198043890292']

columns = ['Discord_ID', 'Steam_ID']

new_df = pd.DataFrame([data],columns=columns)"""

df1 = pd.DataFrame([['a', 1], ['b', 2]],
                   columns=['letter', 'number'])

df2 = pd.DataFrame([['c', 3], ['d', 4]],
                   columns=['letter', 'number'])

df3 = pd.concat([df1, df2], ignore_index=True)

print(df1)
print(df2)
print(df3)

