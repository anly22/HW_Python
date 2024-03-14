from typing import List, Dict
from itertools import groupby

class Book:
    pile = []
    categories = set()
   
    def __init__(self, id: str, title: str, author: str, category: str):
        self.id = id
        self.title = title
        self.author = author
        self.category = category
        self.book = {'id': self.id, 'title': self.title, 'author': self.author, 'category': self.category}
        self.pile.append(self.book)
        self.categories.add(self.category)


    def __repr__(self) -> str:
        return f"'id':{self.id}, 'title':{self.title}, 'author': {self.author}, 'category': {self.category}"


    @classmethod
    def devide_by_categories(cls, pile, categories):
        devided_list = []
        def grouper(book):
            return book['category']

        pile = sorted(pile, key=grouper)
        
        for key, group_items in groupby(pile, key=grouper):
            li = []
            for item in group_items: 
                li.append(item)
            devided_list.append(li)
        sorted_categories = sorted(list(categories))
        library = dict(zip(sorted_categories, devided_list))
        return library
      
  


class Shelf:
    all_shelves = []


    def __init__(self, id: int, content: list) -> list:
        self.id = id
        self.content = content
       

    def __repr__(self):
        return f'[{self.id},{self.content}]'
    

    @classmethod
    def devide_to_shelves(cls, library: list):
        for i in range(0, len(library)):
            content = list(library.items())[i]
            shelf = Shelf(i+1, list(content))
            Shelf.all_shelves.append(shelf)

        return Shelf.all_shelves


    @staticmethod
    def sorted_by_title():
        for x in range(len(Shelf.all_shelves)):
            print(Shelf.all_shelves[x][1][1])
            (Shelf.all_shelves[x][1][1]).sort(key = lambda book: book['title'])
        return Shelf.all_shelves
     
    # def sorted_by_title() doesnot run successfully because: "'Shelf' object is not subscriptable"
    # But if I copy my Shelf.all_shelves to another file as variable, it runs

    # How to do it here?
