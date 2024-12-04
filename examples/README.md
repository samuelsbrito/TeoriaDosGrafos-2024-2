## **Tipo de Grafo Utilizado**

Nesta implementação, o grafo é representado usando **listas de adjacência**. Cada vértice possui uma lista encadeada que armazena seus vértices adjacentes.  

### Características:
- **Direcionado ou Não Direcionado**: A estrutura suporta ambos os tipos. Por padrão, o exemplo no `main.c` usa um grafo não direcionado.
- **Estrutura Modular**: A biblioteca de grafos (`graph.h` e `graph.c`) contém funções para criar grafos, adicionar arestas e calcular densidade.

---

## **Como Compilar**

Para compilar o programa, você precisará de um compilador C (como `gcc`) e do utilitário `make`. Siga os passos abaixo:

1. Certifique-se de que os arquivos do projeto (`main.c`, `graph.c`, `graph.h`, `Makefile`) estejam na mesma pasta.

2. No terminal, navegue até a pasta do projeto e execute:
   ```bash
   make
   ```

3. Isso criará um executável chamado `graph`.

4. Para limpar os arquivos de compilação, use:
   ```bash
   make clean
   ```

---

## **Como Executar**

Após compilar, você pode executar o programa com:
```bash
./graph
```

---

## **Exemplo de Uso**

O programa cria um grafo com 5 vértices e adiciona as seguintes arestas:
- 0 <-> 1
- 0 <-> 2
- 1 <-> 2
- 3 <-> 4

### Saída:
A saída do programa incluirá a lista de adjacência do grafo e a densidade calculada, escalada por 1000.

#### Exemplo de saída:
```
UNDIRECTED GRAPH:
Vertex ---> Adjacency List
0 ---> 2 -> 1 -> NULL
1 ---> 2 -> 0 -> NULL
2 ---> 1 -> 0 -> NULL
3 ---> 4 -> NULL
4 ---> 3 -> NULL
Graph Density (scaled x1000): 400
```

### Interpretação:
- O grafo possui 5 vértices e 4 arestas.
- O número máximo de arestas para um grafo não direcionado com 5 vértices é \( \frac{5 \times (5-1)}{2} = 10 \).
- A densidade do grafo é \( \frac{4}{10} = 0.4 \), o que equivale a 400 quando escalado por 1000.

![](../res/GPLv3_Logo.svg.png)