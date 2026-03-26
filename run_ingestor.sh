#!/bin/bash

set -e
set -u
set -o pipefail

# Check argument was passed
if [ -z "$1" ]; then
    echo "Error: No folder path provided."
    echo "Usage: bash run_pipeline.sh /path/to/data"
    exit 1
fi

FOLDER=$1

# Check folder exists
if [ ! -d "$FOLDER" ]; then
    echo "Error: Folder $FOLDER does not exist."
    exit 1
fi

echo "Running ingestor on $FOLDER..."
echo "Pipeline started at $(date)"
python -m data_ingestor.main "$FOLDER"
echo "Pipeline complete at $(date)"