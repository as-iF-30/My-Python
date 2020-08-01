class Trie(object):
   def __init__(self):
      self.child = {}
   def insert(self, word):
      current = self.child
      for l in word:
         if l not in current:
            current[l] = {}
         current = current[l]
      current['#']=1
   def search(self, word):
      current = self.child
      for l in word:
         if l not in current:
            return False
         current = current[l]
      return '#' in current
   def startsWith(self, prefix):
      current = self.child
      for l in prefix:
         if l not in current:
            return False
         current = current[l]
      return True
# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert('apple')
print(obj.search('apple'))
print(obj.search('app'))
print(obj.startsWith('app'))
obj.insert('app')
print(obj.search('app'))
