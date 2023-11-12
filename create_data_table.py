from random import randint, choice
from datetime import date, timedelta

# Функція для заповнення таблиці Фільми
def add_data(cur):
    films = [
        ("Левеня", "Мелодрама", 120, 4.5),
        ("Один в Дома", "Комедія", 90, 3.8),
        ("Рембо", "Бойовик", 110, 4.2),
        ("Титанік", "Мелодрама", 195, 4.8),
        ("Шрек", "Комедія", 92, 4.6),
        ("Матриця", "Бойовик", 136, 4.3),
        ("Дневник Бріджит Джонс", "Мелодрама", 97, 3.9),
        ("Дюнкерк", "Бойовик", 106, 4.7),
        ("Дурні поведінки", "Комедія", 100, 3.5),
        ("Тінь батька", "Мелодрама", 115, 4.0),
        ("Шоу Трумана", "Комедія", 103, 4.4),
    ]

    kinoteatri = [
        ("Муltiplex", randint(15, 40) * 10, 100, "Heroiv 11b", "380686813211"),
        ("Lavina", randint(15, 40) * 10, 80, "Lisova 4b", "380747843623"),
        ("Ocean Plaza", randint(15, 40) * 10, 120, "Svitla 11a", "380636457321"),
        # Add more kinoteatri as needed
    ]

    # Generate random dates for exams
    start_date = date(2023, 11, 1)
    exam_dates = [start_date + timedelta(days=randint(1, 30)) for _ in range(15)]

    # Sample data for Транслювання_фільмів
    translyuvannya_films = [
        (1, choice([1, 2, 3]), exam_dates[0], 4),
        (2, choice([1, 2, 3]), exam_dates[1], 2),
        (3, choice([1, 2, 3]), exam_dates[2], 7),
        (4, choice([1, 2, 3]), exam_dates[3], 3),
        (5, choice([1, 2, 3]), exam_dates[4], 5),
        (6, choice([1, 2, 3]), exam_dates[5], 6),
        (7, choice([1, 2, 3]), exam_dates[6], 2),
        (8, choice([1, 2, 3]), exam_dates[7], 5),
        (9, choice([1, 2, 3]), exam_dates[8], 4),
        (10, choice([1, 2, 3]), exam_dates[9], 7),
        (11, choice([1, 2, 3]), exam_dates[10], 3),
        (12, choice([1, 2, 3]), exam_dates[11], 6),
        (13, choice([1, 2, 3]), exam_dates[12], 4),
        (14, choice([1, 2, 3]), exam_dates[13], 5),
        (15, choice([1, 2, 3]), exam_dates[14], 6),
    ]

    # Insert data into the tables
    film_ids = []  # Зберігатиме ідентифікатори фільмів
    kinoteatr_ids = []  # Зберігатиме ідентифікатори кінотеатрів

    for film in films:
        cur.execute("INSERT INTO Фільми (Назва_фільму, Жанр, Тривалість, Рейтинг) VALUES (%s, %s, %s, %s) RETURNING Код_фільму", film)
        film_ids.append(cur.fetchone()[0])  # Отримуємо ідентифікатор доданого фільму і зберігаємо його

    for kinoteatr in kinoteatri:
        cur.execute("INSERT INTO Кінотеатри (Назва_кінотеатру, Ціни_на_квитки, Кількість_місць, Адреса, Телефон) VALUES (%s, %s, %s, %s, %s) RETURNING Код_кінотеатру", kinoteatr)
        kinoteatr_ids.append(cur.fetchone()[0])  # Отримуємо ідентифікатор доданого кінотеатру і зберігаємо його

    for i, exam in enumerate(translyuvannya_films):
        film_id = film_ids[i % len(film_ids)]  # Зациклюємо ідентифікатор фільму, щоб додати його двічі
        exam = (film_id, kinoteatr_ids[i % len(kinoteatr_ids)], exam[2], exam[3])  # Оновлюємо дані для транслювання фільму з новим ідентифікатором кінотеатру
        cur.execute("INSERT INTO Транслювання_фільмів (Код_фільму, Код_кінотеатру, Дата_початку_показів, \"Термін показу (кількість днів)\") VALUES (%s, %s, %s, %s)", exam)
