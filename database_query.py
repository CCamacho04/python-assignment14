import sqlite3

conn = sqlite3.connect('baseball.db')
cursor = conn.cursor()

while True:
    if input('SQL> ') in ['exit', 'quit']:
        break

    try:
        cursor.execute(input('SQL> '))
        rows = cursor.fetchall()

        for r in rows:
            print(r)

    except Exception as e:
        print('Error', e)

conn.close()