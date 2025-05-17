from seed import connect_to_prodev

def stream_users():
    conn_prodev = connect_to_prodev()
    cursor = conn_prodev.cursor(dictionary=True)  
    query = """
            select * from user_data;
            """
    try:
        cursor.execute(query)
    except Exception as e:
        print(e)

    for row in cursor:
        yield row

    cursor.close()
    conn_prodev.close()


if __name__ == "__main__":
    data = stream_users()