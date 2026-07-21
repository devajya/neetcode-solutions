class WordDictionary:
    class Node:
        def __init__(self):
            self.child = {} 
            self.end = False

    def __init__(self):
        self.trie = self.Node()

    def addWord(self, word: str) -> None:
        ptr = self.trie
        for c in word:
            if c not in ptr.child:
                ptr.child[c] = self.Node()
            ptr = ptr.child[c]
        ptr.end = True

    def search(self, word: str) -> bool:
        def dfs(idx, node):
            ptr = node
            for i in range(idx, len(word)):
                c = word[i]
                if c == ".":
                    for child_node in ptr.child.values():
                        if dfs(i+1, child_node):
                            return True
                    return False
                else:
                    if c not in ptr.child:
                        return False
                    ptr = ptr.child[c]
            return ptr.end
        return dfs(0, self.trie)