from collections import defaultdict
from tree.avltree import AVLTree
from lookup.saying import Saying  # Correct: now ONLY imported

class SayingDatabase:
    def __init__(self):
        self.tree = AVLTree()
        self.hawaiian_index = defaultdict(set)
        self.english_index = defaultdict(set)

    def insert_saying(self, saying):
        self.tree.insert_saying(saying)

        for word in saying.hawaiian.lower().split():
            self.hawaiian_index[word].add(saying)

        for word in saying.english.lower().split():
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
