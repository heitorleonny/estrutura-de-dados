class Nodo:

    def __init__(self, dado=None, pai=None) -> None:
        self.dado = dado
        self.filho_esquerdo = None
        self.filho_direito = None
        self.pai = pai

    