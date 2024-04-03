class ArvoreBinaria():

        
    @staticmethod
    def getInfo(p):
        return p.dado
    
    @staticmethod
    def getLeft(p):
        return p.filho_esquerdo
    
    @staticmethod
    def getRight(p):
        return p.filho_direito
    
    @staticmethod
    def getFather(p):
        return p.pai
    
    @staticmethod
    def isLeft(p):
        q = ArvoreBinaria.getFather(p)
        if q == None:
            return False # siginifica que p é a raiz
        if ArvoreBinaria.getLeft(q) == p:
            return True
        return False
    
    @staticmethod
    def isRight(p):
        q = ArvoreBinaria.getFather(p)
        if q == None:
            return False # siginifica que p é a raiz
        if ArvoreBinaria.getRight(q) == p:
            return True
        return False
    
    @staticmethod
    def brother(p):
        if ArvoreBinaria.getFather(p) == None:
            return False # p é a raiz
        if ArvoreBinaria.isLeft(p):
            return ArvoreBinaria.getRight(ArvoreBinaria.getFather(p))
        return ArvoreBinaria.getLeft(ArvoreBinaria.getFather(p))
    
    