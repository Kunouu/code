import psycopg2
connect = psycopg2.connect(host = 'localhost',
                        database = 'university',
                        user = 'postgres',
                        password = '12345678',
                        port = '5432'
                        )
cur = connect.cursor()
cur.execute('SELECT first_name FROM university ORDER BY first_name ASC LIMIT 15')
usernames = [r[0] for r in cur.fetchall()]
# Found= False
# while not Found:
#     username = input('Введите ваш логин:')
#     if username in usernames:
#         print('Вы есть в списке')
#         Found=True
#     else:
#         print('К сожалению мы не смогли вас найти!')
def binary_search(username):
    return True
    return False


connect.commit()
cur.close()
connect.close()
