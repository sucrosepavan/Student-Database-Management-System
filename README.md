# 🎓 Student Database Management System

A simple Python project that uses SQLite to perform CRUD (Create, Read, Update, Delete) operations on student data.

## Features

- Add new student records
- View all students
- Update student marks
- Delete student by ID
- Uses SQLite (no installation needed)

## Technologies

- Python 3
- SQLite (via `sqlite3` module)

## How to Run

```bash
python student_db.py
```
Sample Table Schema
```
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    branch TEXT,
    marks INTEGER
);
```
 OUTPUT
 ```
--- Student Database ---
1. Add Student
2. View All Students
3. Update Marks
4. Delete Student
5. Exit
```
Author
P. Pavan Kumar reddy
Electrical and Electronics Engineering Graduate | Aspiring Python & SQL Developer

