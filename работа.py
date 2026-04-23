# =========================
# ХРАНЕНИЕ ФИЛЬМОВ
# =========================
movies = []  # список фильмов

# =========================
# 1. ПОКАЗАТЬ СПИСОК
# =========================
def show_movies():
    if not movies:
        print("\nСписок пуст\n")
    else:
        print("\nСписок фильмов:")
        for i, movie in enumerate(movies):
            status = "✔" if movie["watched"] else "✘"
            print(f"{i + 1}. [{status}] {movie['title']}")
        print()

# =========================
# 2. ДОБАВИТЬ ФИЛЬМ
# =========================
def add_movie():
    title = input("Введите название фильма: ")
    movies.append({
        "title": title,
        "watched": False
    })
    print("Фильм добавлен\n")

# =========================
# 3. ОТМЕТИТЬ ПРОСМОТРЕННЫМ
# =========================
def mark_watched():
    show_movies()
    try:
        num = int(input("Номер просмотренного фильма: "))
        movies[num - 1]["watched"] = True
        print("Отмечено как просмотрено\n")
    except:
        print("Ошибка\n")

# =========================
# 4. УДАЛИТЬ ФИЛЬМ
# =========================
def delete_movie():
    show_movies()
    try:
        num = int(input("Номер фильма для удаления: "))
        movies.pop(num - 1)
        print("Удалено\n")
    except:
        print("Ошибка\n")

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
            show_movies()
        elif choice == "2":
            add_movie()
        elif choice == "3":
            mark_watched()
        elif choice == "4":
            delete_movie()
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