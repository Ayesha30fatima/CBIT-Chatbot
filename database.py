import sqlite3
import pandas as pd
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def create_tables():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    # Exams
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS exams (
            course TEXT,
            branch TEXT,
            year TEXT,
            semester TEXT,
            subject TEXT,
            exam_type TEXT,
            date TEXT,
            time TEXT,
            venue TEXT,
            max_marks INTEGER
        )
    """)

    # Assignments
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS assignments (
            course TEXT,
            subject TEXT,
            assignment_title TEXT,
            faculty TEXT,
            release_date TEXT,
            deadline TEXT,
            max_marks INTEGER,
            submission_type TEXT
        )
    """)

    # # Holidays
    # cursor.execute("""
    #     CREATE TABLE IF NOT EXISTS holidays (
    #         name TEXT,
    #         Date TEXT,
    #         Type TEXT
    #     )
    # """)


    # Schedule
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS schedule (
            course TEXT,
            branch TEXT,
            year TEXT,
            semester TEXT,
            day TEXT,
            subject TEXT,
            time TEXT,
            room TEXT,
            faculty TEXT
        )
    """)

    # Faculty
    cursor.execute("DROP TABLE IF EXISTS faculty")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS faculty (
            name TEXT,
            department TEXT,
            designation TEXT,
            email TEXT,
            courses_taught TEXT
        )
    """)

    # Syllabus
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS syllabus (
            subject_name TEXT,
            course_code TEXT,
            unit_number TEXT,
            unit_title TEXT,
            topics TEXT
        )
    """)

    # Labs
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS labs (
            lab_name TEXT,
            course_code TEXT,
            program_list TEXT
        )
    """)

    conn.commit()
    conn.close()

def insert_data():
    exams = pd.read_csv("exam_schedule.csv")
    assignments = pd.read_csv("assignments.csv")
    schedule = pd.read_csv("class_schedule.csv")
    syllabus = pd.read_csv("Syllabus_Table.csv")
    labs = pd.read_csv("Labs_Table.csv")

    faculty = pd.DataFrame([
        ["Dr. M Swamy Das", "Computer Science", "Professor", "mswamidas_cse@cbit.ac.in", "Soft Computing"],
        ["Dr T Sridevi", "Computer Science", "Associate Professor", "tsridevi_cse@cbit.ac.in", "Natural Language Processing"],
        ["Dr. E.Padmalatha", "Computer Science", "Associate Professor", "epadmalatha_cse@cbit.ac.in", "Big Data Analytics"],
        ["Dr. Kolla Morarjee", "Computer Science", "Associate Professor", "morarjeek_cse@cbit.ac.in", "Advanced Databases"],
        ["Dr Uma Maheswari V", "Computer Science", "Associate Professor", "umamaheswariv_cse@cbit.ac.in", "Student Co-ordinator"]
    ], columns=["name", "department", "designation", "email", "courses_taught"])

    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM exams")
    cursor.execute("DELETE FROM assignments")
    cursor.execute("DELETE FROM schedule")
    cursor.execute("DELETE FROM faculty")
    cursor.execute("DELETE FROM syllabus")
    cursor.execute("DELETE FROM labs")

    for _, row in exams.iterrows():
        cursor.execute("INSERT INTO exams VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", tuple(row))

    for _, row in assignments.iterrows():
        cursor.execute("INSERT INTO assignments VALUES (?, ?, ?, ?, ?, ?, ?, ?)", tuple(row))

    for _, row in schedule.iterrows():
        cursor.execute("INSERT INTO schedule VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", tuple(row))

    for _, row in faculty.iterrows():
        cursor.execute("INSERT INTO faculty VALUES (?, ?, ?, ?, ?)", tuple(row))

    for _, row in syllabus.iterrows():
        cursor.execute("INSERT INTO syllabus VALUES (?, ?, ?, ?, ?)", tuple(row))

    for _, row in labs.iterrows():
        cursor.execute("INSERT INTO labs VALUES (?, ?, ?)", tuple(row))

    conn.commit()
    conn.close()

def insert_almanac_exam_schedule():
    subjects = [
        "Soft Computing", "Advanced Databases", "Big Data Analytics",
        "Disaster Mitigation", "Natural Language Processing",
        "Operating Systems", "Machine Learning", "Network Security"
    ]

    exams_data = [
        ("MTECH", "CSE", "1st Year", "I", subjects[0], "Class Test I", "09.02.2025", "10:00", "Room 101", 20),
        ("MTECH", "CSE", "1st Year", "I", subjects[1], "Class Test I", "09.02.2025", "14:00", "Room 102", 20),
        ("MTECH", "CSE", "1st Year", "I", subjects[2], "Class Test I", "10.02.2025", "10:00", "Room 103", 20),
        ("MTECH", "CSE", "1st Year", "I", subjects[3], "Class Test I", "10.02.2025", "14:00", "Room 104", 20),
        ("MTECH", "CSE", "1st Year", "I", subjects[4], "Class Test I", "11.02.2025", "10:00", "Room 105", 20),
        ("MTECH", "CSE", "1st Year", "I", subjects[5], "Class Test I", "11.02.2025", "14:00", "Room 106", 20),
        ("MTECH", "CSE", "1st Year", "I", subjects[6], "Class Test II", "12.02.2025", "10:00", "Room 101", 20),
        ("MTECH", "CSE", "1st Year", "I", subjects[7], "Class Test II", "12.02.2025", "14:00", "Room 102", 20),
        ("MTECH", "CSE", "1st Year", "I", subjects[0], "Class Test II", "10.06.2025", "10:00", "Room 201", 20),
        ("MTECH", "CSE", "1st Year", "I", subjects[1], "Class Test II", "10.06.2025", "14:00", "Room 202", 20),
        ("MTECH", "CSE", "1st Year", "I", subjects[2], "Class Test II", "11.06.2025", "10:00", "Room 203", 20),
        ("MTECH", "CSE", "1st Year", "I", subjects[3], "Class Test II", "11.06.2025", "14:00", "Room 204", 20),
        ("MTECH", "CSE", "1st Year", "I", subjects[4], "Class Test II", "12.06.2025", "10:00", "Room 205", 20),
        ("MTECH", "CSE", "1st Year", "I", subjects[5], "Class Test II", "12.06.2025", "14:00", "Room 206", 20),
        ("MTECH", "CSE", "1st Year", "I", subjects[6], "Class Test II", "10.06.2025", "10:00", "Room 201", 20),
        ("MTECH", "CSE", "1st Year", "I", subjects[7], "Class Test II", "10.06.2025", "14:00", "Room 202", 20),
        ("MTECH", "CSE", "1st Year", "I", subjects[0], "End Semester", "07.07.2025", "10:00", "Main Hall", 60),
        ("MTECH", "CSE", "1st Year", "I", subjects[1], "End Semester", "09.07.2025", "10:00", "Main Hall", 60),
        ("MTECH", "CSE", "1st Year", "I", subjects[2], "End Semester", "11.07.2025", "10:00", "Main Hall", 60),
        ("MTECH", "CSE", "1st Year", "I", subjects[3], "End Semester", "14.07.2025", "10:00", "Main Hall", 60),
        ("MTECH", "CSE", "1st Year", "I", subjects[4], "End Semester", "16.07.2025", "10:00", "Main Hall", 60),
        ("MTECH", "CSE", "1st Year", "I", subjects[5], "End Semester", "18.07.2025", "10:00", "Main Hall", 60),
        ("MTECH", "CSE", "1st Year", "I", subjects[6], "End Semester", "21.07.2025", "10:00", "Main Hall", 60),
        ("MTECH", "CSE", "1st Year", "I", subjects[7], "End Semester", "23.07.2025", "10:00", "Main Hall", 60),
    ]

    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    # Prevent duplicates
    cursor.execute("DELETE FROM exams WHERE exam_type IN ('Class Test I', 'Class Test II', 'End Semester')")

    for row in exams_data:
        cursor.execute("INSERT INTO exams VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", row)

    conn.commit()
    conn.close()

import sqlite3

def create_holidays_table():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS holidays')
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS holidays (
            name TEXT,
            start_date TEXT,
            end_date TEXT,
            type TEXT,
            description TEXT
        )
    """)
    conn.commit()
    conn.close()

def insert_indian_holidays_2025():
    holidays = [
        # Vacations
        ("Sankranthi Vacation", "2025-01-13", "2025-01-27", "Vacation", "15-day Sankranthi vacation."),
        ("Summer Vacation", "2025-07-01", "2025-07-31", "Vacation", "1-month summer vacation."),
        ("Dussehra Vacation", "2025-09-28", "2025-10-05", "Vacation", "Week-long Dussehra vacation."),

        # Public Holidays & Festivals
        ("Republic Day", "2025-01-26", "2025-01-26", "Public Holiday", "Celebration of the Indian Constitution."),
        ("Mahashivratri", "2025-02-26", "2025-02-26", "Festival", "Dedicated to Lord Shiva."),
        ("Holi", "2025-03-14", "2025-03-14", "Festival", "Festival of colors."),
        ("Good Friday", "2025-04-18", "2025-04-18", "Public Holiday", "Christian holy day."),
        ("Ramzan/Eid-ul-Fitr", "2025-03-30", "2025-03-30", "Festival", "Marks the end of Ramadan."),
        ("Ambedkar Jayanti", "2025-04-14", "2025-04-14", "Public Holiday", "Birth anniversary of Dr. B.R. Ambedkar."),
        ("Bakrid/Eid al-Adha", "2025-06-07", "2025-06-07", "Festival", "Festival of sacrifice."),
        ("Muharram", "2025-07-06", "2025-07-06", "Festival", "Islamic New Year."),
        ("Independence Day", "2025-08-15", "2025-08-15", "Public Holiday", "India’s Independence Day."),
        ("Janmashtami", "2025-08-16", "2025-08-16", "Festival", "Birth of Lord Krishna."),
        ("Ganesh Chaturthi", "2025-08-26", "2025-08-26", "Festival", "Celebrates birth of Lord Ganesha."),
        ("Gandhi Jayanti", "2025-10-02", "2025-10-02", "Public Holiday", "Birthday of Mahatma Gandhi."),
        ("Vijaya Dashami/Dussehra", "2025-10-03", "2025-10-03", "Festival", "Victory of good over evil."),
        ("Diwali", "2025-10-20", "2025-10-20", "Festival", "Festival of lights."),
        ("Guru Nanak Jayanti", "2025-11-05", "2025-11-05", "Festival", "Birth of Guru Nanak."),
        ("Christmas", "2025-12-25", "2025-12-25", "Public Holiday", "Birth of Jesus Christ.")
    ]

    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM holidays")  # Optional: Reset before insert

    for holiday in holidays:
        cursor.execute("INSERT INTO holidays VALUES (?, ?, ?, ?, ?)", holiday)

    conn.commit()
    conn.close()



if __name__ == "__main__":
    create_tables()
    insert_data()
    insert_almanac_exam_schedule()
    create_holidays_table()             
    insert_indian_holidays_2025()         
    print("All tables created and data (including Almanac exams & holidays) loaded successfully.")

