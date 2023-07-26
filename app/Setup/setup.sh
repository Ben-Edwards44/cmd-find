#!/usr/bin/env bash

echo "Setting up permissions..."

chmod +x help.sh

echo "Permissions setup"

echo "Building JSON file..."

python3 create_json.py
python3 add_embeddings.py

echo "JSON file built"

echo "Moving file..."

cp command_info.json ..
rm command_info.json

echo "File moved"
echo "Setup complete"