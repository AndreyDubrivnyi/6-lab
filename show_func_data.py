from psycopg2 import sql
from tabulate import tabulate

def data(cur):
    tables = ["Фільми", "Кінотеатри", "Транслювання_фільмів"]
    for table in tables:
        display_table_data(table, cur)

def display_table_data(table_name, cursor):
    
    # Вивести структуру таблиці
    cursor.execute(f"SELECT column_name, data_type FROM information_schema.columns WHERE table_name = '{table_name}'")
    columns_info = cursor.fetchall()
    print(f"\nСтруктура таблиці {table_name}:")
    table_structure = tabulate(columns_info, headers=["Column", "Data Type"], tablefmt="grid")
    print(table_structure)

    # Вивести дані з таблиці
    cursor.execute(sql.SQL("SELECT * FROM {}").format(sql.Identifier(table_name)))
    data = cursor.fetchall()
    print(f"\nДані в таблиці {table_name}:")
    table_data = tabulate(data, headers=[desc[0] for desc in cursor.description], tablefmt="grid")
    print(table_data)