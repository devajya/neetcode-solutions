class PrefixTree:
    class Node:
        def __init__(self, val: str = ""):
            self.val = val
            self.nextLetters = [None] * 26 

    def __init__(self):
        self.root = self.Node("*")
        self.words = set()

    def insert(self, word: str) -> None:
        self.words.add(word)
        ptr = self.root
        for idx, c in enumerate(word):
            if ptr.nextLetters[ord(c) - ord('a')] is None:
                ptr.nextLetters[ord(c) - ord('a')] = self.Node(c)
            ptr = ptr.nextLetters[ord(c) - ord('a')]


    def search(self, word: str) -> bool:
        return word in self.words

    def startsWith(self, prefix: str) -> bool:
        if prefix in self.words:
            return True
            
        ptr = self.root
        i=0
        while i<len(prefix):
            ptr = ptr.nextLetters[ord(prefix[i]) - ord('a')]
            if ptr is None:
                return False
            i+=1
            

        return True

        

        