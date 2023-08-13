import pandas as pd
import numpy as np

def setting_indexes(df, index_name):
    #Setting correct indexes
    return df.set_index(index_name)
   
def switch_columns(df, column_A, column_B):
    cols = list(df.columns)
    index_A = cols.index(column_A)
    index_B = cols.index(column_B)
    cols[index_A], cols[index_B]  = cols[index_B], cols[index_A] 
    df[cols]
    return df

def convert_to_float(df, col_name):
    df[col_name] = df[col_name].replace(np.nan, '0')
    df[col_name] = df[col_name].str.replace('.', '')
    df[col_name] = df[col_name].str.replace(',', '.').astype(float)
    return df