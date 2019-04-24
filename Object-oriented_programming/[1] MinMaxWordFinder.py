# Find a shortest and longest word in sequence

from solution import MinMaxWordFinder

finder = MinMaxWordFinder()
finder.add_sentence('hello')
finder.add_sentence('  abc     def    ')
finder.add_sentence('world')
finder.add_sentence('            abc          ')
finder.add_sentence('asdf')
finder.add_sentence('qwert')
print(' '.join(finder.shortest_words()))
print(' '.join(finder.longest_words()))
