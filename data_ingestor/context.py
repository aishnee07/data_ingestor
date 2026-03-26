from .factory import get_ingestor
from contextlib import contextmanager

@contextmanager
def managed_ingestor(filepath):
	ingestor = get_ingestor(filepath)
	print(f"Starting ingestion for {filepath}")
	try:
		yield ingestor
	except Exception as e:
		print(f"Ingestion failed: {e}")
		raise   # re-raise it so it propagates
	finally:
		print(f"Ingestion complete for {filepath}")