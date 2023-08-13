import pandas as pd 
import numpy as np 


class FileOrganizer:
    def __init__(self, type, file, file_key):
        self.type = type
        self.file = file
        self.file_key = file_key
        self.valid_csv_File1_cols = ['id','Date','Ensemble','Licence','Ensemble Area','EID','Transmitter Area',
                                    'Site','Freq.','Block','TII Main Id (Hex)','TII Sub Id (Hex)',
                                    'Serv Label1 ','SId 1 (Hex)','LSN 1 (Hex)',
                                    'Serv Label2 ','SId 2 (Hex)','LSN 2 (Hex)',
                                    'Serv Label3 ','SId 3 (Hex)','LSN 3 (Hex)',
                                    'Serv Label4 ','SId 4 (Hex)','LSN 4 (Hex)',
                                    'Serv Label5 ','SId 5 (Hex)','LSN 5 (Hex)',
                                    'Serv Label6 ','SId 6 (Hex)','LSN 6 (Hex)',
                                    'Serv Label7 ','SId 7 (Hex)','LSN 7 (Hex)',
                                    'Serv Label8 ','SId 8 (Hex)','LSN 8 (Hex)',
                                    'Serv Label9 ','SId 9 (Hex)','LSN 9 (Hex)',
                                    'Serv Label10 ','SId 10 (Hex)','LSN 10 (Hex)',
                                    'Serv Label11 ','SId 11 (Hex)','LSN 11 (Hex)',
                                    'Serv Label12 ','SId 12 (Hex)','LSN 12 (Hex)',
                                    'Serv Label13 ','SId 13 (Hex)','LSN 13 (Hex)',
                                    'Serv Label14 ','SId 14 (Hex)','LSN 14 (Hex)',
                                    'Serv Label15 ','SId 15 (Hex)','LSN 15 (Hex)',
                                    'Serv Label16 ','SId 16 (Hex)','LSN 16 (Hex)',
                                    'Serv Label17 ','SId 17 (Hex)','LSN 17 (Hex)',
                                    'Serv Label18 ','SId 18 (Hex)','LSN 18 (Hex)',
                                    'Serv Label19 ','SId 19 (Hex)','LSN 19 (Hex)',
                                    'Serv Label20 ','SId 20 (Hex)','LSN 20 (Hex)',
                                    'Serv Label21 ','SId 21 (Hex)','LSN 21 (Hex)',
                                    'Serv Label22 ','SId 22 (Hex)','LSN 22 (Hex)',
                                    'Serv Label23 ','SId 23 (Hex)','LSN 23 (Hex)',
                                    'Serv Label24 ','SId 24 (Hex)','LSN 24 (Hex)',
                                    'Serv Label25 ','SId 25 (Hex)','LSN 25 (Hex)',
                                    'Serv Label26 ','SId 26 (Hex)','LSN 26 (Hex)',
                                    'Serv Label27 ','SId 27 (Hex)','LSN 27 (Hex)',
                                    'Serv Label28 ','SId 28 (Hex)','LSN 28 (Hex)',
                                    'Serv Label29 ','SId 29 (Hex)','LSN 29 (Hex)',
                                    'Serv Label30 ','SId 30 (Hex)','LSN 30 (Hex)',
                                    'Serv Label31 ','SId 31 (Hex)','LSN 31 (Hex)',
                                    'Serv Label32 ','SId 32 (Hex)','LSN 32 (Hex)',
                                    'Data Serv Label1','Data SId 1 (Hex)',
                                    'Data Serv Label2','Data SId 2 (Hex)',
                                    'Data Serv Label3','Data SId 3 (Hex)',
                                    'Data Serv Label4','Data SId 4 (Hex)',
                                    'Data Serv Label5','Data SId 5 (Hex)',
                                    'Data Serv Label6','Data SId 6 (Hex)',
                                    'Data Serv Label7','Data SId 7 (Hex)',
                                    'Data Serv Label8','Data SId 8 (Hex)',
                                    'Data Serv Label9','Data SId 9 (Hex)',
                                    'Data Serv Label10','Data SId 10 (Hex)',
                                    'Data Serv Label11','Data SId 11 (Hex)',
                                    'Data Serv Label12','Data SId 12 (Hex)',
                                    'Data Serv Label13','Data SId 13 (Hex)',
                                    'Data Serv Label14','Data SId 14 (Hex)',
                                    'Data Serv Label15','Data SId 15 (Hex)'
                                    ]
        

        self.valid_csv_File2_cols = ['id','NGR','Longitude/Latitude',
                                        'Site Height','In-Use Ae Ht','In-Use ERP Total','Dir Max ERP',
                                        '0','10','20','30','40','50','60','70','80','90',
                                        '100','110','120','130','140','150','160','170','180','190',
                                        '200','210','220','230','240','250','260','270','280','290',
                                        '300','310','320','330','340','350','Lat','Long'
                                        ]
    

        self.valid_json_File1_cols = ['ID', 'Date', 'Ensemble ID ', 'Transmitter Area', 
                                'Site', 'Frequency', 'Block', 
                                'TII Main ID', 'TII Sub ID']

        #valid_json_File1_cols =['ID','Ensemble','Licence','Ensemble Area', 'EID', 
                            #'Transmitter Area', 'Site' 'Frequency', 'Services', 
                            # 'Data Services']

        self.valid_json_File2_cols = ['ID','NGR','Longitude/Latitude',
                            'Site Height','In-Use Ae Ht', 
                            'In-Use ERP Total', 'Azimuth Degrees', 'Dir Max ERP']
        
        #valid_json_File2_cols = ['ID','NGR','Longitude/Latitude',
                            #'Site Height','Aerial Height(m)', 
                            #'Power(kW)', 'Azimuth Degrees']

        self.message = ''

    
    def file_processer(self):
        if self.type =='JSON':
            json_file = self.json_opener()
            print(f'El archivo es {self.validate_json_file(json_file)}')
            if self.validate_json_file(json_file):
                self.message =f'{self.file_key} has been uploaded as a {self.type} type file'
                return json_file
            else:
                self.message =f'Invalid {self.file_key}. Please check the file'
            
        elif self.type == 'CSV':
            csv_file = self.csv_opener()
            print(f'El archivo es {self.validate_csv_file(csv_file)}')
            if self.validate_csv_file(csv_file):
                self.message =f'{self.file_key} has been uploaded as a {self.type} type file'
                return csv_file
            else:
                self.message =f'Invalid {self.file_key}. Please check the file'
        
        else:
            self.message = f'Invalid File. Please check the file'


    def get_message(self):
        return self.message


    def json_opener(self):
        df = pd.read_json(self.file, encoding='latin-1', na_values = np.nan)
        return df


    def csv_opener(self):
        df = pd.read_csv(self.file, encoding='latin-1', na_values = np.nan)
        return df

    
    def validate_csv_file(self, csv_file):
        valid_column_headers =[]
        if self.file_key == 'ParametersDAB':
            valid_column_headers = self.valid_csv_File1_cols
        
        elif self.file_key == 'AntennaDAB':
            valid_column_headers = self.valid_csv_File2_cols

        if not all(col in csv_file.columns for col in valid_column_headers):
            return False
        else:
            return True


    def validate_json_file(self, json_file):
        valid_keys = []
        if self.file_key == 'ParametersDAB':
            valid_keys = self.valid_json_File1_cols

        elif self.file_key == 'AntennaDAB':
            valid_keys = self.valid_json_File2_cols
        
        for unique_id, parameters in json_file.items():
            if not all(key in parameters for key in valid_keys):
                print(f"Invalid keys in the JSON object with ID {unique_id}")
                return False
            else:
               
                return True
               
      