#!/usr/bin/env bash
VENV_PATH=".venv"
if [ ! -d "$VENV_PATH" ]; then
  python3 -m venv "$VENV_PATH"
fi
"$VENV_PATH/bin/python" -m pip install --upgrade pip
"$VENV_PATH/bin/python" -m pip install -r requirements.txt
echo "Installed requirements into $VENV_PATH"
