class WordDictionary:
    class Node:
        def __init__(self, val: str = ""):
            self.val = val
            self.next = [None]*26
            self.isEnd = False

    def __init__(self):
        self.trie = self.Node("*")
        

    def addWord(self, word: str) -> None:
        root = self.trie
        for c in word:
            if root.next[ord(c) - ord('a')] is None:
                root.next[ord(c) - ord('a')] = self.Node(c)
            root = root.next[ord(c) - ord('a')]
        root.isEnd = True
        

    def search(self, word: str) -> bool:
        return self.dfs(0, word, self.trie)
    
    def dfs(self, idx: int, word: str, node: Node) -> bool:
        ptr = node
        for i in range(idx, len(word)):
            c = word[i]

            if c == '.':
                for n in ptr.next:
                    if n != None and self.dfs(i+1, word, n):
                        return True
                return False
            else:
                flag = ""
                for k in ptr.next:
                    if k and c == k.val:
                        flag = k.val
                        break

                if flag == "":
                    return False
                ptr = ptr.next[ord(flag) - ord('a')]
            
        return ptr.isEnd

        
