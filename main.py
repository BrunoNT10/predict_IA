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

anos = list(set(list(df.data.apply(parse_year))))

times = list(set(list(df['mandante'])))

print(anos)
print(times)

# for i, row in df.iterrows():
    
# for i, row in df.iterrows():
#     if not row.vencedor == "-":
#         print(f"{row.mandante} x {row.visitante} - vencedor: {row.vencedor}")
    
#     else:
#         print(f"{row.mandante} x {row.visitante} - empate")
    
