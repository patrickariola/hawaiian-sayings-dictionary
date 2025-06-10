import unicodedata
import re
from lookup.saying import Saying

class AVLNode:
    def __init__(self, key, saying):
        self.key = key
        self.normalized_key = self._create_sort_key(key)
        self.saying = saying
        self.left = None
        self.right = None
        self.height = 1
    
    def _create_sort_key(self, text):
        text = unicodedata.normalize('NFD', text)
        text = text.lower()
        text = re.sub(r"[ʻ']", " ", text)
        text = ''.join(c for c in text if not unicodedata.combining(c))
        text = re.sub(r'\s+', ' ', text).strip()
        return text

class AVLTree:
    def __init__(self):
        self.root = None

    def _create_sort_key(self, text):
        text = unicodedata.normalize('NFD', text)
        text = text.lower()
        text = re.sub(r"[ʻ']", " ", text)
        text = ''.join(c for c in text if not unicodedata.combining(c))
        text = re.sub(r'\s+', ' ', text).strip()  
        return text
    
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
    
        normalized_key = self._create_sort_key(key)
        normalized_root_key = root.normalized_key

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
    
    def _find_min_node(self, node):
        current = node
        while current and current.left:
            current = current.left
        return current

    def _find_max_node(self, node):
        current = node
        while current and current.right:
            current = current.right
        return current

# -----------------------------      SEARCH METHODS     -------------------------------

    def search_saying(self, key):
        normalized_key = self._create_sort_key(key)
        return self._search(self.root, normalized_key)
    
    def _search(self, node, key):
        if not node:
            return None
        if node.normalized_key == key:
            return node
        elif key < node.normalized_key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

# -----------------------------      ORDERED SET OPERATIONS     -------------------------------

    def insert_saying(self, saying):
        self.root = self.insert(self.root, saying.hawaiian, saying)

    def member(self, key, silent=False):
        result = self.search_saying(key) is not None
        if not silent:
            print(f"Member check ({key}):")
            print(f"- {result}")
        return result
    
    def first(self):
        if not self.root:
            return None
        min_node = self._find_min_node(self.root)
        return min_node.saying if min_node else None

    def last(self):
        if not self.root:
            return None
        max_node = self._find_max_node(self.root)
        return max_node.saying if max_node else None
        
    def predecessor(self, key):
        def _predecessor(node, key, pred=None):
            if not node:
                return pred if pred else None
            normalized_key = self._create_sort_key(key)
            if node.normalized_key == normalized_key:
                if node.left:
                    current = node.left
                    while current.right:
                        current = current.right
                    return current.saying
                return pred
            elif normalized_key < node.normalized_key:
                return _predecessor(node.left, key, pred)
            else:
                return _predecessor(node.right, key, node.saying)
        result = _predecessor(self.root, key)
        return result if result and self.member(key, silent=True) else None


    def successor(self, key):
        def _successor(node, key, succ=None):
            if not node:
                return succ
            if node.normalized_key == self._create_sort_key(key):
                if node.right:
                    current = node.right
                    while current.left:
                        current = current.left
                    return current.saying
                return succ
            elif self._create_sort_key(key) < node.normalized_key:
                return _successor(node.left, key, node.saying)
            else:
                return _successor(node.right, key, succ)
        return _successor(self.root, key)

    def get_tree_height(self):
        return self.height(self.root)
    
    def debug_print_inorder(self):
        """Debug method to print tree in order"""
        def _inorder(node):
            if node:
                _inorder(node.left)
                print(f"Sort key: '{node.normalized_key}' -> Original: '{node.key}'")
                _inorder(node.right)
        _inorder(self.root)