import pandas as pd
from abc import ABC, abstractmethod
from decorators import timer, validate_dataframe

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

# ingestor = FileIngestor("data.csv", "csv")  # Python considers FileIngestor to be an incomplete blueprint due to the abstract method read(), and thus raises a TypeError when you try to instantiate it.

