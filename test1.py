import pandas as pd

df = pd.read_csv('aaa.csv')

print(df.to_string()) 


#df = pd.read_parquet("a.parquet")
#print(df.head())
#print(df.dtypes)