from collections import defaultdict

class Saying:
    def __init__(self, hawaiian, english, explanation_haw, explanation_eng):
        self.hawaiian = hawaiian
        self.english = english
        self.explanation_haw = explanation_haw
        self.explanation_eng = explanation_eng

    def __repr__(self):
        return f"{self.hawaiian} → {self.english}"

class SayingDatabase:
    def __init__(self):
        self.sayings = []
        self.hawaiian_index = defaultdict(set)
        self.english_index = defaultdict(set)

    def insert_saying(self, saying):
        self.sayings.append(saying)

        for word in saying.hawaiian.lower().split():
            self.hawaiian_index[word].add(saying)

        for word in saying.english.lower().split():
            self.english_index[word].add(saying)

    def mehua(self, word):
        return list(self.hawaiian_index.get(word.lower(), []))

    def withword(self, word):
        return list(self.english_index.get(word.lower(), []))
