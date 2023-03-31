#! /usr/bin/env bash

pyenv local
poetry install
EXECUTABLE=$(poetry env info | awk '/Executable/ { print $2; exit }')
sed -i.bak "/<interpreter_path>/ s#<interpreter_path>#$EXECUTABLE#" \
  .vscode/settings.json
rm .vscode/settings.json.bak
git init
git add .
git commit -m "generate project with cookiecutter"