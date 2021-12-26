import csv
import json

import pandas as pd
import numpy as np
import os

STATE_CODE = "pk"
CSV_FILE_PATH="raw/" + STATE_CODE + ".csv"
OUT_FILE_PATH_SUFFIX_DIR="processed/" + STATE_CODE + "/dr_suf/"
OUT_FILE_PATH_PREFIX_DIR="processed/" + STATE_CODE + "/dr_pre/"

DRAVIDIAN_PREFIXES = [ "Vanji", "Thondi", "Gorkai", "Patti", "Karakai", "Amur", "Sonpatti", "Kallur", "Gorkhai", "Cheri", "Seri", "Kandikai", "Kudam", "Kutta", "Tonri", "Tondi", "Kodi", "Kodu", "Koil", "Selle", "Celli", "Pali", "Palai", "Kari", "Wanni", "Malli", "Malla", "Mala", "Nalli", "Kalur", "Kadai", "Iday", "Konkar", "Kosar", "Puli", "Yanai", "Korran", "Kallar", "Kott", "Kot", "Pugal", "Kulam", "Kolam", "Khand", "Kant", "Murug", "Kadam", "Bali"]

DRAVIDIAN_SUFFIXES = {
"g_palli" : [ "palli","pali","halli","pallika","palliya","palle", "Palli", "Pali", "Halli", "Pallika", "Palliya", "Palle" ],
"g_patti" : [ "patti", "pattam", "hatti", "pattu", "padu", "Patti", "Pattam", "Hatti", "Pattu", "Padu" ],
"g_kudi" : [ "kudi", "kodika", "kurma", "gudi", "guddi", "Kudi", "Kodika", "Kurma", "Gudi", "Guddi" ],
"g_kuppam" : [ "kuppam", "kumpai", "koppa", "kupamu", "kumbu", "kumba", "Kuppam", "Kumpai", "Koppa", "Kupamu", "Kumbu", "Kumba" ],
"g_nadu" : [ "natu", "nadu", "nandu", "nat", "naru", "nar", "nay", "Natu", "Nadu", "Nandu", "Nat", "Naru", "Nar", "Nay" ],
"g_mantai" : [ "mantai", "mandi", "manru", "Mantai", "Mandi", "Manru" ],
"g_kuntru" : [ "kuntu", "kuntram", "kunnam", "kunnu", "konda", "konra", "kod", "kode", "goda", "gode", "godi", "goron", "gudda", "gutta", "gudde", "guddamu", "gude", "gudri", "guti", "gudiya", "Kuntu", "Kuntram", "Kunnam", "Kunnu", "Konda", "Konra", "Kod", "Kode", "Goda", "Gode", "Godi", "Goron", "Gudda", "Gutta", "Gudde", "Guddamu", "Gude", "Gudri", "Guti", "Gudiya" ],
"g_kottakai" : [ "kottakai", "kottam", "kottil", "kotti", "kotta", "kotya", "korka", "kotam", "kurka", "kotorla", "kotorli", "kota", "Kottakai", "Kottam", "Kottil", "Kotti", "Kotta", "Kotya", "Korka", "Kotam", "Kurka", "Kotorla", "Kotorli", "Kota" ],
"g_malai" : [ "malai", "mala", "male", "mare", "Malai", "Mala", "Male", "Mare" ],
"g_kodi" : [ "kotu", "koti", "kodu", "Kotu", "Koti", "Kodu", "Kodi" ],
"g_kere" : [ "cira", "kire", "kere", "ceruvu", "Cira", "Kire", "Kere", "Ceruvu" ],
"g_porai" : [ "porai", "porrai", "pode", "parro", "parta", "Porai", "Porrai", "Pode", "Parro", "Parta" ],
"g_kulam" : [ "kulam", "kola", "kolanu", "kollu", "glunju", "Kulam", "Kola", "Kolanu", "Kollu", "Glunju" ],
"g_kottai" : [ "kottai", "kotta", "kote", "kot", "kota", "koda", "gote", "Kottai", "Kotta", "Kote", "Kot", "Kota", "Koda", "Gote" ]
}

INDO_ARYAN_SUFFIXES = {
#"g_pur" : [ "pur", "pora", "puri", "puram", "Pur", "pora", "Puri", "Puram" ],
#"g_nagar" : [ ]
}

if not os.path.exists(OUT_FILE_PATH_SUFFIX_DIR):
    os.makedirs(OUT_FILE_PATH_SUFFIX_DIR)
if not os.path.exists(OUT_FILE_PATH_PREFIX_DIR):
    os.makedirs(OUT_FILE_PATH_PREFIX_DIR)

df = pd.read_csv(CSV_FILE_PATH)
for suffix_group in DRAVIDIAN_SUFFIXES:
    print("procesing suffix group:" + suffix_group)

    for filter in DRAVIDIAN_SUFFIXES[suffix_group]:
        if filter == "ur":
            ur_df = df[df['name'].str.endswith(filter)]
            pur_df = ur_df[~ur_df['name'].str.endswith('pur')]
            kaur_df = pur_df[~pur_df['name'].str.endswith('Kaur')]
            filter_df = kaur_df[~kaur_df['name'].str.endswith('Jhaur')]
        else:
            filter_df = df[df['name'].str.endswith(filter)]
        
        print(len(filter_df))
        if len(filter_df) > 0:
            group_dfs = np.split(filter_df, range(1997, len(filter_df), 1997))
            for idx, out_df in enumerate(group_dfs):
                out_file_path = OUT_FILE_PATH_SUFFIX_DIR + STATE_CODE + "_" + filter + "_" + str(idx) + "_" + str(len(out_df)) + ".csv"
                out_df.to_csv(out_file_path, index=False)

for filter in DRAVIDIAN_PREFIXES:
    filter_df = df[df['name'].str.startswith(filter)]
    
    print(len(filter_df))
    if len(filter_df) > 0:
        group_dfs = np.split(filter_df, range(1997, len(filter_df), 1997))
        for idx, out_df in enumerate(group_dfs):
            out_file_path = OUT_FILE_PATH_PREFIX_DIR + STATE_CODE + "_" + filter + "_" + str(idx) + "_" + str(len(out_df))+".csv"
            out_df.to_csv(out_file_path, index=False)