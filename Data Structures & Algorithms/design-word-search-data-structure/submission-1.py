class WordDictionary:

    def __init__(self):
        self.children = {}
        self.endOfWord = False        

    def addWord(self, word: str) -> None:
        cur = self 
        for c in word:
            if c not in cur.children:
                cur.children[c] = WordDictionary()
            cur = cur.children[c]
        cur.endOfWord = True
    def search(self, word: str) -> bool:
        if not word:
            return self.endOfWord
        cur = self

        for i in range(len(word)):

            if word[i] == ".":
                for child in cur.children:
                    if cur.children[child].search(word[i+1:]):
                        return True
            if word[i] not in cur.children:
                return False

            cur = cur.children[word[i]]
        return cur.endOfWord