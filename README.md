

# Lab 1: Grade Generator Calculator

This project consists of **two parts**: a Python application (`grade-generator.py`) for calculating a student’s final grade and exporting the data, and a Bash shell script (`organizer.sh`) for organizing and archiving the resulting CSV files.

---

## Project Overview

The primary goal of this lab is to demonstrate proficiency in:

* **Python**: Interactive input, validation, conditional logic, complex calculations, and file I/O (CSV).
* **Bash Scripting**: Directory management, file searching, timestamp generation, file renaming, and logging.

---

## Part 1: Python Grade Generator (`grade-generator.py`)

This interactive Python script collects assignment details, calculates a weighted final grade, determines Pass/Fail status, prints a summary to the console, and exports the data to a CSV file.

### ⚙️ Features

| Feature               | Description                                                                                                                             |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| **Interactive Input** | Continuously prompts the user for Assignment Name, Category (FA/SA), Grade Obtained (0-100), and Weight until the user chooses to stop. |
| **Input Validation**  | Ensures the Grade is between 0–100, Category is ‘FA’ or ‘SA’ (uppercase), and Weight is positive.                                       |
| **Calculation Logic** | Calculates Weighted Grade for each assignment: `(Grade / 100) * Weight`. Sums these to get Total Formative and Total Summative scores.  |
| **Final Metrics**     | Calculates the Total Grade (`Total Formative + Total Summative`) and GPA (`(Total Grade / 100) * 5.0`).                                 |
| **Pass/Fail Logic**   | A student passes only if they score at or above 50% in both Formative and Summative categories.                                         |
| **Console Output**    | Displays a clear summary of all totals, GPA, and final Status.                                                                          |
| **CSV Export**        | Exports all user-entered assignment data to `grades.csv` with headers: Assignment, Category, Grade, Weight.                             |

### 🚀 How to Run

1. Ensure Python is installed.
2. Run the script from your terminal:

```bash
python3 grade-generator.py
```

3. Follow the on-screen prompts to enter assignment details.

---

## Part 2: Shell Script Organizer (`organizer.sh`)

This Bash script organizes and archives any CSV files generated in the current directory.

### ⚙️ Features

| Step                | Description                                                                                                                   |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| **Setup**           | Checks for the existence of an `archive/` directory and creates it if it does not exist.                                      |
| **File Processing** | Finds all CSV files (`*.csv`) in the current directory.                                                                       |
| **Renaming**        | Generates a unique timestamp and inserts it into each filename (e.g., `grades.csv` → `grades-YYYYMMDD-HHMMSS.csv`).           |
| **Logging**         | Appends a detailed log of the archival action, including the file content, to `organizer.log`. Logs accumulate with each run. |
| **Archiving**       | Moves the renamed CSV file to the `archive/` directory.                                                                       |

### 🚀 How to Run

1. Make the script executable:

```bash
chmod +x organizer.sh
```

2. Run the script (after generating CSV files with Python):

```bash
./organizer.sh
```

3. Check the `archive/` directory and `organizer.log` to view results.

---

## 📦 Submission Requirements

Ensure your submission includes:

* `grade-generator.py`
* `organizer.sh`
* `README.md`

