#!/bin/bash

# ================================
#    SETTINGS & INITIAL SETUP
# ================================
STORE_DIR="stored_csv"
ACTIVITY_LOG="activity.log"

# Create the archive directory if it doesn't already exist
if [ ! -d "$STORE_DIR" ]; then
    mkdir -p "$STORE_DIR"
    echo "$(date '+%Y-%m-%d %H:%M:%S') - Folder created: $STORE_DIR" >> "$ACTIVITY_LOG"
fi


# ================================
#     SCAN FOR CSV FILES
# ================================
# Look for all .csv files in the current folder
find . -maxdepth 1 -type f -name "*.csv" | while read -r file; do

    NAME=$(basename "$file")

    # Safety check: avoid touching the log file if named .csv (rare)
    if [[ "$NAME" == "$ACTIVITY_LOG" ]]; then
        continue
    fi


    # ================================
    #     PROCESS & RENAME FILE
    # ================================
    STAMP=$(date '+%Y%m%d_%H%M%S')

    # Get filename without extension
    BASE="${NAME%.csv}"

    # New archived filename
    RENAMED="${BASE}_${STAMP}.csv"

    # Write a section in the log describing the operation
    {
        echo
        echo "-----------------------------------------------"
        echo "$(date '+%Y-%m-%d %H:%M:%S') - Processing: $NAME"
        echo "Renamed To: $RENAMED"
        echo "File Preview:"
        cat "$NAME"
        echo "-----------------------------------------------"
    } >> "$ACTIVITY_LOG"


    # Move the CSV into the archive folder with its new timestamped name
    mv "$NAME" "$STORE_DIR/$RENAMED"
    echo "Moved $NAME → $STORE_DIR/$RENAMED"

done


# ================================
#    COMPLETION NOTICE
# ================================
echo "$(date '+%Y-%m-%d %H:%M
