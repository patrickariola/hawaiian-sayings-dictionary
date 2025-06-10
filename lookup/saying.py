class Saying:
    def __init__(self, hawaiian, english, explanation_haw, explanation_eng):
        self.hawaiian = hawaiian
        self.english = english
        self.explanation_haw = explanation_haw
        self.explanation_eng = explanation_eng

    def __repr__(self):
        return (
            f"{self.hawaiian} → {self.english}\n"
            f"Explanation (ʻŌlelo Hawaiʻi): {self.explanation_haw}\n"
            f"Explanation (English): {self.explanation_eng}"
        )


