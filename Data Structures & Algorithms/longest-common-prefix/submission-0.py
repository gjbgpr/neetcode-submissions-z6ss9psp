class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
    
    def lcp(self, word: str, prefix_length: int) -> int:
        node = self.root
        for i in range(min(len(word), prefix_length)):
            if word[i] not in node.children:
                return i
            node = node.children[word[i]]
        return min(len(word), prefix_length)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        
        smallest = 0
        for i in range(1, len(strs)):
            if len(strs[smallest]) > len(strs[i]):
                smallest = i
        
        trie = Trie()
        trie.insert(strs[smallest])
        prefix_length = len(strs[smallest])
        for i in range(len(strs)):
            prefix_length = trie.lcp(strs[i], prefix_length)
        return strs[0][:prefix_length]
        