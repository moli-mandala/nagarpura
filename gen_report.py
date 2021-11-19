import pandas as pd
import numpy as np
import os

LIST_OF_STATE_CODES=["tn", "kl", "ka", "ap", "mh", "mp", "ch", "jk", "up", "bi", "gu", "ra", "wb", "uk", "ha", "od", "cd", "pud", "sik", "tri", "nag", "miz", "meg", "ma", "go", "del", "arp", "as"]

#LIST_OF_FILTERS_ENDSWITH = ["palli", "vali", "valli", "oor", "ur", "ceri", "eri", "turai", "porai", "kadu", "malai", "mala", "pakkam", "kunru", "gund", "kund", "khond", "aru", "kanam", "nad", "seri", "sirai", "mani", "arai", "koli", "param", "halli", "vaadi", "vadi", "nigade", "kulam", "karanai", "kode", "kal", "karai", "vil", "bhil", "nadu", "pattanam", "talai", "gunda", "konda", "wali", "wari", "oli", "kere", "kuppa", "kuppam", "patti", "padi", "adka", "kote", "kudi", "kottai", "pattinam", "uru", "palle", "bali", "balli", "hatti", "halle", "pat", "pati", "gotti", "sarai" ]
LIST_OF_FILTERS_ENDSWITH = [ "pat"]
LIST_OF_FILTERS_STARTSWITH = [""]
LIST_OF_FILTERS_CONTAINS = [""]
consolidate_files = True

for filter in LIST_OF_FILTERS_ENDSWITH:
    out_csv_raw_file_dir="auto_reports/" + filter + "/raw/"
    out_csv_file_dir="auto_reports/" + filter + "/"
    # create direectory if doesn't exist
    if not os.path.exists(out_csv_raw_file_dir):
        os.makedirs(out_csv_raw_file_dir)

    out_file_path_list = {}
    for STATE_CODE in LIST_OF_STATE_CODES:
        in_csv_file_path="raw/" + STATE_CODE + ".csv"
        # read input file
        df = pd.read_csv(in_csv_file_path)

        # remove -pur from results if filter suffix is -ur
        if filter == "ur":
            ur_df = df[df['Name'].str.endswith(filter)]
            filter_df = ur_df[~ur_df['Name'].str.endswith(('pur', 'Pur'))]
        else:
            filter_df = df[df['Name'].str.endswith(filter)]
        
        print("number of matches for filter '" + filter + "' in state '" + STATE_CODE + "': " + str(len(filter_df)))
        # out_file_path = out_csv_raw_file_dir + filter + "_" + STATE_CODE + "_" + str(len(filter_df)) +".csv"
        # out_file_path_list[out_file_path] = str(len(filter_df))
        # filter_df.to_csv(out_file_path, index=False)
        group_dfs = np.split(filter_df, range(1997, len(filter_df), 1997))
        for idx, out_df in enumerate(group_dfs):
            out_file_path = out_csv_raw_file_dir + filter + "_" + STATE_CODE + "_" + str(idx) + "_" + str(len(out_df)) +".csv"
            out_file_path_list[out_file_path] = str(len(filter_df))
            out_df.to_csv(out_file_path, index=False)
    print("************collating****************")
    # print(out_file_path_list)
    # if consolidate_files is True:
    #     num_of_files = 0
    #     is_append = True
    #     num_of_rows = 0
    #     for key, value in out_file_path_list.items():
    #         print("processing '" + key + "'")

    #         df = pd.read_csv(key)
    #         out_result_file_path = out_csv_file_dir  + filter + "_" + num_of_files + ".csv"

    #         if value > 1999:
    #             group_dfs = np.split(df, range(1998, len(df), 1998))
    #             for idx, out_df in enumerate(group_dfs):
    #                 if is_append is False:
    #                     df.to_csv(out_result_file_path, index=False)
    #                 else:
    #                     df.to_csv(out_result_file_path, index=False, mode="a", header=False)
    #         else:
    #             num_of_rows = num_of_rows + value
    #             if num_of_rows > 1999:
    #                 lines_to_write = num_of_rows - 1999
    #             else:
    #                 if is_append is False:
    #                         df.to_csv(out_result_file_path, index=False)
    #                 else:
    #                     df.to_csv(out_result_file_path, index=False, mode="a", header=False)


