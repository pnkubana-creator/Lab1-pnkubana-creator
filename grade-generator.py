import csv
import sys

# --- Data Structure to Hold All Assignments ---
assignments = []
total_fa_weight = 0
total_sa_weight = 0

# --- Helper Functions for Validation ---
def validate_grade(grade_input):
    """Validates grade is a number between 0 and 100."""
    try:
        grade = float(grade_input)
        if 0 <= grade <= 100:
            return grade
        else:
            print("Error: Grade must be between 0 and 100.") #[cite: 40]
            return None
    except ValueError:
        print("Error: Grade must be a number.") #[cite: 43]
        return None

def validate_category(category_input):
    """Validates category is 'FA' or 'SA' and returns uppercase."""
    category = category_input.strip().upper()
    if category in ("FA", "SA"):
        return category
    else:
        print("Error: Category must be 'FA' or 'SA'.") #[cite: 41]
        return None

def validate_weight(weight_input):
    """Validates weight is a positive number."""
    try:
        weight = float(weight_input)
        if weight > 0:
            return weight
        else:
            print("Error: Weight must be a positive number.") #[cite: 42]
            return None
    except ValueError:
        print("Error: Weight must be a number.") #[cite: 43]
        return None

# --- Main Input Loop ---
def collect_input():
    global total_fa_weight, total_sa_weight
    
    while True:
        print("\n--- New Assignment ---")
        
        # 1. Assignment Name
        name = input("Enter Assignment Name: ").strip() #[cite: 33]

        # 2. Category Validation
        category = None
        while category is None:
            category_input = input("Enter Category (FA/SA): ") #[cite: 34]
            category = validate_category(category_input)

        # 3. Grade Validation
        grade = None
        while grade is None:
            grade_input = input("Enter Grade Obtained (0-100): ") #[cite: 35]
            grade = validate_grade(grade_input)
        
        # 4. Weight Validation
        weight = None
        while weight is None:
            weight_input = input("Enter Weight (e.g., 30): ") #[cite: 36]
            weight = validate_weight(weight_input)

        # Add assignment to list
        assignments.append({
            'Assignment': name,
            'Category': category,
            'Grade': grade,
            'Weight': weight,
            # Calculated Field (Grade/100) * Weight [cite: 49]
            'Weighted_Grade': (grade / 100) * weight
        })

        # Update total weights
        if category == "FA":
            total_fa_weight += weight
        else:
            total_sa_weight += weight
            
        # Check if user wants to stop
        stop = input("Add another assignment? (y/n): ").strip().lower() #[cite: 37]
        if stop == 'n':
            break

# --- Calculation Logic ---
def calculate_results():
    total_weighted_fa = 0.0
    total_weighted_sa = 0.0
    
    for item in assignments:
        if item['Category'] == 'FA':
            total_weighted_fa += item['Weighted_Grade'] #[cite: 52]
        else:
            total_weighted_sa += item['Weighted_Grade'] #[cite: 52]

    # Calculate Totals
    total_grade = total_weighted_fa + total_weighted_sa #[cite: 53]
    gpa = (total_grade / 100) * 5.0 #[cite: 54]

    # Pass/Fail Logic [cite: 55]
    status = "PASS"
    resubmission = "None"
    
    # Check if student scored at or above 50% in BOTH categories [cite: 55]
    if total_fa_weight > 0 and (total_weighted_fa / total_fa_weight) < 0.5:
        status = "FAIL"
        resubmission = "Formative"
    elif total_sa_weight > 0 and (total_weighted_sa / total_sa_weight) < 0.5:
        status = "FAIL"
        resubmission = "Summative"
    
    # Store results for summary
    results = {
        'total_fa': total_weighted_fa,
        'weight_fa': total_fa_weight,
        'total_sa': total_weighted_sa,
        'weight_sa': total_sa_weight,
        'total_grade': total_grade,
        'gpa': gpa,
        'status': status,
        'resubmission': resubmission
    }
    return results

# --- Output 1: Console Summary ---
def print_summary(results):
    print("\n" + "="*40)
    print(" " * 15 + "RESULTS") #[cite: 59]
    print("="*40)
    
    print(f"Total Formative: {results['total_fa']:.2f}/{results['weight_fa']:.0f}") #[cite: 60]
    print(f"Total Summative: {results['total_sa']:.2f}/{results['weight_sa']:.0f}") #[cite: 61]
    
    print("-" * 40)
    print(f"Total Grade:     {results['total_grade']:.2f}/100") #[cite: 62, 66]
    print(f"GPA:             {results['gpa']:.4f}") #[cite: 63, 67]
    print(f"Status:          {results['status']}") #[cite: 64, 68]
    print(f"Resubmission:    {results['resubmission']}") #[cite: 65, 69]
    print("="*40 + "\n")

# --- Output 2: CSV File Generation ---
def generate_csv_file():
    filename = "grades.csv" #[cite: 71]
    
    # Header row defined by requirements [cite: 73]
    fieldnames = ['Assignment', 'Category', 'Grade', 'Weight']
    
    try:
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # Write the header [cite: 73]
            writer.writeheader()
            
            # Write the data [cite: 74]
            # Use a list comprehension to write only the required fields
            data_to_write = [{k: item[k] for k in fieldnames} for item in assignments]
            writer.writerows(data_to_write)
            
        print(f"✅ Success! Assignment data exported to {filename}.")
        
    except Exception as e:
        print(f"Error writing CSV file: {e}")
        sys.exit(1)


# --- Main Execution Block ---
if __name__ == "__main__":
    print("Welcome to the Python Grade Generator!")
    
    collect_input()
    
    if not assignments:
        print("No assignments entered. Exiting.")
        sys.exit(0)

    results = calculate_results()
    print_summary(results)
    generate_csv_file()