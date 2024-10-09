#!/usr/bin/env python3

from pprint import pprint

# {{## BEGIN slots ##}}
class ChemicalElement:
    __slots__ = (
        'name',
        'number',
        'symbol',
        'family',
        'iupac_num'
    )

    def __init__(self, sym, nbr, name, fam, numeration):
        self.name = name.lower()
        self.number = nbr
        self.symbol = sym.title()
        self.family = fam.lower()
        self.iupac_num = numeration

    def __str__(self):
        return f"{self.symbol} ({self.name}): {self.number}"

oxygen = ChemicalElement('O', 8, 'oxygen', 'non-metals', 16)
iron = ChemicalElement('Fe', 26, 'iron', 'transition metal', 8)

print(oxygen)
print(iron)
# {{## END slots ##}}

# {{## BEGIN no-extending-slots ##}}
#iron.atomic_mass = 55.845 # AttributeError!
# {{## END no-extending-slots ##}}

# {{## BEGIN extending-with-slots ##}}
class Book:
    __slots__ = (
        'title',
        'author',
        'isbn',
        '__dict__'
    )
    def __init__(self, t, a, i):
        self.title = t
        self.author = a
        self.isbn = i

book = Book("Lord of the Rings", "J R R Tolkien", "Who knows")
book.volumes = 3
print(f"{book.title} is a {book.volumes}-volume series")
# {{## END extending-with-slots ##}}
