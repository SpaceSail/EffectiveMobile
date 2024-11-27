from models import Storage
import json
from pathlib import Path

path = Path(__file__).parents[1]
_file = path.joinpath('data/storage.json')


# check if json storage exists
def check_json_storage() -> bool:
    if not _file.exists():
        return False


# creating json storage. Data set to avoid blanc json file or to rewrite
# data every time
def create_json_storage() -> None:
    print('creating storage')
    Path(_file).touch()
    with open(_file, 'w') as file:
        json.dump([{'title': 'title',
                    'author': 'author',
                    'year': 'year',
                    'id': 'id',
                    'status': 'status'}], file)


# add data to json
def write_json(obj: Storage) -> None:
    with open(_file, 'r') as infile:
        json_data = json.load(infile)
        json_data.append(obj.__dict__())
        with open(_file, 'w') as outfile:
            json.dump(json_data, outfile)


# load data from json
def load_json() -> list:
    with open(_file, 'r') as infile:
        json_data = json.load(infile)
        return json_data


# list of all books
def get_all_books() -> list:
    json_data = load_json()
    print(json_data)
    return json_data


# searching by any: title, author, year
def search_book(title: str = None,
                author: str = None,
                year: str = None) -> list:
    json_data = load_json()
    books = []
    for i in json_data:
        if (i['title'] == title
                or i['author'] == author
                or i['year'] == year):
            books.append(i)
    return books[1:]


# delete book from storage
def delete_book() -> None:
    id = input('Please, point out an id: ')
    json_data = load_json()
    print(json_data)
    for i in range(len(json_data)):
        if id == json_data[i]['id']:
            print(json_data[i])
            print(f"{json_data[i]} is deleted")
            with open('../data/storage.json', 'w') as outfile:
                json_data.remove(json_data[i])
                json.dump(json_data, outfile)
            return
        else:
            print('Sorry, there is no book with such id')
            return


# changing status of a book
def change_status() -> None:
    id = input('Please, point out an id : ')
    status = input("Please, point out a status('в наличии', 'выдана'): ")
    json_data = load_json()
    print(json_data)
    for i in range(len(json_data)):
        print(f"{json_data[i]} is changed")
        if json_data[i]['id'] == id:
            json_data[i]['status'] = status
            print(json_data)
            with open('../data/storage.json', 'w') as outfile:
                json.dump(json_data, outfile)
        else:
            print('Sorry, there is no book with such id')


# parsing args
def map(arg):
    mapping = {'search': search_book,
               'delete': delete_book,
               'get_all': get_all_books,
               'change_status': change_status,
               }
    return mapping[arg]()
