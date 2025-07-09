import sqlite3

# Connect to SQLite database (or create if it doesn't exist)
conn = sqlite3.connect('student.db')
cursor = conn.cursor()

# Create student table
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    branch TEXT NOT NULL,
    marks INTEGER NOT NULL
)
''')

def add_student():
    id = int(input("Enter ID: "))
    name = input("Enter Name: ")
    branch = input("Enter Branch: ")
    marks = int(input("Enter Marks: "))
    cursor.execute("INSERT INTO students VALUES (?, ?, ?, ?)", (id, name, branch, marks))
    conn.commit()
    print("Student added successfully!")

def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def update_marks():
    id = int(input("Enter student ID to update: "))
    new_marks = int(input("Enter new marks: "))
    cursor.execute("UPDATE students SET marks = ? WHERE id = ?", (new_marks, id))
    conn.commit()
    print("Marks updated.")

def delete_student():
    id = int(input("Enter student ID to delete: "))
    cursor.execute("DELETE FROM students WHERE id = ?", (id,))
    conn.commit()
    print("Student deleted.")

def menu():
    while True:
        print("\n--- Student Database ---")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Update Marks")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            update_marks()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            break
        else:
            print("Invalid choice.")

menu()
conn.close()
