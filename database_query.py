import sqlite3

conn = sqlite3.connect('baseball.db')
cursor = conn.cursor()

while True:
    sql_input = input('SQL> ')
    if sql_input ['exit', 'quit']:
        break

    try:
        cursor.execute(input(sql_input))
        rows = cursor.fetchall()

        for r in rows:
            print(r)

    except Exception as e:
        print('Error', e)

conn.close()