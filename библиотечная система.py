import csv
library = {
    "Война и мир": {
        "author": "Л. Толстой",
        "year": 1869,
        "ratings": [5, 4, 5]
    },
    "Преступление и наказание": {
        "author": "Ф. Достоевский",
        "year": 1866,
        "ratings": [5, 5, 4]
    }
}


def show_menu():
    print("1. Добавить книгу")
    print("2. Показать все книги")
    print("3. Найти книгу по названию")
    print("4. Удалить книгу")
    print("5. Добавить новую оценку книге")
    print("6. Книги выпущенные после определённого года")
    print("7. Книги с рейтингом выше порога")
    print("8. Экспортировать книги в CSV")
    print("9. Импортировать книги из CSV")
    print("10. Выход")


def add_book():
    try:
        title = input("Введите название книги: ").strip()
        if not title:
            print("Название не может быть пустым")
            return

        if title in library:
            print("Книга с таким названием уже существует")
            return

        author = input("Введите автора: ").strip()
        if not author:
            print("Поле автора не может быть пустым")
            return


        year = int(input("Введите год издания: "))
        if year < 0 or year > 2024:
            print("Некорректный год!")
            return

        ratings_input = input("Введите оценки через запятую (например: 5,4,3): ").strip()
        if ratings_input:
            ratings = [int(x.strip()) for x in ratings_input.split(",")]
            for rating in ratings:
                if rating < 1 or rating > 5:
                    print("Оценки должны быть от 1 до 5!")
                    return
        else:
            ratings = []

        library[title] = {
            "author": author,
            "year": year,
            "ratings": ratings
        }
        print(f"Книга '{title}' успешно добавлена!")

    except ValueError:
        print("Ошибка ввода. Убедитесь, что год и оценки введены корректно.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


def show_all_books():
    if not library:
        print("Библиотека пуста!")
        return
    else:
        for title in library:
            print(f" название: {title}")
            print(f" автор: ", library[title]['author'])
            print(f" год издания: {library[title]['year']}")
            print(f" оценки: {library[title]['ratings']}")

def find_book_by_title():
    search_title = input("Введите название книги для поиска: ").strip()


    i = 1
    for title, info in library.items():
        if search_title.lower() in title.lower():
            print(f"Название: '{title}'")
            print(f"Автор: {info['author']}")
            print(f"Год: {info['year']}")
            print(f"Оценки: {info['ratings']}")
            i += 1
            break
    else:
        print("Книга не найдена!")


def delete_book():
    title = input("Введите название книги для удаления: ").strip()

    if title in library:
        del library[title]
        print(f"Книга '{title}' успешно удалена!")
    else:
        print("Книга с таким названием не найдена!")


def add_rating():
    title = input("Введите название книги: ").strip()

    if title not in library:
        print("Книга с таким названием не найдена!")
        return

    try:
        rating = int(input("Введите новую оценку (1-5): "))
        if rating < 1 or rating > 5:
            print("Оценка должна быть от 1 до 5!")
            return

        library[title]["ratings"].append(rating)
        print(f"Оценка {rating} добавлена к книге '{title}'")

    except ValueError:
        print("Ошибка! Введите число от 1 до 5.")


def books_after_year():
    try:
        year = int(input("Введите год: "))
        found_books = False

        for title, info in library.items():
            if info["year"] > year:
                print(f"'{title}' - {info['author']} ({info['year']})")
                found_books = True

        if not found_books:
            print("Книги не найдены.")

    except ValueError:
        print("Ошибка. Введите корректный год.")


def books_above_rating():
    try:
        threshold = float(input("Введите порог рейтинга (0-5): "))
        if threshold < 0 or threshold > 5:
            print("Рейтинг должен быть от 0 до 5!")
            return

        found_books = False

        for title, info in library.items():
            ratings = info["ratings"]
            if ratings:
                avg_rating = sum(ratings) / len(ratings)
                if avg_rating > threshold:
                    print(f"'{title}' - {info['author']} (Рейтинг: {avg_rating:.2f})")
                    found_books = True

        if not found_books:
            print("Книги не найдены.")

    except ValueError:
        print("Ошибка! Введите число.")


def export_to_csv():
    try:
        filename = input("Введите имя файла для экспорта (например: books.csv): ").strip()
        if not filename.endswith('.csv'):
            filename += '.csv'

        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(['название', 'автор', 'год', 'оценки'])

            for title, info in library.items():
                ratings_str = ','.join(map(str, info['ratings']))
                writer.writerow([title, info['author'], info['year'], ratings_str])

        print(f"Данные успешно экспортированы в файл {filename}")

    except Exception as e:
        print(f"Ошибка при экспорте: {e}")


def import_from_csv():
    try:
        filename = input("Введите имя файла для импорта: ").strip()

        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')
            next(reader)

            imported_count = 0
            for row in reader:
                if len(row) == 4:
                    title, author, year, ratings_str = row

                    if ratings_str:
                        ratings = [int(x) for x in ratings_str.split(',')]
                    else:
                        ratings = []

                    library[title] = {
                        "author": author,
                        "year": int(year),
                        "ratings": ratings
                    }
                    imported_count += 1

        print(f"Успешно импортировано {imported_count} книг")

    except FileNotFoundError:
        print("Файл не найден!")
    except Exception as e:
        print(f"Ошибка при импорте: {e}")


def main():
    print("Добро пожаловать в библиотечную систему!")

    while True:
        show_menu()

        try:
            choice = input("Выберите действие (1-10): ").strip()

            if choice == '1':
                add_book()
            elif choice == '2':
                show_all_books()
            elif choice == '3':
                find_book_by_title()
            elif choice == '4':
                delete_book()
            elif choice == '5':
                add_rating()
            elif choice == '6':
                books_after_year()
            elif choice == '7':
                books_above_rating()
            elif choice == '8':
                export_to_csv()
            elif choice == '9':
                import_from_csv()
            elif choice == '10':
                print("До свидания!")
                break
            else:
                print("Неверный выбор! Введите число от 1 до 10.")

        except KeyboardInterrupt:
            print("\nПрограмма завершена пользователем.")
            break
        except Exception as e:
            print(f"Произошла непредвиденная ошибка: {e}")

if __name__ == "__main__":
    main()
