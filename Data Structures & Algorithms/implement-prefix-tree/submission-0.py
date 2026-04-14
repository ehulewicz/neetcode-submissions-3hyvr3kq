class PrefixTree:

    def __init__(self):
        self.tree = {}
        

    def insert(self, word: str) -> None:
        curr = self.tree
        for w in word:
            if w not in curr:
                curr[w] = {}
            curr = curr[w]
        curr[-1] = True


    def search(self, word: str) -> bool:
        curr = self.tree
        for w in word:
            if w not in curr:
                return False
            curr = curr[w]
        return True if -1 in curr else False

    def startsWith(self, prefix: str) -> bool:
        curr = self.tree
        for w in prefix:
            if w not in curr:
                return False
            curr = curr[w]
        return True