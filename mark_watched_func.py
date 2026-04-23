from show_movies_func import show_movies
# =========================
# 3. ОТМЕТИТЬ ПРОСМОТРЕННЫМ
# =========================
def mark_watched(movies):
    show_movies(movies)
    try:
        num = int(input("Номер просмотренного фильма: "))
        movies[num - 1]["watched"] = True
        print("Отмечено как просмотрено\n")
    except:
        print("Ошибка\n")
