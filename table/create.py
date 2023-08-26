import psycopg

# Connect to an existing database
with psycopg.connect("dbname=postgres user=postgres host=localhost port=5432 password=qwerty2007 ",) as conn:

    conn.autocommit = True

    # Open a cursor to perform database operations
    with conn.cursor() as cur:

        sql = '''CREATE TABLE my_table(
            id SERIAL PRIMARY KEY,
            name VARCHAR(255)
        )'''

        cur.execute(sql)
        print("Create table !!")

        conn.commit()