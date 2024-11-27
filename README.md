# The simplest app to manage the book storage

## Possibbilities:
### main CRUD operations:
- add bbook
- remove book
- update status
- search by id, author or year 


### Run:
```bash
src/main.py```

### Add book
```bash
python3 main.py -t <title> -a <author_name> -y <year>```

### Commands
```bash
python3 main.py -com <command>```

-'search': search book by author or year or title
-'delete': delete from storage by id
-'get_all': list of all books
-'change_status': change availiability
