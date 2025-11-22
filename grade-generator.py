import csv
import sys

# ==============================
#   Global Containers
# ==============================
records = []              # Stores all task entries
fa_total_weight = 0       # Tracks total FA weighting
sa_total_weight = 0       # Tracks total SA weighting


# ==============================
#   Validation Utilities
# ==============================
def check_score(value):
    """Ensure the score is a numeric value between 0 and 100."""
    try:
        score = float(value)
        if 0 <= score <= 100:
            return score
        print("Invalid: Score must be 0–100.")
        return None
    except ValueError:
        print("Invalid: Score should be a numeric value.")
        return None


def check_type(raw_type):
    """Confirm the assessment type is FA or SA."""
    mode = raw_type.strip().upper()
    if mode in ("FA", "SA"):
        return mode
    print("Invalid: Type must be FA or SA only.")
    return None


def check_weight(amount):
    """Ensure the weighting is positive."""
    try:
        w = float(amount)
        if w > 0:
            return w
        print("Invalid: Weight must be greater than zero.")
        return None
    except ValueError:
        print("Invalid: Weight must be a number.")
        return None


# ==============================
#   Data Collection Loop
# ==============================
def gather_entries():
    global fa_total_weight, sa_total_weight

    while True:
        print("\n--- Add New Task ---")

        # Task label
        title = input("Task Name: ").strip()

        # Task category
        category = None
        while category is None:
            category = check_type(input("Type (FA/SA): "))

        # Score
        score = None
        while score is None:
            score = check_score(input("Score (0–100): "))

        # Weight
        weight = None
        while weight is None:
            weight = check_weight(input("Weight: "))

        # Store task info
        records.append({
            "Task": title,
            "Type": category,
            "Score": score,
            "Weight": weight,
            "WeightedScore": (score / 100) * weight
        })

        # Update weight category totals
        if category == "FA":
            fa_total_weight += weight
        else:
            sa_total_weight += weight

        # Continue?
        cont = input("Add another? (y/n): ").lower().strip()
        if cont == 'n':
            break


# ==============================
#   Result Processing
# ==============================
def compute_results():
    fa_points = 0
    sa_points = 0

    for r in records:
        if r["Type"] == "FA":
            fa_points += r["WeightedScore"]
        else:
            sa_points += r["WeightedScore"]

    full_score = fa_points + sa_points
    gpa = (full_score / 100) * 5

    verdict = "PASS"
    redo = "None"

    # Failure logic (below 50% in FA or SA)
    if fa_total_weight > 0 and (fa_points / fa_total_weight) < 0.5:
        verdict = "FAIL"
        redo = "Formative"
    elif sa_total_weight > 0 and (sa_points / sa_total_weight) < 0.5:
        verdict = "FAIL"
        redo = "Summative"

    return {
        "fa_points": fa_points,
        "fa_weight": fa_total_weight,
        "sa_points": sa_points,
        "sa_weight": sa_total_weight,
        "final_score": full_score,
        "gpa": gpa,
        "verdict": verdict,
        "redo": redo
    }


# ==============================
#   Display Report
# ==============================
def display_report(info):
    print("\n" + "=" * 45)
    print(" " * 16 + "FINAL REPORT")
    print("=" * 45)

    print(f"FA Total: {info['fa_points']:.2f}/{info['fa_weight']:.0f}")
    print(f"SA Total: {info['sa_points']:.2f}/{info['sa_weight']:.0f}")

    print("-" * 45)
    print(f"Overall Score: {info['final_score']:.2f}/100")
    print(f"GPA: {info['gpa']:.4f}")
    print(f"Status: {info['verdict']}")
    print(f"Resubmission Required: {info['redo']}")
    print("=" * 45 + "\n")


# ==============================
#   CSV Export
# ==============================
def save_as_csv():
    filename = "output_grades.csv"
    headers = ["Task", "Type", "Score", "Weight"]

    try:
        with open(filename, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()

            # Save only visible fields
            cleaned = [{h: rec[h] for h in headers} for rec in records]
            writer.writerows(cleaned)

        print(f"✔ Data successfully saved to {filename}")

    except Exception as err:
        print(f"CSV Write Error: {err}")
        sys.exit(1)


# ==============================
#   Program Entry Point
# ==============================
if __name__ == "__main__":
    print("=== Grade Processing Program ===")

    gather_entries()

    if not records:
        print("No tasks provided. Program stopped.")
        sys.exit(0)

    summary = compute_results()
    display_report(summary)
    save_as_csv()
