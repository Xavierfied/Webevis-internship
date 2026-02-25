# 🎓 Student Performance Management System (SPMS)

## 📖 Overview
Build a simple Python-based system to manage student records and analyze their academic performance. The system uses **Pandas** DataFrames for processing and processes everything directly from a CSV file.

## ✨ Features
* **CRUD Operations:** Add new students, update existing records (ID, name, marks), delete records, and search for specific students by name.
* **Performance Analysis:** Automatically calculates the average score for each student and assigns a performance category (Excellent, Good, Average, Poor).
* **Topper Identification:** Identifies the highest-achieving students overall based on average score, and the top scorers in individual subjects.
* **Automated Reporting:** Generates a clean final report and exports the data to a new CSV file (`student_report.csv`).
* **Validation:** Ensures unique student IDs, handles invalid inputs, and formats names cleanly.

## 🛠️ Prerequisites
Make sure you have Python installed on your system. You will also need the `pandas` and `numpy` libraries. You can install them using pip:

```bash
pip install pandas numpy
```

How to Run the System
Prepare your CSV File: Ensure you have a starting CSV file (e.g., students.csv) containing student records with columns for id, name, math, english, science, and history.

Update the File Path: Open the Python script and verify that the FILE_PATH variable points to the correct location of your input CSV file.

Run the Script: Open your terminal or command prompt, navigate to the folder containing your script, and run:

```bash
python "Student Performance Management System.py"
```

Use the Interactive Menu: Follow the on-screen prompts to interact with the system.
