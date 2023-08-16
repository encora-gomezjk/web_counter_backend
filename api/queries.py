from ariadne import QueryType
from helpers.words_counter import Words_Counter
from helpers.words_reader import Words_Reader

query = QueryType()
words_reader = Words_Reader()
words = words_reader.read()

@query.field("count_words")
def count_words(*_, text: str):
   counter = Words_Counter(text=text, list_of_words_to_exclude=words)
   return counter.count()
