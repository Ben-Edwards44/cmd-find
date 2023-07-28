#!/usr/bin/env bash

echo "Building JSON file..."

chmod +x help.sh

python3 create_json.py
python3 add_embeddings.py

echo "JSON file built"