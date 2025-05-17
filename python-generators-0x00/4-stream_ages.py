from seed import connect_to_prodev

def stream_user_ages():
    conn_prodev = connect_to_prodev()
    cursor = conn_prodev.cursor(dictionary=True)  

    query = "SELECT age FROM user_data"

    cursor.execute(query)

    for row in cursor:
        yield row

    cursor.close()
    conn_prodev.close()

def calculate_average_age():
    total = 0
    amount = 0
    for row in stream_user_ages():
        total += row['age']
        amount += 1
    
    average = total / amount

    print('Average age of users:', average)

calculate_average_age()