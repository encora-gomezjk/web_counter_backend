from collections import Counter, OrderedDict

class Words_Counter:

    def __init__(self, text: str, list_of_words_to_exclude: list):
        self.__text = text
        self.__list_of_words_to_exclude = list_of_words_to_exclude

    def count(self):
        words_items = self.__text.lower().split()
        words_counter = Counter(words_items)
        words_counter = OrderedDict(words_counter.most_common())
        valid_words_counter = {''.join(filter(str.isalnum, k)): words_counter[k] for k in words_counter if k not in self.__list_of_words_to_exclude}
        return valid_words_counter
