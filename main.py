import matrizAdjacencias
import listaAdjacencias
import info
import busca

# cria um grafo a partir de um arquivo:
def leitura(nomeArquivo):
    print("Implementar metodo leitura...")

if __name__ == "__main__":
    grafo = matrizAdjacencias.MatrizAdjacencias(5)

    grafo.addAresta(0, 1, 5)
    grafo.addAresta(1, 2, 10)
    grafo.addAresta(2, 3, 2)
    grafo.addAresta(3, 4, -14)
    grafo.addAresta(3, 2, 138)
    grafo.addAresta(4, 0)
    grafo.printGrafo()

    print(f"Existe aresta entre 3 e 4? {grafo.possuiAresta(3,4)}")
    print(f"Existe aresta entre 3 e 1? {grafo.possuiAresta(3,1)}")

    print(f"Vizinhos de 3: {grafo.vizinhos(3)}")