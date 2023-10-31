# Graph-Bridges

## Introduction

Basic implementation that reads a directed graph, finding its <b><a href='https://en.wikipedia.org/wiki/Bridge_(graph_theory)'>bridges</a></b> and <b><a href='https://en.wikipedia.org/wiki/Articulation_point'>articulation points</a></b>.

## How It Works

The program starts by reading the number of vertices and edges (v e). After obtaining these values, it proceeds to read pairs of vertices representing the edges. The graph is represented using an <b>adjacency list</b>. Then uses a deapth search algorithm to find <b>bridges</b> and <b>articulation points</b>.

## How to use it

### Input

Initially, you need to specify both the number of vertices and edges in a single line as (v e). For instance, consider a graph with x vertices and y edges:
```
x y

```
After, will start to read each edge path, let say x is 5 and y is 8, an example of input 

```
5 8
0 1
1 2
2 3
3 4
3 0
2 4
1 4
0 4

```

### Output

```
(3,4) e ponte!
3 e um ponto de articulacao.

```
The edge (3,4) is a bridge and the vertice 3 is articulation point. If nothing shows on the screen, there's no edge or point in the graph.

### Dependencies
Pyhton 3.7 or higher.
