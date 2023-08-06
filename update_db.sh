#!/bin/bash

# Update the database when a new 
# xassida is added
export DJANGO_SETTINGS_MODULE=xassida.production

processed=()

# git the list of midified files
modified_files=$(git diff --name-only)

echo "changed files: $modified_files"
for xassida in $modified_files
do
  if [[ $xassida == xassidas/**/*.txt ]]; then
    name=$( echo $xassida | cut -f 4 -d '/'  )
    author=$( echo $xassida | cut -f 3 -d '/'  )
    echo "[Updating...] $author --> $name"
    if [[ " ${processed[@]} " =~ " $name " ]]; then
      echo "Skipping duplicate xassida $name"
    else
      ../venv/bin/python parse_xassida.py -x $name
      ../venv/bin/python parse_translations.py -x $name
      ../venv/bin/python parse_author.py -a $author
      cd ../utils/db
      ../../venv/bin/python insert.py -x $name
      echo "Processed xassida $name"
      processed+=("$name")
    fi
  fi
done;

