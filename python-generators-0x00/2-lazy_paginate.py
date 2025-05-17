from seed import connect_to_prodev

def lazy_paginate(page_size):
    pass

def paginate_users(page_size, offset):
    conn_prodev = connect_to_prodev()
    cursor = conn_prodev.cursor(dictionary=True)  

    query = "SELECT * FROM user_data LIMIT %s OFFSET %s"
    cursor.execute(query, (page_size, offset))
    rows = cursor.fetchall()

    cursor.close()
    conn_prodev.close()

    return rows

def lazy_paginate(page_size):
    offset = 0

    while True:
        rows = paginate_users(page_size, offset)
        if not rows:
            break

        for row in rows:
            yield row

        offset += page_size

if __name__ == "__main__":
    for user in lazy_paginate(50):
        print(user)