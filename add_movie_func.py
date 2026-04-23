# =========================
# 2. ДОБАВИТЬ ФИЛЬМ
# =========================
def add_movie(movies):
    title = input("Введите название фильма: ")
    movies.append({
        "title": title,
        "watched": False
    })
    print("Фильм добавлен\n")