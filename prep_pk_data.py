import pandas as pd

IN_FILE_PATH=r'raw/pk_raw.csv'
OUT_FILE_PATH_PREFIX=r'raw/pk.csv'

df = pd.read_csv(IN_FILE_PATH, low_memory=False)
df.columns = df.columns.str.replace(' ', '')
cols = ["name","asciiname","alternatenames","latitude","longitude"]
df = df[["name","asciiname","alternatenames","latitude","longitude"]]
df.to_csv(OUT_FILE_PATH_PREFIX, index=False)