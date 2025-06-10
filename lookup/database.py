from collections import defaultdict
from tree.avltree import AVLTree
from lookup.saying import Saying

class SayingDatabase:
    def __init__(self):
        self.tree = AVLTree()
        self.hawaiian_index = defaultdict(set)
        self.english_index = defaultdict(set)

    def _tokenize_and_clean(self, text):
        import re
        text = text.lower()
        text = re.sub(r'[^\w\s]', ' ', text)
        words = [word for word in text.split() if word]
        return words

    def insert_saying(self, saying):
        print(f"Inserted: {saying.hawaiian} → {saying.english}")
        self.tree.insert_saying(saying)
        hawaiian_words = self._tokenize_and_clean(saying.hawaiian)
        for word in hawaiian_words:
            self.hawaiian_index[word].add(saying)
        english_words = self._tokenize_and_clean(saying.english)
        for word in english_words:
            self.english_index[word].add(saying)

    def mehua(self, word):
        return list(self.hawaiian_index.get(word.lower(), []))

    def withword(self, word):
        return list(self.english_index.get(word.lower(), []))

    def member(self, hawaiian_key):
        return self.tree.member(hawaiian_key)

    def first(self):
        return self.tree.first()

    def last(self):
        return self.tree.last()

    def predecessor(self, hawaiian_key):
        return self.tree.predecessor(hawaiian_key)

    def successor(self, hawaiian_key):
        return self.tree.successor(hawaiian_key)