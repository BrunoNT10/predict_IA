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

times = list(set(list(df['mandante'])))

print(anos)
print(times)

# for i, row in df.iterrows():
    
# for i, row in df.iterrows():
#     if not row.vencedor == "-":
#         print(f"{row.mandante} x {row.visitante} - vencedor: {row.vencedor}")
    


df.to_csv("updated_pontuation.csv")