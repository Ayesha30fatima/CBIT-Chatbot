# import sqlite3
# import re

# # Store user context globally
# user_course = ""
# user_year = ""

# def get_exam_info():
#     conn = sqlite3.connect("data.db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT subject, exam_type, date, time, venue FROM exams WHERE course = ? AND year = ? ORDER BY date",
#                    (user_course, user_year))
#     rows = cursor.fetchall()
#     conn.close()

#     if not rows:
#         return "No exam data found for your course and year."

#     return "\n".join([f"{subject} ({exam_type}) on {date} at {time} in {venue}" for subject, exam_type, date, time, venue in rows])


# def get_schedule():
#     conn = sqlite3.connect("data.db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT day, subject, time, room, faculty FROM schedule WHERE course = ? AND year = ? ORDER BY day",
#                    (user_course, user_year))
#     rows = cursor.fetchall()
#     conn.close()

#     if not rows:
#         return "No schedule found for your course and year."

#     return "\n".join([f"{day}: {subject} at {time} in {room} (by {faculty})" for day, subject, time, room, faculty in rows])


# def get_faculty_info():
#     conn = sqlite3.connect("data.db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT name, department, designation, email, office_hours FROM faculty")
#     rows = cursor.fetchall()
#     conn.close()

#     if not rows:
#         return "No faculty data found."

#     return "\n".join([f"{name} ({designation}, {department}) — {email}, Office Hours: {office_hours}" 
#                       for name, department, designation, email, office_hours in rows])


# def get_assignments():
#     conn = sqlite3.connect("data.db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT subject, assignment_title, deadline FROM assignments WHERE course = ? ORDER BY deadline",
#                    (user_course,))
#     rows = cursor.fetchall()
#     conn.close()

#     if not rows:
#         return "No assignment deadlines found for your course."

#     return "\n".join([f"{subject}: {assignment_title} due by {deadline}" for subject, assignment_title, deadline in rows])


# from datetime import datetime

# def get_today_schedule():
#     today = datetime.now().strftime("%A")  # e.g., 'Monday'
#     conn = sqlite3.connect("data.db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT day, subject, time, room, faculty FROM schedule WHERE course = ? AND year = ? AND day = ?", 
#                    (user_course, user_year, today))
#     rows = cursor.fetchall()
#     conn.close()

#     if not rows:
#         return f"No classes scheduled for today ({today})."
    
#     return "\n".join([f"{subject} at {time} in {room} (by {faculty})" for day, subject, time, room, faculty in rows])


# def get_schedule_by_day(day):
#     conn = sqlite3.connect("data.db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT subject, time, room, faculty FROM schedule WHERE course = ? AND year = ? AND day = ?", 
#                    (user_course, user_year, day))
#     rows = cursor.fetchall()
#     conn.close()

#     if not rows:
#         return f"No classes scheduled on {day}."
    
#     return "\n".join([f"{subject} at {time} in {room} (by {faculty})" for subject, time, room, faculty in rows])


# def get_schedule_by_faculty(faculty_name):
#     conn = sqlite3.connect("data.db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT day, subject, time, room FROM schedule WHERE course = ? AND year = ? AND faculty LIKE ?", 
#                    (user_course, user_year, f"%{faculty_name}%"))
#     rows = cursor.fetchall()
#     conn.close()

#     if not rows:
#         return f"No classes found taught by {faculty_name}."

#     return "\n".join([f"{day}: {subject} at {time} in {room}" for day, subject, time, room in rows])







# def handle_query(query):
#     query = query.lower()

#     # Exams
#     if re.search(r'\bexam\b|\btest\b|\bmid\b|\bend term\b', query):
#         return get_exam_info()

#     # Faculty
#     elif re.search(r'\bfaculty\b|\bteacher\b|\bprofessor\b|\bstaff\b', query):
#         return get_faculty_info()

#     # Assignments
#     elif re.search(r'\bassignments?\b|\bdeadlines?\b|\bsubmit(ting|s)?\b', query):
#         return get_assignments()

#     # Today's schedule
#     elif "today" in query and "class" in query:
#         return get_today_schedule()

#     # Specific day schedule (e.g., "monday classes")
#     elif any(day in query for day in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]):
#         for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]:
#             if day.lower() in query:
#                 return get_schedule_by_day(day)

#     # Faculty-specific class queries
#     elif "class" in query and "by" in query:
#         match = re.search(r'class(?:es)? by (dr\.?\s\w+|prof\.?\s\w+|\w+)', query)
#         if match:
#             faculty_name = match.group(1).strip().title()
#             return get_schedule_by_faculty(faculty_name)

#     # General schedule
#     elif re.search(r'\b(class|timetable|schedule)\b', query):
#         return get_schedule()

#     elif query in ['exit', 'quit']:
#         return "Goodbye!"

#     else:
#         return "I didn't quite get that. Try asking about exams, schedule, assignments, or faculty."



# # 🧠 Ask course/year and start chatbot loop
# if __name__ == "__main__":
#     print("👩‍🎓 Welcome to the Student Helpdesk Chatbot!")
    

#     user_course = input("🔷 Please enter your course code (e.g., CSE101): ").strip().upper()
#     year_input = input("🔷 Please enter your year (e.g., 1st Year): ").strip().lower()

#     # Normalize to match DB format
#     if "1" in year_input:
#         user_year = "1st Year"
#     elif "2" in year_input:
#         user_year = "2nd Year"
#     elif "3" in year_input:
#         user_year = "3rd Year"
#     elif "4" in year_input:
#         user_year = "4th Year"
#     else:
#         user_year = "Unknown"


#     print("\n✅ Setup complete. You can now ask about exams, schedule, faculty, or assignments!")
#     print("💬 Type 'exit' anytime to quit.\n")

#     while True:
#         user_input = input("You: ")
#         if user_input.lower() in ['exit', 'quit']:
#             print("Bot: Goodbye!")
#             break
#         response = handle_query(user_input)
#         print("Bot:", response)


#Version2

# import sqlite3
# import re
# from datetime import datetime

# # Store user context globally
# user_course = ""
# user_year = ""

# def get_exam_info():
#     conn = sqlite3.connect("data.db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT subject, exam_type, date, time, venue FROM exams WHERE course = ? AND year = ? ORDER BY date",
#                    (user_course, user_year))
#     rows = cursor.fetchall()
#     conn.close()

#     if not rows:
#         return "No exam data found for your course and year."

#     return "\n".join([f"{subject} ({exam_type}) on {date} at {time} in {venue}" for subject, exam_type, date, time, venue in rows])

# def get_schedule():
#     conn = sqlite3.connect("data.db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT day, subject, time, room, faculty FROM schedule WHERE course = ? AND year = ? ORDER BY day",
#                    (user_course, user_year))
#     rows = cursor.fetchall()
#     conn.close()

#     if not rows:
#         return "No schedule found for your course and year."

#     return "\n".join([f"{day}: {subject} at {time} in {room} (by {faculty})" for day, subject, time, room, faculty in rows])

# def get_faculty_info():
#     conn = sqlite3.connect("data.db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT name, department, designation, email, office_hours FROM faculty")
#     rows = cursor.fetchall()
#     conn.close()

#     if not rows:
#         return "No faculty data found."

#     return "\n".join([f"{name} ({designation}, {department}) — {email}, Office Hours: {office_hours}" 
#                       for name, department, designation, email, office_hours in rows])

# def get_assignments():
#     conn = sqlite3.connect("data.db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT subject, assignment_title, deadline FROM assignments WHERE course = ? ORDER BY deadline",
#                    (user_course,))
#     rows = cursor.fetchall()
#     conn.close()

#     if not rows:
#         return "No assignment deadlines found for your course."

#     return "\n".join([f"{subject}: {assignment_title} due by {deadline}" for subject, assignment_title, deadline in rows])

# def get_today_schedule():
#     today = datetime.now().strftime("%A")
#     conn = sqlite3.connect("data.db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT day, subject, time, room, faculty FROM schedule WHERE course = ? AND year = ? AND day = ?", 
#                    (user_course, user_year, today))
#     rows = cursor.fetchall()
#     conn.close()

#     if not rows:
#         return f"No classes scheduled for today ({today})."

#     return "\n".join([f"{subject} at {time} in {room} (by {faculty})" for day, subject, time, room, faculty in rows])

# def get_schedule_by_day(day):
#     conn = sqlite3.connect("data.db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT subject, time, room, faculty FROM schedule WHERE course = ? AND year = ? AND day = ?", 
#                    (user_course, user_year, day))
#     rows = cursor.fetchall()
#     conn.close()

#     if not rows:
#         return f"No classes scheduled on {day}."

#     return "\n".join([f"{subject} at {time} in {room} (by {faculty})" for subject, time, room, faculty in rows])

# def get_schedule_by_faculty(faculty_name):
#     conn = sqlite3.connect("data.db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT day, subject, time, room FROM schedule WHERE course = ? AND year = ? AND faculty LIKE ?", 
#                    (user_course, user_year, f"%{faculty_name}%"))
#     rows = cursor.fetchall()
#     conn.close()

#     if not rows:
#         return f"No classes found taught by {faculty_name}."

#     return "\n".join([f"{day}: {subject} at {time} in {room}" for day, subject, time, room in rows])

# def get_syllabus(subject, unit=None):
#     conn = sqlite3.connect("data.db")
#     cursor = conn.cursor()
#     if unit:
#         cursor.execute("SELECT unit_number, unit_title, topics FROM syllabus WHERE subject_name LIKE ? AND unit_number LIKE ?", 
#                        (f"%{subject}%", f"%{unit}%"))
#     else:
#         cursor.execute("SELECT unit_number, unit_title, topics FROM syllabus WHERE subject_name LIKE ?", 
#                        (f"%{subject}%",))
#     rows = cursor.fetchall()
#     conn.close()

#     if not rows:
#         return "No syllabus found for that subject or unit."

#     return "\n\n".join([f"{unit} — {title}\n{topics}" for unit, title, topics in rows])

# def get_lab_programs(subject):
#     conn = sqlite3.connect("data.db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT program_list FROM labs WHERE lab_name LIKE ?", (f"%{subject}%",))
#     row = cursor.fetchone()
#     conn.close()

#     if not row:
#         return "No lab programs found for that subject."
#     return row[0]

# def handle_query(query):
#     query = query.lower()

#     # Exams
#     if re.search(r'\bexam\b|\btest\b|\bmid\b|\bend term\b', query):
#         return get_exam_info()

#     # Faculty
#     elif re.search(r'\bfaculty\b|\bteacher\b|\bprofessor\b|\bstaff\b', query):
#         return get_faculty_info()

#     # Assignments
#     elif re.search(r'\bassignments?\b|\bdeadlines?\b|\bsubmit(ting|s)?\b', query):
#         return get_assignments()

#     # Today's schedule
#     elif "today" in query and "class" in query:
#         return get_today_schedule()

#     # Specific day schedule
#     elif any(day in query for day in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]):
#         for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]:
#             if day.lower() in query:
#                 return get_schedule_by_day(day)

#     # Faculty-specific class queries
#     elif "class" in query and "by" in query:
#         match = re.search(r'class(?:es)? by (dr\.?\s\w+|prof\.?\s\w+|\w+)', query)
#         if match:
#             faculty_name = match.group(1).strip().title()
#             return get_schedule_by_faculty(faculty_name)

#     # Syllabus queries
#     elif "syllabus" in query or "unit" in query:
#         match = re.search(r"(unit\s+\w+)?\s*(of|for)?\s*(advanced databases|soft computing|big data analytics|natural language processing|disaster mitigation)", query)
#         if match:
#             unit = match.group(1).strip().title() if match.group(1) else None
#             subject = match.group(3).strip().title()
#             return get_syllabus(subject, unit)

#     # Lab program queries
#     elif "lab" in query and ("program" in query or "experiment" in query or "list" in query):
#         match = re.search(r"(advanced databases and soft computing|big data analytics|mini project)", query)
#         if match:
#             subject = match.group(1).strip().title()
#             return get_lab_programs(subject)

#     # General schedule
#     elif re.search(r'\b(class|timetable|schedule)\b', query):
#         return get_schedule()

#     elif query in ['exit', 'quit']:
#         return "Goodbye!"

#     else:
#         return "I didn't quite get that. Try asking about exams, schedule, assignments, or faculty."

# if __name__ == "__main__":
#     print("\U0001F469‍\U0001F393 Welcome to the Student Helpdesk Chatbot!")
#     user_course = input("🔷 Please enter your course code (e.g., CSE101): ").strip().upper()
#     year_input = input("🔷 Please enter your year (e.g., 1st Year): ").strip().lower()

#     if "1" in year_input:
#         user_year = "1st Year"
#     elif "2" in year_input:
#         user_year = "2nd Year"
#     elif "3" in year_input:
#         user_year = "3rd Year"
#     elif "4" in year_input:
#         user_year = "4th Year"
#     else:
#         user_year = "Unknown"

#     print("\n✅ Setup complete. You can now ask about exams, schedule, faculty, or assignments!")
#     print("💬 Type 'exit' anytime to quit.\n")

#     while True:
#         user_input = input("You: ")
#         if user_input.lower() in ['exit', 'quit']:
#             print("Bot: Goodbye!")
#             break
#         response = handle_query(user_input)
#         print("Bot:", response)

# version 3

# import sqlite3
# import re
# from datetime import datetime

# # Store user context globally
# user_course = ""
# user_year = ""

# def get_exam_info():
#     conn = sqlite3.connect("data.db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT subject, exam_type, date, time, venue FROM exams WHERE course = ? AND year = ? ORDER BY date",
#                    (user_course, user_year))
#     rows = cursor.fetchall()
#     conn.close()

#     if not rows:
#         return "No exam data found for your course and year."

#     return "\n".join([f"{subject} ({exam_type}) on {date} at {time} in {venue}" for subject, exam_type, date, time, venue in rows])

# def get_exam_info_by_type(exam_type):
#     conn = sqlite3.connect("data.db")
#     cursor = conn.cursor()
#     cursor.execute("""
#         SELECT subject, date, time, venue 
#         FROM exams 
#         WHERE course = ? AND year = ? AND exam_type = ? 
#         ORDER BY date
#     """, (user_course, user_year, exam_type))
#     rows = cursor.fetchall()
#     conn.close()

#     if not rows:
#         return f"No {exam_type} schedule found for your course and year."

#     return f"{exam_type} Schedule:\n" + "\n".join(
#         [f"{subject} on {date} at {time} in {venue}" for subject, date, time, venue in rows]
#     )

# def get_schedule():
#     conn = sqlite3.connect("data.db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT day, subject, time, room, faculty FROM schedule WHERE course = ? AND year = ? ORDER BY day",
#                    (user_course, user_year))
#     rows = cursor.fetchall()
#     conn.close()

#     if not rows:
#         return "No schedule found for your course and year."

#     return "\n".join([f"{day}: {subject} at {time} in {room} (by {faculty})" for day, subject, time, room, faculty in rows])

# def get_faculty_info():
#     conn = sqlite3.connect("data.db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT name, department, designation, email FROM faculty")
#     rows = cursor.fetchall()
#     conn.close()

#     if not rows:
#         return "No faculty data found."

#     return "\n".join([f"{name} ({designation}, {department}) — {email}" for name, department, designation, email in rows])

# def get_professor_email(name):
#     conn = sqlite3.connect("data.db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT email FROM faculty WHERE name LIKE ?", (f"%{name}%",))
#     row = cursor.fetchone()
#     conn.close()

#     if not row:
#         return f"Email for {name} not found."
#     return f"Email of {name} is {row[0]}"

# def get_assignments():
#     conn = sqlite3.connect("data.db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT subject, assignment_title, deadline FROM assignments WHERE course = ? ORDER BY deadline",
#                    (user_course,))
#     rows = cursor.fetchall()
#     conn.close()

#     if not rows:
#         return "No assignment deadlines found for your course."

#     return "\n".join([f"{subject}: {assignment_title} due by {deadline}" for subject, assignment_title, deadline in rows])

# def get_today_schedule():
#     today = datetime.now().strftime("%A")
#     conn = sqlite3.connect("data.db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT day, subject, time, room, faculty FROM schedule WHERE course = ? AND year = ? AND day = ?", 
#                    (user_course, user_year, today))
#     rows = cursor.fetchall()
#     conn.close()

#     if not rows:
#         return f"No classes scheduled for today ({today})."

#     return "\n".join([f"{subject} at {time} in {room} (by {faculty})" for day, subject, time, room, faculty in rows])

# def get_schedule_by_day(day):
#     conn = sqlite3.connect("data.db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT subject, time, room, faculty FROM schedule WHERE course = ? AND year = ? AND day = ?", 
#                    (user_course, user_year, day))
#     rows = cursor.fetchall()
#     conn.close()

#     if not rows:
#         return f"No classes scheduled on {day}."

#     return "\n".join([f"{subject} at {time} in {room} (by {faculty})" for subject, time, room, faculty in rows])

# def get_schedule_by_faculty(faculty_name):
#     conn = sqlite3.connect("data.db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT day, subject, time, room FROM schedule WHERE course = ? AND year = ? AND faculty LIKE ?", 
#                    (user_course, user_year, f"%{faculty_name}%"))
#     rows = cursor.fetchall()
#     conn.close()

#     if not rows:
#         return f"No classes found taught by {faculty_name}."

#     return "\n".join([f"{day}: {subject} at {time} in {room}" for day, subject, time, room in rows])

# def get_professor_by_subject_from_faculty(subject_name):
#     conn = sqlite3.connect("data.db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT name FROM faculty WHERE courses_taught LIKE ?", (f"%{subject_name}%",))
#     rows = cursor.fetchall()
#     conn.close()

#     if not rows:
#         return f"No professor found teaching {subject_name}."

#     return f"{subject_name} is taught by: " + ", ".join([name for (name,) in rows])

# def get_student_coordinator():
#     conn = sqlite3.connect("data.db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT name, email FROM faculty WHERE courses_taught LIKE '%Student Co-ordinator%'")
#     row = cursor.fetchone()
#     conn.close()

#     if not row:
#         return "No student co-ordinator found."
#     return f"Your student co-ordinator is {row[0]} — Email: {row[1] if row[1] else 'Not available'}"

# def get_syllabus(subject, unit=None):
#     conn = sqlite3.connect("data.db")
#     cursor = conn.cursor()

#     if unit:
#         cursor.execute(
#             "SELECT unit_number, unit_title, topics FROM syllabus WHERE subject_name LIKE ? AND unit_number LIKE ?",
#             (f"%{subject}%", f"%{unit}%")
#         )
#     else:
#         cursor.execute(
#             "SELECT unit_number, unit_title, topics FROM syllabus WHERE subject_name LIKE ?",
#             (f"%{subject}%",)
#         )

#     rows = cursor.fetchall()
#     conn.close()

#     if not rows:
#         return "No syllabus found for that subject or unit."

#     seen = set()
#     formatted_units = []
#     for unit, title, topics in rows:
#         key = f"{unit.strip()} — {title.strip()}"
#         if key not in seen:
#             seen.add(key)
#             formatted_units.append(f"{key}\n{topics.strip()}")

#     return "\n\n".join(formatted_units)

# def get_lab_programs(subject):
#     conn = sqlite3.connect("data.db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT program_list FROM labs WHERE lab_name LIKE ?", (f"%{subject}%",))
#     row = cursor.fetchone()
#     conn.close()

#     if not row:
#         return "No lab programs found for that subject."
#     return row[0]

# def handle_query(query):
#     query = query.lower()

#     # Specific Exam Type Queries
#     if "class test i" in query:
#         return get_exam_info_by_type("Class Test I")
#     elif "class test ii" in query:
#         return get_exam_info_by_type("Class Test II")
#     elif "end semester" in query or "end sem" in query or "final exam" in query:
#         return get_exam_info_by_type("End Semester")
#     elif re.search(r'\bexam\b|\btest\b|\bmid\b|\bend term\b', query):
#         return get_exam_info()

#     # Faculty
#     elif re.search(r'\bfaculty\b|\bteacher\b|\bprofessor\b|\bstaff\b', query):
#         return get_faculty_info()

#     # Email query
#     elif re.search(r'email.*(dr\.?|prof\.?|\b)[a-z]+', query):
#         match = re.search(r'email.*(dr\.?|prof\.?|\b)([a-z ]+)', query)
#         if match:
#             name = match.group(2).strip().title()
#             return get_professor_email(name)

#     # Who teaches what
#     elif re.search(r'(who teaches|professor.*for|faculty.*for|which professor.*teaches)', query):
#         match = re.search(r'(soft computing|advanced databases|natural language processing|big data analytics|disaster mitigation|operating systems|machine learning|data mining|network security)', query)
#         if match:
#             subject_name = match.group(1).strip().title()
#             return get_professor_by_subject_from_faculty(subject_name)

#     # Assignments
#     elif re.search(r'\bassignments?\b|\bdeadlines?\b|\bsubmit(ting|s)?\b', query):
#         return get_assignments()

#     # Today's schedule
#     elif "today" in query and "class" in query:
#         return get_today_schedule()

#     # Specific day schedule
#     elif any(day in query for day in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]):
#         for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]:
#             if day.lower() in query:
#                 return get_schedule_by_day(day)

#     # Faculty-specific class queries
#     elif "class" in query and "by" in query:
#         match = re.search(r'class(?:es)? by (dr\.?\s\w+|prof\.?\s\w+|\w+)', query)
#         if match:
#             faculty_name = match.group(1).strip().title()
#             return get_schedule_by_faculty(faculty_name)

#     # Syllabus queries
#     elif "syllabus" in query or "unit" in query:
#         match = re.search(r"(unit\s+\w+)?\s*(of|for)?\s*(advanced databases|soft computing|big data analytics|natural language processing|disaster mitigation)", query)
#         if match:
#             unit = match.group(1).strip().title() if match.group(1) else None
#             subject = match.group(3).strip().title()
#             return get_syllabus(subject, unit)

#     # Lab program queries
#     elif "lab" in query and ("program" in query or "experiment" in query or "list" in query):
#         match = re.search(r"(advanced databases and soft computing|big data analytics|mini project)", query)
#         if match:
#             subject = match.group(1).strip().title()
#             return get_lab_programs(subject)

#     # General schedule
#     elif re.search(r'\b(class|timetable|schedule)\b', query):
#         return get_schedule()

#     elif query in ['exit', 'quit']:
#         return "Goodbye!"

#     else:
#         return "I didn't quite get that. Try asking about exams, schedule, assignments, or faculty."

# if __name__ == "__main__":
#     print("👩‍🎓 Welcome to the Student Helpdesk Chatbot!")
#     user_course = input("🔷 Please enter your course code (e.g., CSE101): ").strip().upper()
#     year_input = input("🔷 Please enter your year (e.g., 1st Year): ").strip().lower()

#     if "1" in year_input:
#         user_year = "1st Year"
#     elif "2" in year_input:
#         user_year = "2nd Year"
#     elif "3" in year_input:
#         user_year = "3rd Year"
#     elif "4" in year_input:
#         user_year = "4th Year"
#     else:
#         user_year = "Unknown"

#     print("\n✅ Setup complete. You can now ask about exams, schedule, faculty, or assignments!")
#     print("💬 Type 'exit' anytime to quit.\n")

#     while True:
#         user_input = input("You: ")
#         if user_input.lower() in ['exit', 'quit']:
#             print("Bot: Goodbye!")
#             break
#         response = handle_query(user_input)
#         print("Bot:", response)


#Version 4
# import sqlite3
# import re
# from datetime import datetime
# import difflib

# # Store user context globally
# user_course = ""
# user_year = ""

# # Utility: Fuzzy match subject name
# def find_closest_subject(user_query, subjects):
#     matches = difflib.get_close_matches(user_query, subjects, n=1, cutoff=0.6)
#     return matches[0] if matches else None

# def get_exam_info():
#     conn = sqlite3.connect("data.db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT subject, exam_type, date, time, venue FROM exams WHERE course = ? AND year = ? ORDER BY date",
#                    (user_course, user_year))
#     rows = cursor.fetchall()
#     conn.close()
#     if not rows:
#         return "No exam data found for your course and year."
#     return "\n".join([f"{subject} ({exam_type}) on {date} at {time} in {venue}" for subject, exam_type, date, time, venue in rows])

# def get_schedule():
#     conn = sqlite3.connect("data.db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT day, subject, time, room, faculty FROM schedule WHERE course = ? AND year = ? ORDER BY day",
#                    (user_course, user_year))
#     rows = cursor.fetchall()
#     conn.close()
#     if not rows:
#         return "No schedule found for your course and year."
#     return "\n".join([f"{day}: {subject} at {time} in {room} (by {faculty})" for day, subject, time, room, faculty in rows])

# def get_faculty_info():
#     conn = sqlite3.connect("data.db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT name, department, designation, email, courses_taught FROM faculty")
#     rows = cursor.fetchall()
#     conn.close()
#     if not rows:
#         return "No faculty data found."

#     return "\n".join([
#         f"{name} ({designation}, {department}) — {email}\nCourses Taught: {courses_taught}"
#         for name, department, designation, email, courses_taught in rows
#     ])


# def get_professor_email(name):
#     conn = sqlite3.connect("data.db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT email FROM faculty WHERE name LIKE ?", (f"%{name}%",))
#     row = cursor.fetchone()
#     conn.close()
#     if not row:
#         return f"Email for {name} not found."
#     return f"Email of {name} is {row[0]}"

# def get_assignments():
#     conn = sqlite3.connect("data.db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT subject, assignment_title, deadline FROM assignments WHERE course = ? ORDER BY deadline",
#                    (user_course,))
#     rows = cursor.fetchall()
#     conn.close()
#     if not rows:
#         return "No assignment deadlines found for your course."
#     return "\n".join([f"{subject}: {assignment_title} due by {deadline}" for subject, assignment_title, deadline in rows])

# def get_today_schedule():
#     today = datetime.now().strftime("%A")
#     conn = sqlite3.connect("data.db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT day, subject, time, room, faculty FROM schedule WHERE course = ? AND year = ? AND day = ?", 
#                    (user_course, user_year, today))
#     rows = cursor.fetchall()
#     conn.close()
#     if not rows:
#         return f"No classes scheduled for today ({today})."
#     return "\n".join([f"{subject} at {time} in {room} (by {faculty})" for _, subject, time, room, faculty in rows])

# def get_schedule_by_day(day):
#     conn = sqlite3.connect("data.db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT subject, time, room, faculty FROM schedule WHERE course = ? AND year = ? AND day = ?", 
#                    (user_course, user_year, day))
#     rows = cursor.fetchall()
#     conn.close()
#     if not rows:
#         return f"No classes scheduled on {day}."
#     return "\n".join([f"{subject} at {time} in {room} (by {faculty})" for subject, time, room, faculty in rows])

# def get_schedule_by_faculty(faculty_name):
#     conn = sqlite3.connect("data.db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT day, subject, time, room FROM schedule WHERE course = ? AND year = ? AND faculty LIKE ?", 
#                    (user_course, user_year, f"%{faculty_name}%"))
#     rows = cursor.fetchall()
#     conn.close()
#     if not rows:
#         return f"No classes found taught by {faculty_name}."
#     return "\n".join([f"{day}: {subject} at {time} in {room}" for day, subject, time, room in rows])

# def get_professor_by_subject_from_faculty(subject_name):
#     conn = sqlite3.connect("data.db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT name FROM faculty WHERE courses_taught LIKE ?", (f"%{subject_name}%",))
#     rows = cursor.fetchall()
#     conn.close()
#     if not rows:
#         return f"No professor found teaching {subject_name}."
#     return f"{subject_name} is taught by: " + ", ".join([name for (name,) in rows])

# def get_syllabus(subject, unit=None):
#     conn = sqlite3.connect("data.db")
#     cursor = conn.cursor()
#     if unit:
#         cursor.execute("SELECT unit_number, unit_title, topics FROM syllabus WHERE subject_name LIKE ? AND unit_number LIKE ?", 
#                        (f"%{subject}%", f"%{unit}%"))
#     else:
#         cursor.execute("SELECT unit_number, unit_title, topics FROM syllabus WHERE subject_name LIKE ?", 
#                        (f"%{subject}%",))
#     rows = cursor.fetchall()
#     conn.close()
#     if not rows:
#         return "No syllabus found for that subject or unit."
#     return "\n\n".join([f"{unit} — {title}\n{topics}" for unit, title, topics in rows])

# def get_lab_programs(subject):
#     conn = sqlite3.connect("data.db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT program_list FROM labs WHERE lab_name LIKE ?", (f"%{subject}%",))
#     row = cursor.fetchone()
#     conn.close()
#     if not row:
#         return "No lab programs found for that subject."
#     return row[0]

# def handle_query(query):
#     query = query.lower()

#     # Exams
#     if re.search(r'\bexam\b|\btest\b|\bmid\b|\bend term\b', query):
#         return get_exam_info()

#     # Faculty info
#     elif re.search(r'\bfaculty\b|\bteacher\b|\bprofessor\b|\bstaff\b', query):
#         return get_faculty_info()

#     # Email
#     elif "email" in query and any(x in query for x in ["dr", "prof", "sir", "madam"]):
#         match = re.search(r'email.*?(dr\.?|prof\.?|sir|madam)?\s*([a-z\s]+)', query)
#         if match:
#             name = match.group(2).strip().title()
#             return get_professor_email(name)

#     # Who teaches what (improved multi-word + fuzzy subject matching)
#     elif re.search(r'(who teaches|professor.*for|faculty.*for|which professor.*teaches)', query):
#         conn = sqlite3.connect("data.db")
#         cursor = conn.cursor()
#         cursor.execute("SELECT DISTINCT subject_name FROM syllabus")
#         subjects = [row[0] for row in cursor.fetchall()]
#         conn.close()

#         matched_subject = None
#         query_lower = query.lower()

#         # Check if any subject phrase is a substring of the query
#         for subj in subjects:
#             if subj.lower() in query_lower:
#                 matched_subject = subj
#                 break

#         # Fallback: fuzzy match the full query against subjects
#         if not matched_subject:
#             import difflib
#             match = difflib.get_close_matches(query_lower, [s.lower() for s in subjects], n=1, cutoff=0.6)
#             if match:
#                 for s in subjects:
#                     if s.lower() == match[0]:
#                         matched_subject = s
#                         break

#         if matched_subject:
#             return get_professor_by_subject_from_faculty(matched_subject)

#         return "I couldn't match the subject. Try again using a more specific course name."

#     # Assignments
#     elif re.search(r'\bassignments?\b|\bdeadlines?\b|\bsubmit(ting|s)?\b', query):
#         return get_assignments()

#     # Today's schedule
#     elif "today" in query and "class" in query:
#         return get_today_schedule()

#     # Specific day schedule
#     elif any(day in query for day in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]):
#         for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]:
#             if day.lower() in query:
#                 return get_schedule_by_day(day)

#     # Faculty-specific class queries
#     elif "class" in query and "by" in query:
#         match = re.search(r'class(?:es)? by (dr\.?\s\w+|prof\.?\s\w+|\w+)', query)
#         if match:
#             faculty_name = match.group(1).strip().title()
#             return get_schedule_by_faculty(faculty_name)

#     # Syllabus queries
#     elif "syllabus" in query or "unit" in query:
#         match = re.search(r"(unit\s+\w+)?\s*(of|for)?\s*(\w[\w\s]+)", query)
#         if match:
#             unit = match.group(1).strip().title() if match.group(1) else None
#             subject = match.group(3).strip().title()
#             return get_syllabus(subject, unit)

#     # Lab programs
#     elif "lab" in query and ("program" in query or "experiment" in query or "list" in query):
#         match = re.search(r"([\w\s]+)", query)
#         if match:
#             subject = match.group(1).strip().title()
#             return get_lab_programs(subject)

#     # General schedule
#     elif re.search(r'\b(class|timetable|schedule)\b', query):
#         return get_schedule()

#     elif query in ['exit', 'quit']:
#         return "Goodbye!"

#     return "I didn't quite get that. Try asking about exams, schedule, assignments, or faculty."



# FINAL VERSION OF CHATBOT
import sqlite3
import re
from datetime import datetime

# Store user context globally
user_course = ""
user_year = ""

# ---------------------- EXAMS ----------------------

def get_exam_info():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT subject, exam_type, date, time, venue FROM exams WHERE LOWER(course) LIKE ? AND LOWER(year) LIKE ? ORDER BY date",
        (f"%{user_course.lower()}%", f"%{user_year.lower()}%"))
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        return "No exam data found for your course and year."

    return "\n".join([
        f"{subject} ({exam_type}) on {date} at {time} in {venue}"
        for subject, exam_type, date, time, venue in rows
    ])

def get_exam_info_by_type(exam_type):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT subject, date, time, venue FROM exams WHERE LOWER(course) LIKE ? AND LOWER(year) LIKE ? AND exam_type = ? ORDER BY date",
        (f"%{user_course.lower()}%", f"%{user_year.lower()}%", exam_type))
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        return f"No {exam_type} schedule found for your course and year."

    return f"{exam_type} Schedule:\n" + "\n".join([
        f"{subject} on {date} at {time} in {venue}"
        for subject, date, time, venue in rows
    ])

def get_exam_date_by_subject(subject):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT exam_type, date, time, venue FROM exams WHERE LOWER(subject) LIKE ? AND LOWER(course) LIKE ? AND LOWER(year) LIKE ? ORDER BY date",
        (f"%{subject.lower()}%", user_course.lower(), user_year.lower()))
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        return f"No exams found for {subject}."

    return f"{subject} exams:\n" + "\n".join([
        f"{exam_type} on {date} at {time} in {venue}"
        for exam_type, date, time, venue in rows
    ])

# ---------------------- FACULTY ----------------------

def get_faculty_info():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, department, designation, email FROM faculty")
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        return "No faculty data found."

    return "\n".join([f"{name} ({designation}, {department}) — {email}" for name, department, designation, email in rows])

def get_professor_email(name):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT email FROM faculty WHERE name LIKE ?", (f"%{name}%",))
    row = cursor.fetchone()
    conn.close()

    if not row:
        return f"Email for {name} not found."
    return f"Email of {name} is {row[0]}"

def get_professor_by_subject_from_faculty(subject_name):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM faculty WHERE courses_taught LIKE ?", (f"%{subject_name}%",))
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        return f"No professor found teaching {subject_name}."

    return f"{subject_name} is taught by: " + ", ".join([name for (name,) in rows])

def get_student_coordinator():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, email FROM faculty WHERE courses_taught LIKE '%Student Co-ordinator%'")
    row = cursor.fetchone()
    conn.close()

    if not row:
        return "No student co-ordinator found."
    return f"Your student co-ordinator is {row[0]} \nEmail: {row[1] if row[1] else 'Not available'}"

# ---------------------- ASSIGNMENTS ----------------------

def get_assignments(subject=None):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    if subject:
        cursor.execute(
            "SELECT subject, assignment_title, deadline FROM assignments WHERE course = ? AND LOWER(subject) LIKE ? ORDER BY deadline",
            (user_course, f"%{subject.lower()}%",)
        )
    else:
        cursor.execute(
            "SELECT subject, assignment_title, deadline FROM assignments WHERE course = ? ORDER BY deadline",
            (user_course,)
        )

    rows = cursor.fetchall()
    conn.close()

    if not rows:
        return "No assignment deadlines found for that subject." if subject else "No assignment deadlines found for your course."

    return "\n".join([f"{subject}: {assignment_title} due by {deadline}" for subject, assignment_title, deadline in rows])

# ---------------------- SCHEDULE ----------------------

def get_schedule():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT day, subject, time, room, faculty FROM schedule WHERE course = ? AND year = ? ORDER BY day",
                   (user_course, user_year))
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        return "No schedule found for your course and year."

    return "\n".join([f"{day}: {subject} at {time} in {room} (by {faculty})" for day, subject, time, room, faculty in rows])

def get_today_schedule():
    today = datetime.now().strftime("%A")
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT subject, time, room, faculty FROM schedule WHERE course = ? AND year = ? AND day = ?",
                   (user_course, user_year, today))
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        return f"No classes scheduled for today ({today})."

    return "\n".join([f"{subject} at {time} in {room} (by {faculty})" for subject, time, room, faculty in rows])

def get_schedule_by_day(day):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT subject, time, room, faculty FROM schedule WHERE course = ? AND year = ? AND day = ?",
                   (user_course, user_year, day))
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        return f"No classes scheduled on {day}."

    return "\n".join([f"{subject} at {time} in {room} (by {faculty})" for subject, time, room, faculty in rows])

def get_schedule_by_faculty(faculty_name):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT day, subject, time, room FROM schedule WHERE course = ? AND year = ? AND faculty LIKE ?",
                   (user_course, user_year, f"%{faculty_name}%"))
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        return f"No classes found taught by {faculty_name}."

    return "\n".join([f"{day}: {subject} at {time} in {room}" for day, subject, time, room in rows])

# ---------------------- SYLLABUS ----------------------

def get_syllabus(subject, unit=None):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    if unit:
        cursor.execute(
            "SELECT unit_number, unit_title, topics FROM syllabus WHERE subject_name LIKE ? AND unit_number LIKE ?",
            (f"%{subject}%", f"%{unit}%"))
    else:
        cursor.execute(
            "SELECT unit_number, unit_title, topics FROM syllabus WHERE subject_name LIKE ?",
            (f"%{subject}%",))
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        return "No syllabus found for that subject or unit."

    seen = set()
    formatted_units = []
    for unit, title, topics in rows:
        key = f"{unit.strip()} — {title.strip()}"
        if key not in seen:
            seen.add(key)
            formatted_units.append(f"{key}\n{topics.strip()}")

    return "\n\n".join(formatted_units)

# ---------------------- LABS ----------------------

def get_lab_programs(subject):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT program_list FROM labs WHERE lab_name LIKE ?", (f"%{subject}%",))
    row = cursor.fetchone()
    conn.close()

    if not row:
        return "No lab programs found for that subject."
    return row[0]

# ---------------------- HOLIDAYS ----------------------

def get_holidays_by_month(month_name):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    try:
        month_num = datetime.strptime(month_name[:3], "%b").month
    except ValueError:
        return f"'{month_name}' is not a valid month."

    cursor.execute("SELECT name, start_date, end_date, type FROM holidays")
    rows = cursor.fetchall()
    conn.close()

    matched = []
    for name, start, end, htype in rows:
        try:
            s_month = datetime.strptime(start, "%Y-%m-%d").month
        except ValueError:
            continue

        if s_month == month_num:
            if start == end:
                matched.append(f"{name} on {start} ({htype})")
            else:
                matched.append(f"{name} from {start} to {end} ({htype})")

    if not matched:
        return f"No holidays found in {month_name.title()}."

    return f"Holidays in {month_name.title()}:\n" + "\n".join(matched)

def get_all_holidays():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, start_date, end_date, type FROM holidays ORDER BY start_date")
    rows = cursor.fetchall()
    conn.close()

    return "\n".join([
        f"{name} on {start} ({htype})" if start == end else f"{name} from {start} to {end} ({htype})"
        for name, start, end, htype in rows
    ])

def get_holiday_by_name(keyword):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, start_date, end_date, type FROM holidays WHERE LOWER(name) LIKE ?", (f"%{keyword.lower()}%",))
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        return f"No holiday found for {keyword}."

    return "\n".join([
        f"{name} on {start} ({htype})" if start == end else f"{name} from {start} to {end} ({htype})"
        for name, start, end, htype in rows
    ])

# ---------------------- HANDLE QUERY ----------------------

def handle_query(query):
    query = query.lower()

    # Subject-specific exams
    if "when is" in query and "exam" in query:
        match = re.search(r'when is (.+?) exam', query)
        if match:
            subject = match.group(1).replace("end sem", "").strip().title()
            return get_exam_date_by_subject(subject)

    # Holiday queries
    if "show all holidays" in query or "list all holidays" in query:
        return get_all_holidays()

    elif "holidays this month" in query:
        current_month = datetime.now().strftime("%B")
        return get_holidays_by_month(current_month)

    elif re.search(r"holidays? (in|for) (\w+)", query):
        match = re.search(r"holidays? (in|for) (\w+)", query)
        if match:
            return get_holidays_by_month(match.group(2))

    elif re.search(r"(vacation|holiday).*?(sankranthi|dussehra|summer|diwali|christmas)", query):
        match = re.search(r"(sankranthi|dussehra|summer|diwali|christmas)", query)
        if match:
            return get_holiday_by_name(match.group(1))

    # Exam types
    if any(p in query for p in ["class test ii", "ct2", "class test 2"]):
        return get_exam_info_by_type("Class Test II")
    elif any(p in query for p in ["class test i", "ct1", "class test 1"]):
        return get_exam_info_by_type("Class Test I")
    elif any(p in query for p in ["end semester", "end sem", "finals", "final exam"]):
        return get_exam_info_by_type("End Semester")
    elif any(p in query for p in ["exam", "test", "exam timetable", "exam schedule", "do i have exams"]):
        return get_exam_info()

    # Faculty
    elif re.search(r'\bfaculty\b|\bteacher\b|\bprofessor\b|\bstaff\b', query):
        return get_faculty_info()

    elif re.search(r'email.*(dr\.?|prof\.?|\b)[a-z]+', query):
        match = re.search(r'email.*(dr\.?|prof\.?|\b)([a-z ]+)', query)
        if match:
            name = match.group(2).strip().title()
            return get_professor_email(name)

    elif re.search(r'(who teaches|professor.*for|faculty.*for|which professor.*teaches)', query):
        match = re.search(r'(soft computing|advanced databases|natural language processing|big data analytics|disaster mitigation|operating systems|machine learning|network security)', query)
        if match:
            subject_name = match.group(1).strip().title()
            return get_professor_by_subject_from_faculty(subject_name)

    elif re.search(r'\bstudent co\[- ]?ordinator\b|\bcoordinator\b', query):
        return get_student_coordinator()

    # Assignments
    elif re.search(r'\bassignments?\b|\bdeadlines?\b|\bsubmit(ting|s)?\b', query):
        # List of valid subjects to check for
        subjects = ["natural language processing", "advanced databases", "big data analytics", "soft computing"]

        for subj in subjects:
            if subj in query.lower():
                return get_assignments(subject=subj)
        
        # Default to all assignments
        return get_assignments()


    # Class schedule
    elif "today" in query and "class" in query:
        return get_today_schedule()

    elif any(day in query for day in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]):
        for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]:
            if day.lower() in query:
                return get_schedule_by_day(day)

    elif "class" in query and "by" in query:
        match = re.search(r'class(?:es)? by (dr\.?\s\w+|prof\.?\s\w+|\w+)', query)
        if match:
            faculty_name = match.group(1).strip().title()
            return get_schedule_by_faculty(faculty_name)

    # Syllabus
    elif "syllabus" in query or "unit" in query:
        match = re.search(r"(unit\s+\w+)?\s*(of|for)?\s*(advanced databases|soft computing|big data analytics|natural language processing|disaster mitigation)", query)
        if match:
            unit = match.group(1).strip().title() if match.group(1) else None
            subject = match.group(3).strip().title()
            return get_syllabus(subject, unit)

    # Lab programs
    elif "lab" in query and ("program" in query or "experiment" in query or "list" in query):
        match = re.search(r"(advanced databases( and soft computing)?|big data analytics|mini project)", query)
        if match:
            subject = match.group(1).strip().title()
            return get_lab_programs(subject)

    elif re.search(r'\b(class|timetable|schedule)\b', query):
        return get_schedule()

    elif query in ['exit', 'quit']:
        return "Goodbye!"

    return "I didn't quite get that. Try asking about exams, schedule, holidays, or faculty."

# ---------------------- MAIN ----------------------

if __name__ == "__main__":
    print("👨‍🎓 Welcome to the Student Helpdesk Chatbot!")
    user_course = input("Enter your course (e.g., MTECH): ").strip()
    user_year = input("Enter your year (e.g., 1st Year): ").strip()

    print("\nReady! Ask me about exams, holidays, classes, or assignments.")
    while True:
        q = input("You: ")
        if q.lower() in ["exit", "quit"]:
            print("Bot: Goodbye!")
            break
        print("Bot:", handle_query(q))
