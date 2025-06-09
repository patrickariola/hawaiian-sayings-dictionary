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

    def rotate_left(self, x):
        if not x or not x.right:
            return x
        y = x.right
        temp_subtree = y.left
        y.left = x
        x.right = temp_subtree
        self.update_height(x)
        self.udpate_height(y)
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
            if self._normalize_key(key) < self._normalize_key(root.left.key):
                return self.rotate_right(root)
            else:
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)
            
        # Right heavy
        if balance < -1:
            if self._normalize_key(key) > self._normalize_key(root.right.key):
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

# -----------------------------     TESTING     -------------------------------

    def _insert_for_testing(self, key, saying):
        self.root = self.insert(self.root, key ,saying)

if __name__ == "__main__":
    tree = AVLTree()
    s1 = Saying("Aia akula nō i Ki'ilau.", "He is gone to Ki'ilau.", 
                "He ʻōlelo no ka kamaʻilio lapuwale.", "Said of senseless chatter.")
    s2 = Saying("Aia akula paha i Waikīkī...", "Perhaps gone to Waikiki...", 
                "He hōʻike no ka hoʻohaʻahaʻa.", "Gone where disappointment is met.")
    
    # Insert sayings
    tree._insert_for_testing(s1.hawaiian, s1)
    tree._insert_for_testing(s2.hawaiian, s2)

    # Verify insertions
    print(f"Tree should contain 2 nodes after insertions.")
    node1 = tree.search_saying(s1.hawaiian)
    node2 = tree.search_saying(s2.hawaiian)
    if node1 and node2:
        print(f"Found saying 1: {node1.saying}")
        print(f"Found saying 2: {node2.saying}")
    else:
        print("Insertion failed: nodes not found in tree.")
    