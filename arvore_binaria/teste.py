from nodo import Nodo
from arvore import ArvoreBinaria

# Função para inserir vários elementos na árvore
def inserir_elementos(arvore, elementos):
    for elemento in elementos:
        novo_no = Nodo(elemento)
        arvore = ArvoreBinaria.insert(arvore, novo_no)
    return arvore

# Função para imprimir a árvore em ordem
def imprimir_arvore_in_ordem(raiz):
    if raiz is not None:
        imprimir_arvore_in_ordem(raiz.left)
        print(raiz.data, end=" ")
        imprimir_arvore_in_ordem(raiz.right)

# Teste da árvore binária
if __name__ == "__main__":
    # Criando uma árvore vazia
    arvore = None

    # Elementos a serem inseridos na árvore
    elementos = [10, 5, 15, 2, 7, 40, 12, 20, 3, 9, 17, 1, 4, 6, 8, 11, 13, 16, 18, 19, 21, 0, 22, 23, 24, 25, 26]

    # Inserindo os elementos na árvore
    arvore = inserir_elementos(arvore, elementos)

    # Imprimindo a árvore em ordem
    print("Árvore em ordem:")
    imprimir_arvore_in_ordem(arvore)
    print("\n")

    # Testando as outras funções da árvore
    print("Testando outras funções:")

    # Teste da função de busca
    valor_procurado = 12
    no_encontrado = ArvoreBinaria.tree_search(arvore, valor_procurado)
    if no_encontrado:
        print(f"Valor {valor_procurado} encontrado na árvore.")
    else:
        print(f"Valor {valor_procurado} não encontrado na árvore.")

    # Teste das funções mínimo e máximo
    minimo = ArvoreBinaria.tree_minimum(arvore)
    maximo = ArvoreBinaria.tree_maximum(arvore)
    print(f"Mínimo: {minimo.data}")
    print(f"Máximo: {maximo.data}")

    # Teste da função sucessor
    valor_sucessor = 3
    sucessor = ArvoreBinaria.tree_sucessor(ArvoreBinaria.tree_search(arvore, valor_sucessor))
    if sucessor:
        print(f"Sucessor de {valor_sucessor}: {sucessor.data}")
    else:
        print(f"{valor_sucessor} não tem sucessor.")

    # Teste da função predecessor
    valor_predecessor = 16
    predecessor = ArvoreBinaria.tree_predecessor(ArvoreBinaria.tree_search(arvore, valor_predecessor))
    if predecessor:
        print(f"Predecessor de {valor_predecessor}: {predecessor.data}")
    else:
        print(f"{valor_predecessor} não tem predecessor.")

        # Teste da função delete
    valor_para_excluir = 7
    no_excluido = ArvoreBinaria.tree_search(arvore, valor_para_excluir)
    if no_excluido:
        print(f"Excluindo o valor {valor_para_excluir} da árvore...")
        ArvoreBinaria.delete(arvore, no_excluido)
        imprimir_arvore_in_ordem(arvore)
        
    else:
        print(f"O valor {valor_para_excluir} não está presente na árvore.")
