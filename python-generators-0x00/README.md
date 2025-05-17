# ALX_prodev MySQL Setup

This project sets up a MySQL database named `ALX_prodev`, creates a `user_data` table, and populates it with data from a CSV file (`user_data.csv`).

## 📦 Requirements

- Python 3.x
- MySQL Server
- `mysql-connector-python` package

Install the MySQL connector for Python:

```bash
pip install mysql-connector-python
```

## 🧰 File Structure

```
├── user_data.csv         # CSV file containing user info (name, email, age)
├── setup_database.py     # Python script to create DB, table, and insert data
└── README.md             # This documentation
```

## 📁 CSV Format

The `user_data.csv` file should **not** include a UUID. It should have the following columns:

```
name,email,age
Alice,alice@example.com,28
Bob,bob@example.com,35
...
```

## ⚙️ What the Script Does

1. Connects to the MySQL server.
2. Creates the `ALX_prodev` database (if it doesn't exist).
3. Connects to the `ALX_prodev` database.
4. Creates the `user_data` table (if it doesn't exist) with the following fields:
    - `user_id` (UUID, Primary Key, Indexed)
    - `name` (VARCHAR, Not Null)
    - `email` (VARCHAR, Not Null)
    - `age` (DECIMAL, Not Null)
5. Generates a UUID for each row of data from the CSV.
6. Inserts the data into the table using bulk insertion.
7. Updates existing entries on conflict (by `user_id`).

## 🚀 Running the Script

Update `setup_database.py` with your MySQL credentials, then run:

```bash
python seed.py
```

## ✍️ Author

Nehemiah Mekonnen

## 🛡 License

MIT License (if applicable)