import pandas as pd
from abc import ABC, abstractmethod
from decorators import timer, validate_dataframe
from contextlib import contextmanager
from pathlib import Path

# class to ingest data from files
class FileIngestor(ABC):
    def __init__(self, filepath, file_format):
        self.filepath = filepath
        self.file_format = file_format

    def __repr__(self):
        return f"Data Ingestor: filepath='{self.filepath!r}', file_format='{self.file_format!r}')"
    
    # instance method to read file
    # In Python, if a class inherits from ABC and has even one method decorated with @abstractmethod, Python will prevent you from creating an instance of that class until that method is overridden.
    @abstractmethod
    def read(self):
        pass 
        # print(f"Reading {self.file_format} file from {self.filepath}.") # - overriding in child class 


    # A static method is a function defined within a class that belongs to the class itself rather than a specific object instance. They are called directly using the class name, allowing utility or helper functions to run without instantiating the object, and cannot directly access non-static instance variables. cls.method_name()  - can be called like this.
    @staticmethod
    def validate_extension(filepath):
        valid_extensions = ['.csv', '.json', '.parquet']
        return any(filepath.endswith(ext) for ext in valid_extensions)
    

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


@contextmanager
def managed_ingestor(filepath):
	from utils import get_ingestor
	ingestor = get_ingestor(filepath)
	print(f"Starting ingestion for {filepath}")
	try:
		yield ingestor
	except Exception as e:
		print(f"Ingestion failed: {e}")
		raise   # re-raise it so it propagates
	finally:
		print(f"Ingestion complete for {filepath}")
		

if __name__ == "__main__":
	# Dynamically locate data.csv relative to this script's directory
	script_dir = Path(__file__).parent
	data_file = script_dir / "data.csv"
	
	if not data_file.exists():
		print(f"Error: data.csv not found at {data_file}")
		print(f"Script location: {script_dir}")
		exit(1)
	
	with managed_ingestor(str(data_file)) as ingestor:
		df = ingestor.read()


