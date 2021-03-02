import pandas as pd


def concat_files(csv1, csv2, csv_path):
    """csv1 and csv2 are path of csv files.
    Function takes csv paths, concat them together, drop duplicates and
    write it as a new csv file.
    """
    df_1 = pd.read_csv(csv1, lineterminator="\n")
    df_2 = pd.read_csv(csv2, lineterminator="\n")
    df_concat = pd.concat([df_1, df_2], ignore_index=True)
    df_concat.drop_duplicates(subset=['id'], inplace=True, ignore_index=True)
    df_concat.to_csv(csv_path + ".csv")
