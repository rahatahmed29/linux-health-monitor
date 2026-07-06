#!/bin/bash

echo "=================================="
echo " Linux Hqealth Monitor"
echo "=================================="

source .venv/bin/activate

python app/main.py

echo
echo "Monitoring completed successfully."