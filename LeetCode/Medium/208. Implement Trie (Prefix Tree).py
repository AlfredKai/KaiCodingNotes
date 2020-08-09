class Node:
    def __init__(self, val):
        self.children = {}
        self.val = val

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node(0)
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur_node = self.root
        for c in word:
            if c in cur_node.children:
                cur_node = cur_node.children[c]
            else:
                cur_node.children[c] = Node(0)
                cur_node = cur_node.children[c]
        else:
            cur_node.val = 1
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur_node = self.root
        for c in word:
            if c in cur_node.children:
                cur_node = cur_node.children[c]
            else:
                return False
        return cur_node.val == 1
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur_node = self.root
        for c in prefix:
            if c in cur_node.children:
                cur_node = cur_node.children[c]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert('word')
print(obj.search('word'))
# param_3 = obj.startsWith(prefix)