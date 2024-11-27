import uuid


class Storage:

    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year
        self.id = str(uuid.uuid4())
        self.status = 'В наличии'

    def __repr__(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"

    def __dict__(self):
        """main book data"""
        return {'title': self.title,
                'author': self.author,
                'year': self.year,
                'id': self.id,
                'status': self.status}

    def set_status(self, status: str):
        self.status = status
