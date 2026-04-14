class Node:
    def __init__(self):
        self.endOfWord = False
        self.children = [None]*26

class PrefixTree:
    def __init__(self):
        self.root = Node()
        
    def insert(self, word: str) -> None:
        ptr = self.root
        for c in word:
            i = self.idx(c)

            if ptr.children[i] == None:
                ptr.children[i] = Node()
            ptr = ptr.children[i]
        ptr.endOfWord = True

    def search(self, word: str) -> bool:
        ptr = self.root
        for c in word:
            i = self.idx(c)

            if ptr.children[i] == None:
                return False
            ptr = ptr.children[i]
        return ptr.endOfWord

    def startsWith(self, prefix: str) -> bool:
        ptr = self.root
        for c in prefix:
            i = self.idx(c)

            if ptr.children[i] == None:
                return False
            ptr = ptr.children[i]
        return True


    def idx(self, c: str) -> int:
        if c.islower():
            return ord(c) - ord('a')

        return 26+ord(c) - ord('A')
        
        