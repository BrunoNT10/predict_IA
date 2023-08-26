# %%
import requests
import pandas as pd
import numpy as np


# %%
def parse_year(msg):
    year = msg.split("/")[-1]
    
    return year

csv_path = "dataset/brasileirao_info.csv"

df = pd.read_csv(csv_path)

anos = sorted(list(set(list(df.data.apply(parse_year)))))

times = sorted(list(set(list(df['mandante']))))

# %%

df['pont_mandante'] = ["-"] * 8025
df['pont_visitante'] = ["-"] * 8025

print(df)
# hhjsjsj

for ano in anos:
    team_points = {}
    for time in times:
        team_points[time] = 0
        for i, row in df.iterrows():
            if row.data.split("/")[-1] == ano:
                if row.mandante == time or row.visitante == time:
                    if row.mandante == time:
                        df.at[i, 'pont_mandante'] = team_points[time]                                
                    else:
                        df.at[i, 'pont_visitante'] = team_points[time]
                        
                    if row.vencedor == time:
                        team_points[time] += 3
                    elif row.vencedor == '-':
                        team_points[time] += 1
            
        

df.to_csv("updated_pontuation.csv")

