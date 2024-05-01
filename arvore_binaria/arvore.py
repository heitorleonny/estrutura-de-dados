class ArvoreBinaria():
    @staticmethod
    def getInfo(p):
        return p.data
    
    @staticmethod
    def getLeft(p):
        return p.left
    
    @staticmethod
    def getRight(p):
        return p.right
    
    @staticmethod
    def getFather(p):
        return p.father
    
    @staticmethod
    def isLeft(p):
        q = ArvoreBinaria.getFather(p)
        if q is None:
            return False  # Significa que p é a raiz
        if ArvoreBinaria.getLeft(q) == p:
            return True
        return False
    
    @staticmethod
    def isRight(p):
        q = ArvoreBinaria.getFather(p)
        if q is None:
            return False  # Significa que p é a raiz
        if ArvoreBinaria.getRight(q) == p:
            return True
        return False
    
    @staticmethod
    def brother(p):
        if ArvoreBinaria.getFather(p) is None:
            return False  # p é a raiz
        if ArvoreBinaria.isLeft(p):
            return ArvoreBinaria.getRight(ArvoreBinaria.getFather(p))
        return ArvoreBinaria.getLeft(ArvoreBinaria.getFather(p))
    
    @staticmethod
    def inorder_tree_walk(root):
        if root is not None:
            ArvoreBinaria.inorder_tree_walk(root.left)
            print(root.data)
            ArvoreBinaria.inorder_tree_walk(root.right)
    
    @staticmethod
    def tree_search(x, k):
        while x is not None:
            if k == x.data:
                return x  # Retorna o nó encontrado
            if k < x.data:
                x = x.left
            else:
                x = x.right
        return None  # Não encontrou o nó
    
    @staticmethod
    def tree_minimum(p):
        while p.left is not None:
            p = p.left
        return p
    
    @staticmethod
    def tree_maximum(p):
        while p.right is not None:
            p = p.right
        return p
    
    @staticmethod
    def tree_sucessor(p):
        if p.right is not None:
            return ArvoreBinaria.tree_minimum(p.right)
        y = p.father
        while y is not None and p == y.right:
            p = y
            y = y.father
        return y
    
    @staticmethod
    def tree_predecessor(p):
        if p.left is not None:
            return ArvoreBinaria.tree_maximum(p.left)
        y = p.father
        while y is not None and p == y.left:
            p = y
            y = y.father
        return y
    
    @staticmethod
    def insert(root, z):
        y = None
        x = root
        while x is not None:
            y = x
            if z.data < x.data:
                x = x.left
            else:
                x = x.right
        z.father = y
        if y is None:
            root = z  # A árvore está vazia
        elif z.data < y.data:
            y.left = z
        else:
            y.right = z
        return root
    
    @staticmethod
    def delete(T, z):
        if z is None:
            return
        
        if z.left is None or z.right is None:
            y = z
        else:
            y = ArvoreBinaria.tree_sucessor(z)
        
        if y.left is not None:
            x = y.left
        else:
            x = y.right
        
        if x is not None:
            x.father = y.father
        
        if y.father is None:
            T.root = x
        elif y == y.father.left:
            y.father.left = x
        else:
            y.father.right = x
        
        if y != z:
            z.data = y.data
            
        return y
