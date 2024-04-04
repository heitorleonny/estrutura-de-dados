class Nodo:

    def __init__(self, data=None, father=None) -> None:
        self.data = data
        self.left = None
        self.right = None
        self.father = father

    