import requests

url = "http://andrewbeatty1.pythonanywhere.com/books"
id= 683

#function for getting all books
def read_books():
    response = requests.get(url)
    return response.json()

#function for getting specific books by id
def read_books_id(id):
    id_url = url + "/" + str(id)
    response = requests.get(id_url)
    return response.json()

if __name__ == "__main__":
    books = read_books()
    books_id = read_books_id(id)
    print(books_id)
