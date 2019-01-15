class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def __repr__(self):
        stuff = "User: {}; User Email: {}; # of Books Read: {};".format(self.name, self.email, str(len(self.books)))
        return stuff

    def get_email(self):
        return self.email

    def change_email(self, address):
        prev_email = self.email
        self.email = address
        print("{username}'s email address has been changed from {old} to {new}.".format(username=self.name,
                                                                                        old=prev_email, new=self.email))

    def __eq__(self, other_user):
        return self.name == other_user.name and self.email == other_user.email

    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_average_rating(self):
        rating_sum = 0
        number = len(self.books)
        if number > 0:
            for rating in self.books.values():
                if rating is not None:
                    rating_sum += rating
            average = rating_sum / number
        else:
            average = 0
        return average


class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        prev_isbn = self.isbn
        self.isbn = new_isbn
        print("{t}'s ISBN has been changed from {p} to {c}.".format(t=self.title, p=prev_isbn, c=self.isbn))

    def add_rating(self, rating):
        if rating is not None and 0 <= rating <= 4:
            self.ratings.append(rating)
        elif rating is None:
            print("No rating")
        else:
            print("Invalid Rating")

    def __eq__(self, other_book):
        comparison = self.title == other_book.title and self.isbn == other_book.isbn
        return comparison

    def get_average_rating(self):
        denominator = len(self.ratings)
        tot = 0
        if denominator > 0:
            for item in self.ratings:
                tot += item
            average = tot / denominator
        else:
            average = 0
        return average

    def __hash__(self):
        return hash((self.title, self.isbn))


class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        sentence = "{} by {}".format(self.title, self.author)
        return sentence

class Non_Fiction(Book):

    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        sentence = "{first}, a {second} manual on {third}.".format(first=self.title, second=self.level,
                                                                   third=self.subject)
        return sentence


class TomeRater:

    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        exists = False
        for item in self.books:
            if item.isbn == isbn:
                exists = True
            else:
                pass
        if exists == False:
                new_book = Book(title, isbn)
                self.books[new_book] = 0
                return new_book
        else:
            print("A book already exists with {} isbn number.".format(isbn))

    def create_novel(self, title, author, isbn):
        exists = False
        for item in self.books:
            if item.isbn == isbn:
                exists = True
            else:
                pass
        if exists == False:
                new_fiction = Fiction(title, author, isbn)
                self.books[new_fiction] = 0
                return new_fiction
        else:
            print("A book already exists with {} isbn number.".format(isbn))

    def create_non_fiction(self, title, subject, level, isbn):
        exists = False
        for item in self.books:
            if item.isbn == isbn:
                exists = True
            else:
                pass
        if exists == False:
            new_non_fiction = Non_Fiction(title, subject, level, isbn)
            self.books[new_non_fiction] = 0
            return new_non_fiction
        else:
            print("A non-fiction already exists with {} isbn number.".format(isbn))

    def add_book_to_user(self, book, email, rating=None):
        if email in self.users.keys():
            self.users[email].read_book(book, rating)
            book.add_rating(rating)
            if book in self.books:
                self.books[book] += 1
            else:
                self.books[book] = 1
        else:
            print("No user with email {first}!".format(first=email))

    def add_user(self, name, email, user_books=None):
        if "@" in email:
            if ".com" in email or ".edu" in email or ".org" in email:
                if email not in self.users:
                    new_user = User(name, email)
                    self.users[email] = new_user
                    if user_books is not None:
                        if len(user_books) > 0:
                            for book in user_books:
                                self.add_book_to_user(book, email)
                        else:
                            pass
                    else:
                        pass
                else:
                    print("A user already exists with the email address {}.".format(email))
            else:
                print("The email address is missing the end of the address (.com, .edu, .org, etc.)")
        else:
            print("The email address is missing an @ symbol.")

    def print_catalog(self):
        for key in self.books.keys():
            print(key)

    def print_users(self):
        for user in self.users:
            print(user)

    def get_most_read_book(self):
        num_of_reads = 0
        book_name = None
        for key, value in self.books.items():
            if value > num_of_reads:
                book_name = key
                num_of_reads = value
        return book_name

    def highest_rated_book(self):
        rating = 0
        best_book = None
        for book in self.books:
            if book.get_average_rating() > rating:
                rating = book.get_average_rating()
                best_book = book.title
        return best_book

    def most_positive_user(self):
        rating = 0
        top_user = None
        for user in self.users:
            if self.users[user].get_average_rating() > rating:
                rating = self.users[user].get_average_rating()
                top_user = self.users[user].name
        return top_user
