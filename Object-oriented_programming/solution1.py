class MinMaxWordFinder():
    def __init__(self):
        self.text = ''
    def add_sentence(self, sentence):
        self.text = self.text + ' ' + sentence
    def shortest_words(self):
        minlen = min(list(map(lambda x:len(x),self.text.split())))
        return sorted(list(filter(lambda x: len(x) == minlen,self.text.split())))
    def longest_words(self):
        maxlen = max(list(map(lambda x:len(x),self.text.split())))
        return sorted(list(set((filter(lambda x: len(x) == maxlen,self.text.split())))))
        


