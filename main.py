import pymysql
import dotenv
import os

dotenv.load_dotenv()
TABLE_NAME = 'customers'

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
)


with connection:
    with connection.cursor() as cursor:
        # sql
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'nome VARCHAR(55) NOT NULL, '
            'idade INT NOT NULL, '
            'PRIMARY KEY (id)'
            ') '
        )
    connection.commit()

    # Inserir dados na tgabela
    with connection.cursor() as cursor:
        # sql
        sql = (f'INSERT INTO {TABLE_NAME}  (nome, idade) VALUES (%s, %s) ')
        data = ('Alissa', 29)
        # nao enviar valores junto com a string do sql / injection sql
        result = cursor.execute(sql, data)

        print(result)
        print(sql, data)
    connection.commit()
