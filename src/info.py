import listaAdjacencias
import matrizAdjacencias

# retorna a densidade do grafo:
def densidade(grafo):
    return grafo.numArestas / (grafo.numVertices * (grafo.numVertices - 1))

# retorna o complemento do grafo:
def complemento(grafo):
    print("Implementar metodo complemento...")

# retorna True se o grafo eh completo:
def completo(grafo):
    print("Implementar metodo completo...")

# retorna True se o grafo eh regular:
def regular(grafo):
    print("Implementar metodo regular...")

# retorna um subgrafo induzido pelo conjunto
# de vertices:
def subgrafo(grafo, vertices):
    print("Implementar metodo subgrafo...")