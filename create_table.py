

create_students_table = ("""
    CREATE TABLE IF NOT EXISTS Фільми (
        Код_фільму SERIAL PRIMARY KEY,
        Назва_фільму VARCHAR(255) NOT NULL,
        Жанр VARCHAR(50) NOT NULL,
        Тривалість INTEGER NOT NULL,
        Рейтинг FLOAT NOT NULL
    )
""")

# Створення таблиці "Кінотеатри"
create_subjects_table= ("""
    CREATE TABLE IF NOT EXISTS Кінотеатри (
    Код_кінотеатру SERIAL PRIMARY KEY,
    Назва_кінотеатру VARCHAR(255) NOT NULL,
    Ціни_на_квитки DECIMAL NOT NULL,
    Кількість_місць INTEGER NOT NULL,
    Адреса VARCHAR(255) NOT NULL,
    Телефон VARCHAR(12) CHECK (Телефон ~ '^\d{12}$') NOT NULL
);
""")

# Створення таблиці "Транслювання_фільмів"
create_exams_table =("""
    CREATE TABLE IF NOT EXISTS Транслювання_фільмів (
        Код_транслювання SERIAL PRIMARY KEY,
        Код_фільму INTEGER REFERENCES Фільми(Код_фільму),
        Код_кінотеатру INTEGER REFERENCES Кінотеатри(Код_кінотеатру),
        Дата_початку_показів DATE NOT NULL,
       "Термін показу (кількість днів)" INTEGER NOT NULL 
    )
""")
