class ArvoreAVL:
    
    class Node:
        def __init__(self, key):
            self.key = key
            self.left = None
            self.right = None
            self.height = 1

    def __init__(self) -> None:
        self.root = None
    
    @staticmethod
    def insert(root, key):
        if root is None:
            return ArvoreAVL.Node(key)
        
        if key < root.key:
            root.left = ArvoreAVL.insert(root.left, key)
        else:
            root.right = ArvoreAVL.insert(root.right, key)
        
        root.height = 1 + max(ArvoreAVL._height(root.left), ArvoreAVL._height(root.right))
        
        balance = ArvoreAVL._get_balance(root)
        
        # Casos de rotação
        if balance > 1 and key < root.left.key:
            return ArvoreAVL.right_rotate(root)
        if balance < -1 and key > root.right.key:
            return ArvoreAVL.left_rotate(root)
        if balance > 1 and key > root.left.key:
            root.left = ArvoreAVL.left_rotate(root.left)
            return ArvoreAVL.right_rotate(root)
        if balance < -1 and key < root.right.key:
            root.right = ArvoreAVL.right_rotate(root.right)
            return ArvoreAVL.left_rotate(root)
        
        return root
    
    @staticmethod
    def delete(root, key):
        if root is None:
            return root
        
        if key < root.key:
            root.left = ArvoreAVL.delete(root.left, key)
        elif key > root.key:
            root.right = ArvoreAVL.delete(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            
            temp = ArvoreAVL._min_value_node(root.right)
            root.key = temp.key
            root.right = ArvoreAVL.delete(root.right, temp.key)
        
        if root is None:
            return root
        
        root.height = 1 + max(ArvoreAVL._height(root.left), ArvoreAVL._height(root.right))
        
        balance = ArvoreAVL._get_balance(root)
        
        # Casos de rotação
        if balance > 1 and ArvoreAVL._get_balance(root.left) >= 0:
            return ArvoreAVL.right_rotate(root)
        if balance < -1 and ArvoreAVL._get_balance(root.right) <= 0:
            return ArvoreAVL.left_rotate(root)
        if balance > 1 and ArvoreAVL._get_balance(root.left) < 0:
            root.left = ArvoreAVL.left_rotate(root.left)
            return ArvoreAVL.right_rotate(root)
        if balance < -1 and ArvoreAVL._get_balance(root.right) > 0:
            root.right = ArvoreAVL.right_rotate(root.right)
            return ArvoreAVL.left_rotate(root)
        
        return root
    
    @staticmethod
    def left_rotate(x):
        y = x.right
        x.right = y.left
        if y.left is not None:
            y.left.p = x
        y.p = x.p
        if x.p is None:
            return y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x
        x.p = y
        return y
    
    @staticmethod
    def right_rotate(x):
        y = x.left
        x.left = y.right
        if y.right is not None:
            y.right.p = x
        y.p = x.p
        if x.p is None:
            return y
        elif x == x.p.right:
            x.p.right = y
        else:
            x.p.left = y
        y.right = x
        x.p = y
        return y
    
    @staticmethod
    def _height(node):
        if node is None:
            return 0
        return node.height
    
    @staticmethod
    def _get_balance(node):
        if node is None:
            return 0
        return ArvoreAVL._height(node.left) - ArvoreAVL._height(node.right)
    
    @staticmethod
    def _min_value_node(node):
        current = node
        while current.left is not None:
            current = current.left
        return current