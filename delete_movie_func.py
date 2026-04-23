from show_movies_func import show_movies
# =========================
# 4. УДАЛИТЬ ФИЛЬМ
# =========================
def delete_movie(movies):
    show_movies(movies)
    try:
        num = int(input("Номер фильма для удаления: "))
        movies.pop(num - 1)
        print("Удалено\n")
    except:
        print("Ошибка\n")