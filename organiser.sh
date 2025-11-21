#!/bin/bash

# Define the archive directory and log file [cite: 87, 84]
ARCHIVE_DIR="archive"
LOG_FILE="organizer.log"

# --- 1. Check/Create Archive Directory --- [cite: 87]
if [ ! -d "$ARCHIVE_DIR" ]; then
    mkdir -p "$ARCHIVE_DIR"
    echo "$(date '+%Y-%m-%d %H:%M:%S') - Created archive directory: $ARCHIVE_DIR" >> "$LOG_FILE"
fi

# --- 2. Find and Process CSVs --- [cite: 88]
# Find all files ending in .csv in the current directory
find . -maxdepth 1 -type f -name "*.csv" | while read -r filepath; do
    
    # Remove leading './' from filepath
    ORIGINAL_NAME=$(basename "$filepath")
    
    # Skip the log file itself if it's somehow incorrectly named with .csv
    if [[ "$ORIGINAL_NAME" == "$LOG_FILE" ]]; then
        continue
    fi
    
    # --- 3. Loop, Log, and Archive --- [cite: 89]

    # Generate Timestamp (e.g., 20251105-170000) [cite: 92]
    TIMESTAMP=$(date '+%Y%m%d-%H%M%S')
    
    # Define New Name: insert timestamp before the extension [cite: 93, 94]
    # Example: grades.csv becomes grades-20251105-170000.csv
    BASE_NAME=$(echo "$ORIGINAL_NAME" | sed 's/\(.*\)\(\.csv\)/\1/')
    NEW_NAME="${BASE_NAME}-${TIMESTAMP}.csv"
    
    # Log Action: Append archiving details to organizer.log [cite: 95]
    echo "" >> "$LOG_FILE"
    echo "==================================================" >> "$LOG_FILE"
    echo "$(date '+%Y-%m-%d %H:%M:%S') - ARCHIVING FILE: $ORIGINAL_NAME" >> "$LOG_FILE"
    echo "New Name: $NEW_NAME" >> "$LOG_FILE"
    echo "--- File Content: ---" >> "$LOG_FILE"
    
    # Append the file's entire content to organizer.log [cite: 95]
    cat "$ORIGINAL_NAME" >> "$LOG_FILE"
    echo "==================================================" >> "$LOG_FILE"

    # Move & Rename: Move the file to the archive directory [cite: 97]
    mv "$ORIGINAL_NAME" "$ARCHIVE_DIR/$NEW_NAME"
    echo "Archived $ORIGINAL_NAME to $ARCHIVE_DIR/$NEW_NAME"

done

echo "$(date '+%Y-%m-%d %H:%M:%S') - Organizer script finished processing CSVs." >> "$LOG_FILE"