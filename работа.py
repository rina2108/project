from delete_movie_func import delete_movie
from mark_watched_func import mark_watched
from show_movies_func import show_movies
from add_movie_func import add_movie

# =========================
# ХРАНЕНИЕ ФИЛЬМОВ
# =========================
movies = []  # список фильмов

# =========================
# ГЛАВНОЕ МЕНЮ
# =========================
def main():
    while True:
        print("=== MOVIE LIST ===")
        print("1. Показать список")
        print("2. Добавить фильм")
        print("3. Отметить просмотренным")
        print("4. Удалить фильм")
        print("5. Выход")

        choice = input("Выбери действие: ")

        if choice == "1":
            show_movies(movies)
        elif choice == "2":
            add_movie(movies)
        elif choice == "3":
            mark_watched(movies)
        elif choice == "4":
            delete_movie(movies)
        elif choice == "5":
            print("Пока!")
            break
        else:
            print("Неверный выбор\n")

# =========================
# ЗАПУСК
# =========================
if __name__ == "__main__":
    main()