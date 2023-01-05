import psycopg2

username = 'postgres'
password = 'Minnkko1'
database = 'dota'
host = 'localhost'
port = '5432'

query1 = '''
SELECT category.hero_category, COUNT(heroes.category_id) FROM heroes
JOIN category ON category.category_id = heroes.category_id GROUP BY hero_category
'''

query2 = '''
SELECT roles.hero_role, COUNT(heroes.role_id) FROM heroes
JOIN roles ON roles.role_id = heroes.role_id GROUP BY hero_role
'''

query3 = '''
SELECT hero_name, hero_intelligence FROM heroes
WHERE category_id = 1 ORDER BY hero_strenght DESC
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
print(type(conn))

with conn:

    print ("\nDatabase opened successfully\n")
    cur = conn.cursor()

    print('1. Кількість персонажів кожної категорії\n')
    cur.execute(query1)
    for row in cur:
        print(row)

    print('\n2. Кількість персонажів кожної ролі\n')
    cur.execute(query2)
    for row in cur:
        print(row)

    print('\n3. Показник інтелекту у кожного сильного персонажа\n')
    cur.execute(query3)
    for row in cur:
        print(row)