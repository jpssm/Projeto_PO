import pandas as pd

data_frame = pd.read_excel("Produção_custo.xlsx", sheet_name= "Quantidade produzida (Tonela...")

data_frame = data_frame.drop(index=range(0, 32))
data_frame = data_frame.drop(columns=data_frame.columns[0:2])

data_frame.to_csv("custo_de_produção.csv")