import pandas as pd
import os

consolidate_files = True
RAW_REPORT_FILE_DIR = "auto_reports/"
OUT_DIR = "reports/"
# print(IN_FILE_DIR)
if consolidate_files is True:
    num_of_files = 0
    is_append = True
    num_of_rows = 0
    list_of_raw_report_dirs = os.walk(RAW_REPORT_FILE_DIR)
    for (dirpath, dirnames, filenames) in list_of_raw_report_dirs:
        for s_dir in dirnames:
            for (dirpath, s_dirnames, s_filenames) in os.walk(RAW_REPORT_FILE_DIR + "/" + s_dir):
                #print(s_filenames)
                for s_file in s_filenames:
                    print(s_file)
        
    # for key, value in out_file_path_list.items():
    #     print("processing '" + key + "'")

    #     df = pd.read_csv(key)
    #     out_result_file_path = out_csv_file_dir  + filter + "_" + num_of_files + ".csv"

    #     if value > 1999:
    #         group_dfs = np.split(df, range(1998, len(df), 1998))
    #         for idx, out_df in enumerate(group_dfs):
    #             if is_append is False:
    #                 df.to_csv(out_result_file_path, index=False)
    #             else:
    #                 df.to_csv(out_result_file_path, index=False, mode="a", header=False)
    #     else:
    #         num_of_rows = num_of_rows + value
    #         if num_of_rows > 1999:
    #             lines_to_write = num_of_rows - 1999
    #         else:
    #             if is_append is False:
    #                     df.to_csv(out_result_file_path, index=False)
    #             else:
    #                 df.to_csv(out_result_file_path, index=False, mode="a", header=False)