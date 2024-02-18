class Library:

    def __init__(self, *args, **kwargs):
        # Open books.txt
        self.books = open("books.txt", "a+")

    def __del__(self,*args, **kwargs):
        self.books.close()

    def list_books(self):
        self.books.seek(0)  # Move the file pointer to the beginning
        booklines = self.books.read().splitlines()  
        if len(booklines)<1:
            print("There is no book in the library")
     
        for line in booklines:
            parsed_line = line.split(",")
            book_name = parsed_line[0]
            author = parsed_line[1]
            release_date = parsed_line[2]
            number_of_pages = parsed_line[3]
            print(f"""
            Book Name:  {book_name} and Author : {author} \n
            """)

    def add_book(self, book_name, author, release_date, number_of_pages):
        line = book_name + "," + author + "," + release_date + "," + number_of_pages
        self.books.write(line)

    def remove_book(self, book_name):
        counter = 0
        self.books.seek(0)  # Move the file pointer to the beginning
        booklines = self.books.read().splitlines()        
        for line in booklines:
            if (line.split(","))[0] == book_name:
                booklines.remove(line)
                print("Delete : ", line)
                break
            counter += 1

        self.books.truncate(0)
        for line in booklines:
            self.books.write(line + "\n")

if __name__ == "__main__":
    lib = Library()
    print("""
        \n
        * MENU***\n
        1) List Books\n
        2) Add Book\n
        3) Remove Book\n
    """)
    user_input = input("Enter :")
    if user_input == "1":
        lib.list_books()

    elif user_input == "2":
        book_name = input("Enter book name : ")
        author = input("Enter author : ")
        release_date = input("Enter release date : ")
        number_of_pages = input("Enter number of pages : ")

        lib.add_book(book_name, author, release_date, number_of_pages)

    elif user_input == "3":
        book_name = input("Enter the book name you want to delete:")
        lib.remove_book(book_name)

    else:
        print("Invalid Input!")
