import book_organizing as b
import pprint

book1 = b.Book('1', 'Cinderella', 'Charles Perrault', 'fairy tale')
book2 = b.Book('2', 'Murders by Alphabet', 'Agatha Christie', 'detective')
book3 = b.Book('3', 'The Mysterious Island', 'Jules Verne', 'adventure novel')
book4 = b.Book('4', 'Abstract Algebra with Applications', 'A.Terras', 'education')
book5 = b.Book('5', 'Algorithms', 'R.Sedgewick, K.Wayne', 'education')
book6 = b.Book('6', 'Python', 'Mark Lutz', 'education')
book7 = b.Book('7', 'Journey to the Center of the Earth', 'Jules Verne', 'adventure novel')
book8 = b.Book('8', 'Murder on the Orient Express', 'Agatha Christie', 'detective')
book9 = b.Book('9', 'The snow queen', 'Andersen', 'fairy tale')
book10 = b.Book('10', 'Hamlet', 'Shakespeare', 'play')

# pprint.pprint(b.Book.pile)

library = b.Book.devide_by_categories(b.Book.pile, b.Book.categories)
print('\nLibrary:\n', library)

all_shelves = b.Shelf.devide_to_shelves(library)
print('\nShelves:')
pprint.pprint(all_shelves)

# sorted_all_shelves = b.Shelf.sorted_by_title(all_shelves)
# pprint.pprint('!!!', sorted_all_shelves)
# pprint.pprint(b.Shelf.sorted_by_title())