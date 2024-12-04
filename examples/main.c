//========================================================================
//    This file is part of mocd (Multi-objective Community Detection).
//    Copyright (C) 2024 Guilherme Oliveira Santos
//    This is free software: you can redistribute it and/or modify it
//    under the terms of the GNU GPL3 or any later version.
//========================================================================

#include <stdio.h>
#include <stdint.h>
#include <stdbool.h>
#include "graph.h"

#define NUM_VERTICES 5
#define IS_DIRECTED false

int main() {
    Graph *graph = createGraph(NUM_VERTICES, IS_DIRECTED);

    graph->addEdge(graph, 0, 1);
    graph->addEdge(graph, 0, 2);
    graph->addEdge(graph, 1, 2);
    graph->addEdge(graph, 3, 4);

    graph->print(graph);

    int32_t density = calculateDensity(graph);
    printf("Graph Density (scaled x1000): %d\n", density);

    return 0;
}
