import csv
import json

import pyparsing as pp
import pandas as pd
import numpy as np
import os

LIST_OF_STATE_CODES=["tn", "kl", "ka", "ap", "mh", "mp", "ch", "jk", "up", "bi", "gu", "ra", "wb", "uk", "ha", "od", "cd", "pud", "sik", "tri", "nag", "miz", "meg", "ma", "go", "del", "arp", "as"]
#LIST_OF_STATE_CODES=["od"]
for STATE_CODE in LIST_OF_STATE_CODES:
    CSV_FILE_PATH="raw/" + STATE_CODE + ".csv"
    OUT_FILE_PATH_SUFFIX_DIR="processed/" + STATE_CODE + "/dr_suf/"
    OUT_FILE_PATH_PREFIX_DIR="processed/" + STATE_CODE + "/dr_pre/"
    LIST_OF_FILTERS_ENDSWITH = ["palli", "vali", "valli", "oor", "ur", "ceri", "eri", "turai", "porai", "kadu", "malai", "mala", "pakkam", "kunru", "gund", "kund", "khond", "aru", "kanam", "nad", "seri", "sirai", "mani", "arai", "koli", "param", "halli", "vaadi", "vadi", "nigade", "kulam", "karanai", "kode", "kal", "karai", "vil", "bhil", "nadu", "pattanam", "talai", "gunda", "konda", "wali", "wari", "oli", "kere", "kuppa", "kuppam", "patti", "padi", "adka", "kote", "kudi", "kottai", "pattinam", "uru", "palle", "bali", "balli", "hatti", "halle", "pat", "pati", "gotti", "sarai"]
    #LIST_OF_FILTERS_ENDSWITH = [ "ner" ]
    LIST_OF_FILTERS_STARTSWITH = ["Vanji", "Gorkai", "Thondi", "Madura"]
    LIST_OF_FILTERS_CONTAINS = []

    # create directorires
    if not os.path.exists(OUT_FILE_PATH_SUFFIX_DIR):
        os.makedirs(OUT_FILE_PATH_SUFFIX_DIR)
    if not os.path.exists(OUT_FILE_PATH_PREFIX_DIR):
        os.makedirs(OUT_FILE_PATH_PREFIX_DIR)

    df = pd.read_csv(CSV_FILE_PATH)
    for filter in LIST_OF_FILTERS_ENDSWITH:
        if filter == "ur":
            ur_df = df[df['Name'].str.endswith(filter)]
            filter_df = ur_df[~ur_df['Name'].str.endswith(('pur', 'Pur'))]
        else:
            filter_df = df[df['Name'].str.endswith(filter)]
        
        print(len(filter_df))
        group_dfs = np.split(filter_df, range(1997, len(filter_df), 1997))
        for idx, out_df in enumerate(group_dfs):
            out_file_path = OUT_FILE_PATH_SUFFIX_DIR + STATE_CODE + "_" + filter + "_" + str(idx) + "_" + str(len(out_df)) + ".csv"
            out_df.to_csv(out_file_path, index=False)

    for filter in LIST_OF_FILTERS_STARTSWITH:
        filter_df = df[df['Name'].str.startswith(filter)]
        
        print(len(filter_df))
        group_dfs = np.split(filter_df, range(1997, len(filter_df), 1997))
        for idx, out_df in enumerate(group_dfs):
            out_file_path = OUT_FILE_PATH_PREFIX_DIR + STATE_CODE + "_" + filter + "_" + str(idx) + "_" + str(len(out_df))+".csv"
            out_df.to_csv(out_file_path, index=False, mode='a', header=False)