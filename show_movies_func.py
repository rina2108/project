# =========================
# 1. ПОКАЗАТЬ СПИСОК
# =========================
def show_movies(movies):
    if not movies:
        print("\nСписок пуст\n")
    else:
        print("\nСписок фильмов:")
        for i, movie in enumerate(movies):
            status = "✔" if movie["watched"] else "✘"
            print(f"{i + 1}. [{status}] {movie['title']}")
        print()