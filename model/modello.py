import networkx as nx
from database.DAO import DAO
"DA FARE SOLO LA VIEW, MI SCOCCIA HO FATTO TUTTO"

class Model:
    def __init__(self):
        self._graph = nx.DiGraph()
        self._idMap = {}
        self._mappaFun={}

    def build_graph(self, c, b):
        self._graph.clear()
        self._idMap.clear()

        nodi = DAO.get_nodi(c,b)
        self._graph.add_nodes_from(nodi)
        for n in nodi:
            self._idMap[n.GeneID,n.Function] = n
            if n.GeneID not in self._mappaFun:
                self._mappaFun[n.GeneID]=[]
            self._mappaFun[n.GeneID].append(n.Function)


        edges = list(DAO.get_archi(int(c), int(b)))

        for a in edges:

            for b in self._mappaFun[a.GeneID1]:
                for c in self._mappaFun[a.GeneID2]:
                    if self._idMap[a.GeneID1,b].Chromosome==self._idMap[a.GeneID2,c].Chromosome:
                        self._graph.add_edge(self._idMap[a.GeneID1,b], self._idMap[a.GeneID2,c], weight=a.Expression_Corr)
                        self._graph.add_edge(self._idMap[a.GeneID2, c], self._idMap[a.GeneID1, b], weight=a.Expression_Corr)
                    if self._idMap[a.GeneID1,b].Chromosome<self._idMap[a.GeneID2,c].Chromosome:
                        self._graph.add_edge(self._idMap[a.GeneID1, b], self._idMap[a.GeneID2, c], weight=a.Expression_Corr)
                    if self._idMap[a.GeneID1,b].Chromosome>self._idMap[a.GeneID2,c].Chromosome:
                        self._graph.add_edge(self._idMap[a.GeneID2, c], self._idMap[a.GeneID1, b], weight=a.Expression_Corr)

    def get_stats(self):
        return self._graph.number_of_nodes(), self._graph.number_of_edges()
    def top_5(self):
        lista=self._graph.out_degree()
        lista = sorted(lista, key=lambda x: x[1], reverse=True)
        li = []
        for n in range(5):
            peso=0.0
            archi=list(self._graph.out_edges(lista[n][0], data=True))

            for k in archi:
                peso=peso+float(k[2]["weight"])
            li.append((lista[n][0],len(archi),peso))
        return li



