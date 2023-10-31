class vertice:
    def __init__(self):
        self.adj = []
        self.cor = str("BRANCO")
        self.pred = None
        self.descoberta = None
        self.termino = None
        self.low = None

tempo = int(0)

def cria_Grafo(Max_v, Max_a):
    Grafo = {}

    for i in range(Max_v):
        Grafo[i] = vertice()

    for k in range(Max_a):
        entrada = input()
        aux = entrada.split(" ")
        Grafo[int(aux[0])].adj.append(int(aux[1]))

    return Grafo

def Ponte_Visit(Grafo, atual):
    global tempo;
    filhos = 0
    tempo = tempo + 1
    Grafo[atual].cor = "CINZA"
    Grafo[atual].descoberta = tempo
    Grafo[atual].low = Grafo[atual].descoberta
    for k in range(len(Grafo[atual].adj)):
        filhos = filhos + 1
        aux = Grafo[atual].adj[k]
        if (Grafo[aux].cor == "BRANCO"):
            Grafo[aux].pred = atual
            Ponte_Visit(Grafo, aux)
            Grafo[atual].low = min(int(Grafo[atual].low), int(Grafo[aux].low))
            
            if (Grafo[aux].low > Grafo[atual].descoberta):
                print("({},{}) e ponte!".format(atual, aux))
            
            if (Grafo[atual].pred == None):
                if (filhos > 1):
                    print("{} e um ponto de articulacao.".format(atual))
            else:
                Grafo[atual].low = min(int(Grafo[atual].low), int(Grafo[aux].low))
                if (Grafo[aux].low >= Grafo[atual].descoberta) :
                    print("{} e um ponto de articulacao.".format(atual))
        
        else:
            if ((int(aux) != Grafo[atual].pred) and (int(Grafo[aux].descoberta) < int(Grafo[atual].descoberta))):
                Grafo[atual].low = min(int(Grafo[atual].low), int(Grafo[aux].descoberta))
    Grafo[atual].cor = "PRETO"
    tempo = tempo + 1
    Grafo[atual].termino = tempo

def Ponte_Art(Grafo):
    for j in range(len(Grafo)):
        if (Grafo[j].cor == "BRANCO"):
            Ponte_Visit(Grafo, j)
    return Grafo

Tamanhos = input()
Tamanhos = Tamanhos.split(" ")

Graph = cria_Grafo(int(Tamanhos[0]), int(Tamanhos[1]))

Ponte_Art (Graph)