import psycopg

# Connect to an existing database
with psycopg.connect("dbname=postgres user=postgres host=localhost port=5432 password=qwerty2007 ",) as conn:

    conn.autocommit = True

    # Open a cursor to perform database operations
    with conn.cursor() as cur:

        sql = "DROP DATABASE your_db"

        cur.execute(sql)
        print("Drop Database !!")

        conn.commit()