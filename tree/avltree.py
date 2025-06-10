import unicodedata
from lookup.database import Saying

class AVLNode:
    def __init__(self, key, saying):
        self.key = key
        self.saying = saying
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def _normalize_key(self, key):
        return unicodedata.normalize('NFC', key.lower())
    
    def height(self, node):
        if not node:
            return 0
        return node.height
    
    def balance_factor(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)
    
    def update_height(self, node):
        if not node:
            return
        node.height = max(self.height(node.left), self.height(node.right)) + 1

    def rotate_right(self, y):
        if not y or not y.left:
            return y
        x = y.left
        temp_subtree = x.right
        x.right = y
        y.left = temp_subtree
        self.update_height(y)
        self.update_height(x)
        return x

    def rotate_left(self, x):
        if not x or not x.right:
            return x
        y = x.right
        temp_subtree = y.left
        y.left = x
        x.right = temp_subtree
        self.update_height(x)
        self.update_height(y)
        return y
    
    def insert(self, root, key, saying):
        if not root:
            return AVLNode(key, saying)
    
        normalized_key = self._normalize_key(key)
        normalized_root_key = self._normalize_key(root.key)

        if normalized_key < normalized_root_key:
            root.left = self.insert(root.left, key, saying)
        elif normalized_key > normalized_root_key:
            root.right = self.insert(root.right, key, saying)
        else:
            root.saying = saying
            return root
        
        self.update_height(root)
        balance = self.balance_factor(root)

        # Left heavy
        if balance > 1:
            if self.balance_factor(root.left) >= 0:
                return self.rotate_right(root)
            else:
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)
            
        # Right heavy
        if balance < -1:
            if self.balance_factor(root.right) <= 0:
                return self.rotate_left(root)
            else:
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root)
        return root
    

# -----------------------------      SEARCH METHODS     -------------------------------

    def search_saying(self, key):
        normalized_key = self._normalize_key(key)
        return self._search(self.root, normalized_key)
    
    def _search(self, node, key):
        if not node:
            return None
        if self._normalize_key(node.key) == key:
            return node
        elif key < self._normalize_key(node.key):
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

# -----------------------------      ORDERED SET OPERATIONS     -------------------------------

    # Insert
    def insert_saying(self, saying):
        self.root = self.insert(self.root, saying.hawaiian, saying)

    # Member
    def member(self, key):
        return self.search_saying(key) is not None
    
    # First
    def first(self):
        if not self.root:
            return None
        current = self.root
        while current.left:
            current = current.left
        return current.saying

    # Last
    def last(self):
        if not self.root:
            return None
        current = self.root
        while current.right:
            current = current.right
        return current.saying
        
    # Predecessor
    def predecessor(self, key):
        def _predecessor(node, key, pred=None):
            if not node:
                return pred
            if self._normalize_key(node.key) == self._normalize_key(key):
                if node.left:
                    current = node.left
                    while current.right:
                        current = current.right
                    return current.saying
                return pred
            elif self._normalize_key(key) < self._normalize_key(node.key):
                return _predecessor(node.left, key, pred)
            else:
                return _predecessor(node.right, key, node.saying)
        return _predecessor(self.root, key)

    # Successor
    def successor(self, key):
        def _successor(node, key, succ=None):
            if not node:
                return succ
            if self._normalize_key(node.key) == self._normalize_key(key):
                if node.right:
                    current = node.right
                    while current.left:
                        current = current.left
                    return current.saying
                return succ
            elif self._normalize_key(key) < self._normalize_key(node.key):
                return _successor(node.left, key, node.saying)
            else:
                return _successor(node.right, key, succ)
        return _successor(self.root, key)