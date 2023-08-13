   

from fileorganizer import FileOrganizer 
import utils as ut
from pathlib import Path

raw_files ={}
file_key = 'File1'
#file_key = 'File2'

#filename = "C:/Users/herms/Formative_Assignment/Data sets/TxAntennaDAB.csv"
#filename = "C:/Users/herms/Formative_Assignment/Data sets/TxParamsDAB.csv"
filename = "C:/Users/herms/Formative_Assignment/Antenna_data_JSON.json"
#filename = "C:/Users/herms/Formative_Assignment/Radio_Parameter_data_JSON.json"

route = Path(filename)
file_type = ut.check_file_format(route)
open_file = ut.load_file(route)
categorized_file = FileOrganizer(file_type,open_file)
raw_files[file_key] = categorized_file

for keys, value in raw_files.items():
    print(keys)
    print(value.type)
    print(value.file_processer())