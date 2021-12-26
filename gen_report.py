import pandas as pd
import numpy as np
import os

LIST_OF_STATE_CODES=["tn", "kl", "ka", "ap", "mh", "mp", "ch", "jk", "up", "bi", "gu", "ra", "wb", "uk", "ha", "od", "cd", "pud", "sik", "tri", "nag", "miz", "meg", "ma", "go", "del", "arp", "as", "pu", "jka", "hp"]
#LIST_OF_STATE_CODES=["pu" ]

#LIST_OF_FILTERS_ENDSWITH = ["palli", "vali", "valli", "oor", "ur", "ceri", "eri", "turai", "porai", "kadu", "malai", "mala", "pakkam", "kunru", "gund", "kund", "khond", "aru", "kanam", "nad", "seri", "sirai", "mani", "arai", "koli", "param", "halli", "vaadi", "vadi", "nigade", "kulam", "karanai", "kode", "kal", "karai", "vil", "bhil", "nadu", "pattanam", "talai", "gunda", "konda", "wali", "wari", "oli", "kere", "kuppa", "kuppam", "patti", "padi", "adka", "kote", "kudi", "kottai", "pattinam", "uru", "palle", "bali", "balli", "hatti", "halle", "pat", "pati", "gotti", "sarai" ]
LIST_OF_FILTERS_ENDSWITH = ["kottai", "kotta", "kot", "kote", "kota", "got", "gote", "gotta", "Kottai", "Kotta", "Kot", "Kote", "Kota", "Got", "Gote", "Gotta", "koti", "kottam", "Koti", "kotla", "Kotla", "kudda", "kutta", "kuta", "gottai", "Gottai", "patti", "Patti", "hatti", "Hatti", "padu", "Padu", "bhatti", "Bhatti", "patte", "Patte", "karai", "Karai", "kulam", "palliru", "gudi", "koppa", "koppal", "Koppa", "kadu", "nad", "nadu", "padi", "Padi", "male", "Male", "gutta", "gudde", "Gutta", "kodu", "porai", "kare", "Kare", "kola", "Kola", "kona", "Kona", "kunda", "Kunda", "kunte", "Kunte", "konda", "Konda", "ur", "palli", "vali", "valli", "Halli", "Palli", "oor", "ur", "ceri", "eri", "turai", "porai", "kadu", "malai", "mala",  "pakkam", "kunru", "gund", "kund", "khond", "aru", "kanam", "nad", "seri", "sirai", "mani", "arai", "param", "halli", "Halli", "vaadi", "vadi", "karanai", "kode", "kal", "karai", "vil", "bhil", "nadu", "pattanam", "talai", "gunda", "konda", "kere", "kuppa", "kuppam", "patti", "padi", "adka", "kote", "kudi", "kottai", "pattinam", "uru", "palle", "bali", "balli", "halle", "pat", "pati", "gotti", "pali", "Pali", "Bali", "Vadi","oli", "uli" ]
#LIST_OF_FILTERS_ENDSWITH = ["patti", "Patti", "hatti", "Hatti", "padu", "Padu", "bhatti", "Bhatti", "patte", "Patte"] 
LIST_OF_FILTERS_STARTSWITH = [""]
LIST_OF_FILTERS_CONTAINS = [""]
consolidate_files = True

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
"g_kottai" : [ "kottai", "kotta", "kote", "kot", "kota", "koda", "gote", "Kottai", "Kotta", "Kote", "Kot", "Kota", "Koda", "Gote" ],
"g_valli" : [ "valli", "balli", "vali", "oli", "bali", "Valli", "Balli", "Vali", "Oli", "Bali" ],
"g_oor" : [ "ur", "oor", "Ur", "Oor" ]
}

INDO_ARYAN_SUFFIXES = {
"g_pur" : [ "pur", "pora", "puri", "puram", "pura", "Pura", "Pur", "pora", "Puri", "Puram" ],
"g_nagar" : [ ],
"g_abad" : [ "abad" ]
}

group_name = "go"
for suffix_group in INDO_ARYAN_SUFFIXES:
    print("procesing suffix group:" + suffix_group)
    
    for filter in INDO_ARYAN_SUFFIXES[suffix_group]:
        out_csv_file_dir="auto_reports/" + suffix_group + "/" + filter + "/"
        # create direectory if doesn't exist
        if not os.path.exists(out_csv_file_dir):
            os.makedirs(out_csv_file_dir)

        out_file_path_list = {}
        for STATE_CODE in LIST_OF_STATE_CODES:
            in_csv_file_path="raw/" + STATE_CODE + ".csv"
            # read input file
            df = pd.read_csv(in_csv_file_path)

            # remove -pur from results if filter suffix is -ur
            if filter == "ur":
                ur_df = df[df['Name'].str.endswith(filter, na=False)]
                filter_df = ur_df[~ur_df['Name'].str.endswith(('pur', 'Pur'), na=False)]
            else:
                filter_df = df[df['Name'].str.endswith(filter, na=False)]
            
            print("number of matches for filter '" + filter + "' in state '" + STATE_CODE + "': " + str(len(filter_df)))
            # out_file_path = out_csv_raw_file_dir + filter + "_" + STATE_CODE + "_" + str(len(filter_df)) +".csv"
            # out_file_path_list[out_file_path] = str(len(filter_df))
            # filter_df.to_csv(out_file_path, index=False)
            if len(filter_df) > 0:
                group_dfs = np.split(filter_df, range(1997, len(filter_df), 1997))
                for idx, out_df in enumerate(group_dfs):
                    out_file_path = out_csv_file_dir + filter + "_" + STATE_CODE + "_" + str(idx) + "_" + str(len(out_df)) +".csv"
                    out_file_path_list[out_file_path] = str(len(filter_df))
                    out_df.to_csv(out_file_path, index=False)
