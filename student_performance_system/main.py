import numpy as np
import pandas as pd

FILE_PATH = "Webevis-internship/student_performance_system/data/students_stats.csv"


class SPMS:

    def __init__(self, csv_file_path):
        self.df = pd.read_csv(csv_file_path)

###############################################

    def add_student(self):
        roll = input("Enter the id of the New Student: ")
        name = input("Enter the name of the New Student: ")

        if roll in self.df["id"].values:
            return f" Error: ID '{roll}' already exists. Please enter a unique ID."


        new_stu = {
            "id": roll,
            "name": name
        }
        n = len(self.df)
        self.df.loc[n] = new_stu

        # print(self.df.head(7))
        return f"New Student {name}, added under the ROLL ID: {roll}"

###############################################

    def update_rec(self):
        roll = str(input("Enter the student's ID to perform updation: "))
        ###############################################
        if roll not in self.df["id"].values:
            return "Invalid ID Entered"
        ###############################################
        item_update = str(input(
            "Enter Serial number of one of the following options to update: \n1- Update ID\n2- Update Name\n3- Update Marks:\n").strip(" "))
        ###############################################
        if item_update == "1":
            nroll = str(input("Enter New ID to Update: "))

            if nroll in self.df["id"].values:
                return "New ID already exists in the database! choose a unique ID to update."

            # self.df = self.df.set_index("id")
            self.df.loc[self.df["id"] == roll, ["id"]] = nroll
            # self.df = self.df.reset_index()

            return "Roll-ID Updated Successfully"


        elif item_update == "2":
            nname = str(input("Enter New Name to Update: "))
            self.df.loc[self.df["id"] == roll, ["name"]] = nname
            return "Name Updated Successfully"

        elif item_update == "3":
            subs = ["math", "english", "science", "history"]
            for sub in subs:
                nmarks = int(input(f"Enter the Updated Marks for {sub}:"))
                self.df.loc[self.df["id"] == roll, [sub]] = nmarks

            return "Marks Updated Successfully"
###############################################

    def del_rec(self):
        roll = str(input("Enter the student's ID to perform deletion: ")).strip(" ")
        self.df = self.df.set_index("id")
        ###############################################
        try:
            self.df.drop(index=roll, inplace=True)
            return f"Student Record for the ID: {roll} has been successfully deleted!!"
        except ValueError:
            return f"Invalid ID Received!"
        finally:
            self.df = self.df.reset_index()

###############################################

    def get_info(self):
        name = str(input("Enter the name of the Student:")).lower().strip(" ")
        matches = self.df[self.df['name'].str.lower() == name]
        ###############################################
        if matches.empty:
            return f"No Matches Found"
        else:
            f"Records that were successfully found:\n{matches}"

###############################################

    def performance_analyzer(self):
        subjects = ["math", "english", "science", "history"]
        self.df['average'] = self.df[subjects].mean(axis=1).round(2)
        ###############################################
        def give_grade(score):
            if score >= 85:
                return 'Excellent'
            elif score >= 70:
                return 'Good'
            elif score >= 50:
                return 'Average'
            else:
                return 'Poor'
        ###############################################
        self.df["grade"] = self.df["average"].apply(give_grade)
        return "Students Graded and overall avg score score updated in the main shet!!"

###############################################

    def toppers(self):
        if 'average' not in self.df.columns:
            self.performance_analyzer()
        ###############################################
        highest = self.df["average"].max()
        highest_toppers = self.df[self.df["average"] == highest]
        ###############################################
        # print(f"---> Highest Achivers:")
        subs_tops = []
        i = 1

        for _, row in highest_toppers.iterrows():
            subs_tops.append(
                f'{i}-) {row["name"]} : \n'
                f'----> ID : {row["id"]} \n'
                f'----> Average Marks: {row["average"]}'
            )
            i += 1

        return f"---> Highest Achivers:\n" + "\n".join(subs_tops)

###############################################

    def sub_toppers(self):
        print("\n----> Subject Toppers:")
        subjects = ["math", "english", "science", "history"]
        ###############################################
        for sub in subjects:
            max_score = self.df[sub].max()
            sub_toppers = self.df[self.df[sub] == max_score]
            names = ", ".join(sub_toppers['name'].tolist())
            return f"{sub}: {names} ({max_score} marks)"

###############################################

    def gen_rep(self, output_filename="student_report.csv"):
        # Ensure analysis is done before reporting
        if 'average' not in self.df.columns or 'grade' not in self.df.columns:
            self.performance_analyzer()

        # Select only the specific columns requested in the image
        report_df = self.df[['id', 'name', 'average', 'grade']]

        report_df.to_csv(output_filename, index=False)
        self.df.to_csv("Students_Stats_Updated.csv", index=False)
        save_msg = f"\n Report successfully saved to '{output_filename}'\n"

        fin_report_msg1 = "\n================ FINAL REPORT ================"
        # print(report_df.to_string(index=False))
        # print("==============================================")

        return f"{save_msg}\n\n{fin_report_msg1}\n{report_df.to_string(index=False)}\n{'='*47}"
###############################################

# Initialize the system - Made with AI

rec = SPMS(FILE_PATH)

while True:
    print("\n" + "="*45)
    print("   STUDENT PERFORMANCE MANAGEMENT SYSTEM   ")
    print("="*45)
    print("1. Add a New Student")
    print("2. Update a Student Record")
    print("3. Delete a Student Record")
    print("4. Search for a Student")
    print("5. Analyze Performance (Avg & Grades)")
    print("6. Show Overall Toppers")
    print("7. Show Subject Toppers")
    print("8. Generate Final Report & Save CSVs")
    print("9. Exit")
    print("="*45)

    choice = input("Enter your choice (1-9): ").strip()

    if choice == '1':
        # add_student returns a string, so we print it
        print(rec.add_student())
    elif choice == '2':
        rec.update_rec()
    elif choice == '3':
        rec.del_rec()
    elif choice == '4':
        rec.get_info()
    elif choice == '5':
        rec.performance_analyzer()
    elif choice == '6':
        rec.toppers()
    elif choice == '7':
        rec.sub_toppers()
    elif choice == '8':
        rec.gen_rep()
    elif choice == '9':
        print("\nExiting the system. Goodbye!")
        break
    else:
        print("\n⚠️ Invalid choice. Please enter a number between 1 and 9.")