# Representacao computacional de um grafo por meio de matriz de adjacencias:
class MatrizAdjacencias:
    # inicializa o grafo:    
    def __init__(self, numVertices):
        print("Implementar metodo __init__...")

    # retorna a ordem do grafo:
    def ordem(self):
        print("Implementar metodo ordem...")
    
    # retorna o tamanho do grafo:
    def tamanho(self):
        print("Implementar metodo tamanho...")

    # adiciona uma aresta (v1, v2) no grafo:
    # peso eh um parametro opcional
    def addAresta(self, v1, v2, peso = 1):
        print("Implementar metodo addAresta...")
    
    # retorna True se existe uma aresta (v1,v2) no grafo:
    def possuiAresta(self, v1, v2):
        print("Implementar metodo possuiAresta...")

    # retorna uma lista com os vizinhos de v:
    def vizinhos(self, v):
        print("Implementar metodo vizinhos...")
    
    # retorna o grau (saida) de um vertice:
    def grau(self, v):
        print("Implementar metodo grau...")

    # printa o grafo no formato de matriz de adjacencias:
    def printGrafo(self):
        print("Implementar metodo printGrafo...")