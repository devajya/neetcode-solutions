class Node:
    def __init__(self):
        self.endOfWord = False
        self.children = [None] * 52


class PrefixTree:
    def __init__(self):
        self.root = Node()

    def _traverse(self, string: str, create: bool = False) -> Node | None:
        ptr = self.root

        for c in string:
            i = self.idx(c)
            if i is None:
                return None 

            if ptr.children[i] is None:
                if not create:
                    return None
                ptr.children[i] = Node()

            ptr = ptr.children[i]

        return ptr

    def insert(self, word: str) -> None:
        node = self._traverse(word, create=True)
        if node:
            node.endOfWord = True

    def search(self, word: str) -> bool:
        node = self._traverse(word)
        return node is not None and node.endOfWord

    def startsWith(self, prefix: str) -> bool:
        return self._traverse(prefix) is not None

    def idx(self, c: str) -> int | None:
        if c.islower():
            return ord(c) - ord('a')
        if c.isupper():
            return 26 + ord(c) - ord('A')

        return None
