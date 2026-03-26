# main.py is an entry point, not a library module. Entry points should use absolute imports:
from pathlib import Path
from data_ingestor.context import managed_ingestor
from data_ingestor.utils import scan_and_ingest

if __name__ == "__main__":
    # Dynamically locate data.csv relative to this script's directory
    script_dir = Path(__file__).parent
    dfs = scan_and_ingest(str(script_dir))
    print(f"Ingested {len(dfs)} dataframes from {script_dir}.")