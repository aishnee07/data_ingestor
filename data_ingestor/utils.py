from ingestors import FileIngestor ,CSVIngestor, JSONIngestor, ParquetIngestor 


# factory function - a function that creates and returns new objects or values, abstracting the creation logic away from the client code. Instead of using a direct constructor call (e.g., calling a class with ()), the client calls the factory function, which then determines which specific type of object to create based on certain conditions or inputs.
def get_ingestor(filepath: str) -> FileIngestor:
	if filepath.endswith(".csv"):
		return CSVIngestor(filepath, "csv")
	elif filepath.endswith(".json"):
		return JSONIngestor(filepath, "json")
	elif filepath.endswith(".parquet"):
		return ParquetIngestor(filepath, "parquet")
	else:
		raise ValueError(f"Unsupported file format for file: {filepath}")
