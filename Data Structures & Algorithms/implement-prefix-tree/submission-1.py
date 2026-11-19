class TrieNode():
    def __init__(self):
        self.children = {}
        self.endofword = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for i in word:
            if i not in cur.children:
                cur.children[i] = TrieNode()
            cur = cur.children[i]
        cur.endofword = True
            

    def search(self, word: str) -> bool:
        cur = self.root
        for i in word:
            if i not in cur.children:
                return False
            cur = cur.children[i]
        # if cur.endofword = True:
        #     return True
        # else:return False
        return cur.endofword
        # return True if cur.endofword is True else False
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for i in prefix:
            if i not in cur.children:
                return False
            cur = cur.children[i]

        return True
        
        