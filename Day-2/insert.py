import sqlite3
def insert_data():
    try:
        conn = sqlite3.connect("sqlDatabase.db")
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO Users (username, email, password) VALUES (?, ?, ?)",
            ("Reethi", "reethi@gmail.com", "12345")
        )
        cursor.execute(
            "INSERT INTO Students (name, course) VALUES (?, ?)",
            ("Reethi", "Python FullStack Development")
        )
        cursor.execute(
            "INSERT INTO Tasks (title, description, student_id) VALUES (?, ?, ?)",
            ("Database Setup", "Create SQLite database", 1)
        )

        conn.commit()
        print("Records inserted successfully!")

    except sqlite3.IntegrityError as e:
        print("Database error:", e)
    finally:
        conn.close()
if __name__ == "__main__":
    insert_data()