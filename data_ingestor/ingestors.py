import pandas as pd
from .decorators import timer, validate_dataframe
from .base import FileIngestor


class CSVIngestor(FileIngestor):
    #def __init__(self, filepath, file_format):
	#	super().__init__(filepath, file_format)
	#If the child __init__ does nothing except call super(), don't define it at all. Python calls the parent __init__ automatically. Only override __init__ when you're adding something new.
    @validate_dataframe
    @timer
    def read(self):
        print(f"Reading CSV file from {self.filepath}.")
        return pd.read_csv(self.filepath)
    


class JSONIngestor(FileIngestor):
     
    @validate_dataframe
    @timer
    def read(self):
        df = pd.read_json(self.filepath)
        return df
		
class ParquetIngestor(FileIngestor):
    @validate_dataframe
    @timer
    def read(self):
        df = pd.read_parquet(self.filepath)
        return df



	
