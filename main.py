from conect import *
from create_table import *
from create_data_table import *
from show_func import*
from show_func_data import*

connection = create_connection(
    "postgres", "admin", "root", "127.0.0.1", "5432"
)

execute_query(connection, create_students_table)
execute_query(connection, create_subjects_table)
execute_query(connection, create_exams_table)

cur = connection.cursor()

# add_data(cur)
# execute_queries(cur)
data(cur)