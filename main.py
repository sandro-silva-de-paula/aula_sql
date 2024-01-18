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
    # with connection.cursor() as cursor:
    #     # sql
    #     sql = (f'INSERT INTO {TABLE_NAME}  (nome, idade) VALUES (%s, %s) ')
    #     data = ('Alissa', 29)
    #     # nao enviar valores junto com a string do sql / injection sql
    #     result = cursor.execute(sql, data)

    #     print(result)
    #     print(sql, data)
    # connection.commit()

    # Inserir dados na tabela vindo de um dic
    # with connection.cursor() as cursor:
    #     # sql
    #     sql = (
    #         f'INSERT INTO {TABLE_NAME}  (nome, idade) VALUES (%(nome)s, %(idade)s) ')
    #     data_dic = {
    #         "nome": "Ilseu",
    #         "idade": 62,
    #     }
    #     # nao enviar valores junto com a string do sql / injection sql
    #     result = cursor.execute(sql, data_dic)

    #     print(result)
    #     print(sql, data_dic)
    # connection.commit()

    # Inserir VARIOS dados na tabela vindo de um dic
    # with connection.cursor() as cursor:
    #     # sql
    #     sql = (
    #         f'INSERT INTO {TABLE_NAME}  (nome, idade) VALUES (%(nome)s, %(idade)s) ')
    #     data_dic = (
    #         {"nome": "Evani", "idade": 65, },
    #         {"nome": "Patricia", "idade": 43, },
    #         {"nome": "Toninho", "idade": 65, },
    #         {"nome": "Valmir", "idade": 59, },
    #     )
    #     # nao enviar valores junto com a string do sql / injection sql
    #     result = cursor.executemany(sql, data_dic)

    #     print(result)
    #     print(sql, data_dic)
    # connection.commit()

    # Lendo valores com SELECT
    # with connection.cursor() as cursor:
    #     # sql
    #     id_busca = 3
    #     sql = (f'SELECT idade, nome FROM {TABLE_NAME} '
    #            'WHERE  id=%s ')
    #     cursor.execute(sql, id_busca)
    #     lista_dados = cursor.fetchall()
    #     for row in lista_dados:
    #         print(row)
    #     print(len(lista_dados))
    #     print(cursor.mogrify(sql, id_busca))  # mostar o comando sql

    # Deletando registro
    # with connection.cursor() as cursor:
    #     # sql
    #     id_busca = 10
    #     sql = (f'DELETE FROM {TABLE_NAME} '
    #            'WHERE  id=%s ')
    #     print(cursor.execute(sql, id_busca))
    #     connection.commit()

    #     print(cursor.mogrify(sql, id_busca))  # mostar o comando sql

    # Editando registro
    with connection.cursor() as cursor:
        # sql
        id_busca = 2
        New_nome = 'Sandro Silva '
        sql = (f'UPDATE  {TABLE_NAME} SET nome = %s WHERE  id=%s ')
        print(cursor.execute(sql, (New_nome, id_busca)))
        connection.commit()

        # mostar o comando sql
        print(cursor.mogrify(sql, (New_nome, id_busca)))
