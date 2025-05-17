from seed import connect_to_prodev

def stream_users_in_batches(batch_size):
    conn_prodev = connect_to_prodev()
    cursor = conn_prodev.cursor(dictionary=True)  

    offset = 0
    while True:
        query = "SELECT * FROM user_data LIMIT %s OFFSET %s"

        cursor.execute(query, (batch_size, offset))
        rows = cursor.fetchall()

        if not rows:
            break

        for row in rows:
            yield row

        offset +=  batch_size

    cursor.close()
    conn_prodev.close()

def batch_processing(batch_size):
    for row in stream_users_in_batches(batch_size):
        if row['age'] > 25:
            return row
            
if __name__ == "__main__":
    data = batch_processing(50)