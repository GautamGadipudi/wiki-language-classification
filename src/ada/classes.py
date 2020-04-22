class Stump:
    __slots__ = ['question']
    

    def __init__(self, question):
        self.question = question


    def classify(self, row):
        return self.question.match(row)