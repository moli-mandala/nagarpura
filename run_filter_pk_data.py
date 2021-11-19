import csv
import json

import pyparsing as pp
import pandas as pd
import numpy as np
import os

STATE_CODE = "pk"
CSV_FILE_PATH="raw/" + STATE_CODE + ".csv"
OUT_FILE_PATH_SUFFIX_DIR="processed/" + STATE_CODE + "/dr_suf/"
OUT_FILE_PATH_PREFIX_DIR="processed/" + STATE_CODE + "/dr_pre/"
LIST_OF_FILTERS_ENDSWITH = ["palli", "vali", "valli", "oor", "ur", "ceri", "eri", "turai", "porai", "kadu", "malai", "mala", "pakkam", "kunru", "gund", "kund", "khond", "aru", "kanam", "nad", "seri", "sirai", "mani", "arai", "koli", "param", "halli", "vaadi", "vadi", "nigade", "kulam", "karanai", "kode", "kal", "karai", "vil", "bhil", "nadu", "pattanam", "talai", "gunda", "konda", "wali", "wari", "oli", "kere", "kuppa", "kuppam", "patti", "padi", "adka", "kote", "kudi", "kottai", "pattinam", "uru", "palle", "bali", "balli", "hatti", "halle", "pat", "pati", "gotti", "sarai" ]
LIST_OF_FILTERS_STARTSWITH = ["Vanji", "Thondi", "Gorkai", "Patti", "Karakai", "Amur", "Sonpatti", "Kallur", "Gorkhai", "Cheri", "Seri", "Kandikai", "Kudam", "Kutta", "Tonri", "Tondi", "Kodi", "Kodu", "Koil", "Selle", "Celli", "Pali", "Palai", "Kari", "Wanni", "Malli", "Malla", "Mala", "Nalli", "Kalur", "Kadai", "Iday", "Konkar", "Kosar", "Puli", "Yanai", "Korran"]
LIST_OF_FILTERS_CONTAINS = [ ]



if not os.path.exists(OUT_FILE_PATH_SUFFIX_DIR):
    os.makedirs(OUT_FILE_PATH_SUFFIX_DIR)
if not os.path.exists(OUT_FILE_PATH_PREFIX_DIR):
    os.makedirs(OUT_FILE_PATH_PREFIX_DIR)

df = pd.read_csv(CSV_FILE_PATH)
for filter in LIST_OF_FILTERS_ENDSWITH:
    if filter == "ur":
        ur_df = df[df['name'].str.endswith(filter)]
        pur_df = ur_df[~ur_df['name'].str.endswith('pur')]
        kaur_df = pur_df[~pur_df['name'].str.endswith('Kaur')]
        filter_df = kaur_df[~kaur_df['name'].str.endswith('Jhaur')]
    else:
        filter_df = df[df['name'].str.endswith(filter)]
    
    print(len(filter_df))
    group_dfs = np.split(filter_df, range(1997, len(filter_df), 1997))
    for idx, out_df in enumerate(group_dfs):
        out_file_path = OUT_FILE_PATH_SUFFIX_DIR + STATE_CODE + "_" + filter + "_" + str(idx) + "_" + str(len(out_df)) + ".csv"
        out_df.to_csv(out_file_path, index=False)

for filter in LIST_OF_FILTERS_STARTSWITH:
    filter_df = df[df['name'].str.startswith(filter)]
    
    print(len(filter_df))
    group_dfs = np.split(filter_df, range(1997, len(filter_df), 1997))
    for idx, out_df in enumerate(group_dfs):
        out_file_path = OUT_FILE_PATH_PREFIX_DIR + STATE_CODE + "_" + filter + "_" + str(idx) + "_" + str(len(out_df))+".csv"
        out_df.to_csv(out_file_path, index=False, mode='a', header=False)