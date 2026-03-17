#!/usr/bin/env bash
set -e

echo "[1/3] Django system check..."
python manage.py check

echo "[2/3] Syntax lint (compileall)..."
python -m compileall apps config common

echo "[3/3] Running test suite..."
python manage.py test

echo "Backend verification completed."