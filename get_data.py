# %%
import pandas as pd
import numpy as np


# %%
df = pd.read_csv('updated_pontuation.csv')

column_round = df.rodata
column_mand = df.mandante
column_visit = df.visitante
column_pont_mand = df.pont_mandante
column_pont_visit = df.pont_visitante
column_vencedor = df.vencedor

list_teams = sorted(list(set(list(column_mand))))

index = 0
for team in list_teams:
    for i, row in df.iterrows():
        if row.mandante == team:
            df.at[i, 'mandante'] = index
            if row.vencedor == team:
                df.at[i, 'vencedor'] = 1
                
        if row.visitante == team:
            df.at[i, 'visitante'] = index
            if row.vencedor == team:
                df.at[i, 'vencedor'] = 2
        # if row.vencedor == team:
            
        if row.vencedor == "-":
            df.at[i, 'vencedor'] = 0
            
            
        
    index += 1


df = df.drop(columns=[
    'ID', 'data', 'hora', 'formacao_mandante', 'formacao_visitante', 'tecnico_mandante', 'tecnico_visitante',
    'arena', 'mandante_Placar', 'visitante_Placar', 'mandante_Estado', 'visitante_Estado'
])

df.to_excel("translated.xlsx")
