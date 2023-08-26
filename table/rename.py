import psycopg

# Connect to an existing database
with psycopg.connect("dbname=postgres user=postgres host=localhost port=5432 password=qwerty2007 ",) as conn:

    conn.autocommit = True

    # Open a cursor to perform database operations
    with conn.cursor() as cur:

        sql = "ALTER DATABASE my_table RENAME TO your_table"

        cur.execute(sql)
        print("Rename Database !!")

        conn.commit()