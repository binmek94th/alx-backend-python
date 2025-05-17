import mysql.connector
import csv
import uuid

def connect_db():
    return mysql.connector.connect(
  host="localhost",
  user="root",
  password="1QAZ2wsx@"
)


def create_database(connection):
    cursor = connection.cursor()
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
        print("Database created or already exists.")
    except mysql.connector.Error as err:
        print("Failed creating database:", err)
    cursor.close()

def connect_to_prodev():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1QAZ2wsx@",
        database="ALX_prodev"
    )

def create_table(connection):
    cursor = connection.cursor()
    table_sql = """
    CREATE TABLE IF NOT EXISTS user_data (
        user_id CHAR(36) PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        age DECIMAL NOT NULL,
        INDEX(user_id)
    )
    """
    try:
        cursor.execute(table_sql)
        print("Table created or already exists.")
    except mysql.connector.Error as err:
        print("Failed creating table:", err)
    cursor.close()

def insert_data(connection, data):
    cursor = connection.cursor()
    insert_query = """
    INSERT INTO user_data (user_id, name, email, age)
    VALUES (%s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE name=VALUES(name), email=VALUES(email), age=VALUES(age)
    """
    try:
        cursor.executemany(insert_query, data)
        connection.commit()
        print(f"{cursor.rowcount} rows inserted or updated.")
    except mysql.connector.Error as err:
        print("Error inserting data:", err)
    cursor.close()

def read_csv(filepath):
    with open(filepath, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return [
            (str(uuid.uuid4()), row["name"], row["email"], row["age"])
            for row in reader
        ]


if __name__ == "__main__":
    try:
        conn = connect_db()
        create_database(conn)
        conn.close()

        conn_prodev = connect_to_prodev()
        create_table(conn_prodev)

        data = read_csv("user_data.csv")
        insert_data(conn_prodev, data)

        conn_prodev.close()

    except mysql.connector.Error as err:
        print("Database error:", err)