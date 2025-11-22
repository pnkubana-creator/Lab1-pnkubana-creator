# ⭐ Lab 1: Grade Generator Calculator

This lab exercise is divided into **two standalone components**:

1. A **Python program** that gathers assessment information, performs weighted grade calculations, and saves the results.
2. A **Bash automation script** that organizes the exported CSV files by archiving and logging them.

Both parts work together to demonstrate practical skills in scripting, automation, and data handling.

---

## 📘 Part 1 — Python Grade Calculator (`grade-generator.py`)

This Python application walks the user through entering assessments, validates each input, computes final scores, prints a performance summary, and writes the data to a CSV file.

### 🔧 Main Capabilities

| Feature                  | Description                                                                                  |
| ------------------------ | -------------------------------------------------------------------------------------------- |
| **User Prompts**         | Requests assignment name, assessment type (FA/SA), score (0–100), and weighting.             |
| **Robust Validation**    | Verifies score limits, ensures proper category selection, and checks for positive weighting. |
| **Weighted Computation** | Calculates `(score / 100) × weight` for every assessment.                                    |
| **Category Totals**      | Separately accumulates Formative (FA) and Summative (SA) weighted points.                    |
| **Overall Results**      | Produces a Total Score and converts it to a GPA on a 5.0 scale.                              |
| **Pass/Fail Decision**   | Passing requires a minimum of 50% in both FA and SA sections.                                |
| **Formatted Summary**    | Displays FA total, SA total, GPA, final grade, and resubmission requirement (if any).        |
| **CSV Output**           | Stores assignment data into `grades.csv` for later processing.                               |

### ▶️ Running the Python Script

1. Make sure Python 3 is available on your system.
2. Execute the program:

```bash
python3 grade-generator.py
```

3. Follow the prompts to fill in assignment information.

---

## 📘 Part 2 — CSV Archiver Script (`organizer.sh`)

This shell script scans the current folder for CSV files and automatically archives them with timestamped names while maintaining a log of all processing activity.

### 🔧 Main Capabilities

| Action                   | Description                                                                             |
| ------------------------ | --------------------------------------------------------------------------------------- |
| **Directory Setup**      | Ensures an archive folder is present; creates one if needed.                            |
| **CSV Discovery**        | Locates all `.csv` files within the working directory.                                  |
| **Timestamped Renaming** | Inserts a date/time label into each filename to avoid collisions and track versions.    |
| **Activity Logging**     | Writes an entry to `organizer.log` containing the filename, new name, and its contents. |
| **Archival**             | Moves the renamed CSV file into the archive folder.                                     |

### ▶️ Running the Shell Script

1. Give the script execution permission:

```bash
chmod +x organizer.sh
```

2. Run it after generating CSV files:

```bash
./organizer.sh
```

3. Check the `stored_csv/` or `archive/` directory (depending on your version) for archived files and the log for activity history.

---

## 📂 Submission Checklist

Include these files when submitting your work:

* `grade-generator.py`
* `organizer.sh`
* `README.md`


