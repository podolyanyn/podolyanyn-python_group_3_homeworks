class Author:
    def __init__(self, name: str, country: str, birthday: str):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []  # список книг автора

    def __repr__(self):
        return f"Author(name='{self.name}', country='{self.country}', birthday='{self.birthday}')"

    def __str__(self):
        return f"{self.name} ({self.country}, нар. {self.birthday})"


class Book:
    total_books = 0  # змінна класу для підрахунку всіх створених книг

    def __init__(self, name: str, year: int, author: Author):
        self.name = name
        self.year = year
        self.author = author
        Book.total_books += 1  # збільшення лічильника при створенні книги

    def __repr__(self):
        return f"Book(name='{self.name}', year={self.year}, author='{self.author.name}')"

    def __str__(self):
        return f"'{self.name}' ({self.year}) - {self.author.name}"


class Library:
    def __init__(self, name: str):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, name: str, year: int, author: Author):
        book = Book(name, year, author)
        self.books.append(book)
        author.books.append(book)
        if author not in self.authors:
            self.authors.append(author)
        return book

    def group_by_author(self, author: Author):
        return [book for book in self.books if book.author == author]

    def group_by_year(self, year: int):
        return [book for book in self.books if book.year == year]

    def __repr__(self):
        return f"Library(name='{self.name}', books={len(self.books)}, authors={len(self.authors)})"

    def __str__(self):
        return f"Бібліотека '{self.name}' (Книг: {len(self.books)}, Авторів: {len(self.authors)})"


lib_name = input("Введіть назву бібліотеки: ")
library = Library(lib_name)

n_authors = int(input("Скільки авторів хочете додати? "))
authors = []

for _ in range(n_authors):
    name = input("Ім'я автора: ")
    country = input("Країна автора: ")
    birthday = input("Дата народження (рррр-мм-дд): ")
    authors.append(Author(name, country, birthday))

n_books = int(input("Скільки книг хочете додати? "))
for _ in range(n_books):
    book_name = input("Назва книги: ")
    book_year = int(input("Рік випуску: "))

    print("Оберіть автора за номером:")
    for i, author in enumerate(authors):
        print(f"{i + 1}. {author}")
    author_index = int(input("Ваш вибір: ")) - 1
    chosen_author = authors[author_index]

    library.new_book(book_name, book_year, chosen_author)

print("\n Ваша бібліотека:")
print(library)

print("\nСписок книг:")
for b in library.books:
    print(b)

print("\nЗагальна кількість книг:", Book.total_books)

print("\nКниги першого автора:")
print(library.group_by_author(authors[0]))

year_filter = int(input("\nВведіть рік для пошуку книг: "))
print(library.group_by_year(year_filter))