from .factory import get_ingestor
from .context import managed_ingestor
from pathlib import Path



def read_multiple_files(filepaths: list):
	for filepath in filepaths:
		#yield from read_in_chunks(filepath)   - can't call a method like this, it is not a normal function
		ingestor = get_ingestor(filepath)
		yield from ingestor.read_in_chunks()

def scan_and_ingest(folder: str):
	dfs = []
	extensions = {'.csv', '.json', '.parquet'}
	filepaths = [str(p) for p in Path(folder).rglob("*") if p.suffix.lower() in extensions]
	for path in filepaths:
		with managed_ingestor(path) as ingestor:
			ingested_data = ingestor.read()
			dfs.append(ingested_data)
	return dfs
