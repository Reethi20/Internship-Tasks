import sqlite3

def fetch_records():
    conn = sqlite3.connect("sqlDatabase.db")
    cursor = conn.cursor()

    print("Users Table:")
    cursor.execute("SELECT * FROM Users")
    users = cursor.fetchall()
    for user in users:
        print(user)

    print("\nStudents Table:")
    cursor.execute("SELECT * FROM Students")
    students = cursor.fetchall()
    for student in students:
        print(student)

    print("\nTasks Table:")
    cursor.execute("SELECT * FROM Tasks")
    tasks = cursor.fetchall()
    for task in tasks:
        print(task)

    conn.close()

if __name__ == "__main__":
    fetch_records()