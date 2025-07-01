class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        class TrieNode:
            def __init__(self):
                self.children={}
                self.end=False
        class Trie:
            def __init__(self):
                self.root=TrieNode()
            def insert(self,word):
                node=self.root
                for ch in word:
                    if ch not in node.children:
                        node.children[ch]=TrieNode()
                    node=node.children[ch]
                node.end=True
            def search(self,word):
                node=self.root
                prefix=""
                for ch in (word):
                    if ch in node.children and len(node.children)==1 and not node.end:
                        node=node.children[ch]
                        prefix+=ch
                    else:
                        break
                return prefix
        trie=Trie()
        for i in strs:
            trie.insert(i)
        
        return trie.search(strs[0])
                    
            