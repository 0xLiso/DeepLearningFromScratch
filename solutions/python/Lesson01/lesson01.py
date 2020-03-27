from collections import deque
import unittest


"""
Ejemplo de solución para el primer post.

RECORDAD QUE CONTINE ERRORES INTENCIONADOS PARA EVITAR EL C&P


First post solutions,
REMEMBER, IT HAS SOME INTENTIONAL BUGS TO AVOID C&P


"""


class node():
    name = ""

    def __init__(self, name):
        self.name = name
        self.parent_nodes = []
        self.child_nodes = []

    def __str__(self):
        return str(self.name)

    def add_child(self, j: str):
        if j not in self.child_nodes:
            self.child_nodes.append(j)

    def add_parent(self, j: str):
        if j not in self.parent_nodes:
            self.parent_nodes.append(j)

    def has_child(self, j: str):
        return j in self.child_nodes

    def remove_child(self, j: str):
        self.child_nodes.remove(j)

    def remove_parent(self, j: str):
        self.parent_nodes.remove(j)


class graph():
    nodes = {}

    def __init__(self):
        self.nodes = {}

    def __exist_node__(self, i: str):
        if i not in self.nodes:
            raise ValueError(f"node {i} don't exist.")

    def add_node(self, node_i: node):
        if str(node_i) not in self.nodes:
            self.nodes[str(node_i)] = node_i

    def add_edge(self, i: str, j: str):
        self.__exist_node__(i)
        self.__exist_node__(j)
        self.nodes[i].add_child(j)
        self.nodes[j].add_parent(i)

    def remove_edge(self, i: str, j: str):
        self.__exist_node__(i)
        self.__exist_node__(j)
        self.nodes[i].remove_child(j)
        self.nodes[j].remove_parent(i)

    def has_edge(self, i: str, j: str):
        self.__exist_node__(i)
        self.__exist_node__(j)
        return self.nodes[i].has_child(j)

    def out_edges(self, i: str):
        return self.nodes[i].child_nodes

    def in_edges(self, i: str):
        return self.nodes[i].child_nodes

    def to_dot(self):
        base = "digraph G {"
        sout = base + "\n"
        for n in self.nodes:
            for c in self.nodes[n].child_nodes:
                sout = n + "->" + c + "\n"
        sout += "}"
        return sout

    def dfs(self, i: str):
        # DFS en pseudo-código
        S = []  # recordar que es un contenedor LIFO
        visited = []
        S.append(i)  # Insertamos el nodo inicial en el stack
        while len(S) > 0:
            v = S.pop()
            visited.append(self.nodes[v])
            for w in self.nodes[v].parent_nodes:
                if w not in visited:
                    S.append(w)
        return visited  # devolvemos la lista de los nodos en el orden "profundo" correcto

    def bfs(self, i: str):
        # DFS en pseudo-código
        Q = deque([])  # recordar que es un contenedor LILO
        visited = []
        Q.append(i)  # Insertamos el nodo inicial en el Queue
        while len(Q) > 0:
            v = Q.popleft()
            visited.append(self.nodes[v])
            for w in self.nodes[v].parent_nodes:
                if w not in visited:
                    Q.append(w)
        return visited  # devolvemos la lista de los nodos en el orden "profundo" correcto

    def reverse_bfs(self, i: str):
        raise NotImplementedError

    def is_DAG(self):
        # DFS en pseudo-código

        for i in self.nodes:
            S = []  # recordar que es un contenedor LIFO
            visited = []
            S.append(i)  # Insertamos el nodo inicial en el stack
            while len(S) > 0:
                v = S.pop()
                if v in visited:
                    return False
                visited.append(v)
                for w in self.nodes[v].parent_nodes:
                    if w not in visited:
                        S.append(w)
        return True  # devolvemos la lista de los nodos en el orden "profundo" correcto


class TestGraphMethods(unittest.TestCase):
    def setup(self):
        g = graph()
        g.add_node(node("node_a"))
        g.add_node(node("node_b"))
        g.add_node(node("node_c"))
        g.add_node(node("node_d"))
        g.add_node(node("node_e"))
        g.add_node(node("node_f"))
        return g

    def test_to_dot(self):
        g = graph()
        g.add_node(node("node_a"))
        g.add_node(node("node_b"))
        g.add_node(node("node_c"))
        g.add_node(node("node_d"))
        g.add_node(node("node_e"))
        g.add_node(node("node_f"))

        g.add_edge("node_a", "node_c")
        g.add_edge("node_b", "node_d")
        g.add_edge("node_c", "node_d")
        g.add_edge("node_d", "node_f")
        g.add_edge("node_e", "node_f")

        result = '''digraph G {
        node_a -> node_c
        node_b -> node_d
        node_c -> node_d
        node_d -> node_f
        node_e -> node_f
        }'''

        self.assertTrue(
            g.to_dot().replace(' ', '').replace('\t', '').replace('\n', '') ==
            result.replace(' ', '').replace('\t', '').replace('\n', ''))

    def test_has_edge(self):
        # Test manipulación de grafo  en pseudo-código
        g = self.setup()

        g.add_edge("node_a", "node_c")
        g.add_edge("node_b", "node_d")
        g.add_edge("node_c", "node_d")
        g.add_edge("node_d", "node_f")
        g.add_edge("node_e", "node_f")

        # Test función has_edge
        self.assertFalse(g.has_edge("node_a", "node_b"))
        self.assertTrue(g.has_edge("node_b", "node_d"))

        # Test remove edge
        g.remove_edge("node_b", "node_d")
        self.assertFalse(g.has_edge("node_b", "node_d"))

    def test_dfs(self):
        # Test manipulación de grafo  en pseudo-código
        g = self.setup()
        g.add_node(node("node_f"))
        g.add_node(node("node_g"))
        g.add_node(node("node_h"))
        g.add_node(node("node_i"))
        g.add_node(node("node_j"))

        # el orden de los vertices importa para que la solución sea igual,
        # si se hacen los vertices en otro orden, el resultado será distinto pero igualmente correcto.
        g.add_edge("node_j", "node_h")
        g.add_edge("node_i", "node_h")
        g.add_edge("node_h", "node_a")
        g.add_edge("node_g", "node_a")
        g.add_edge("node_f", "node_b")
        g.add_edge("node_e", "node_c")
        g.add_edge("node_d", "node_c")
        g.add_edge("node_c", "node_b")
        g.add_edge("node_b", "node_a")

        # Test DFS
        resultado = g.dfs("node_a")

        self.assertTrue(resultado == [g.nodes["node_a"], g.nodes["node_b"], g.nodes["node_c"], g.nodes["node_d"],
                                      g.nodes["node_e"], g.nodes["node_f"], g.nodes["node_g"], g.nodes["node_h"],
                                      g.nodes["node_i"], g.nodes["node_j"]])

    def test_bfs(self):
        # Test manipulación de grafo  en pseudo-código
        g = self.setup()
        g.add_node(node("node_f"))
        g.add_node(node("node_g"))
        g.add_node(node("node_h"))
        g.add_node(node("node_i"))
        g.add_node(node("node_j"))

        g.add_edge("node_d", "node_c")
        g.add_edge("node_e", "node_c")
        g.add_edge("node_c", "node_b")
        g.add_edge("node_b", "node_a")
        g.add_edge("node_g", "node_a")
        g.add_edge("node_h", "node_a")
        g.add_edge("node_f", "node_b")
        g.add_edge("node_i", "node_h")
        g.add_edge("node_j", "node_h")

        # Test DFS
        resultado = g.bfs("node_a")

        self.assertTrue([str(x) for x in resultado] == ["node_a", "node_b", "node_g", "node_h",
                                                        "node_c", "node_f", "node_i", "node_j",
                                                        "node_d", "node_e"])

    def test_reverse_bfs(self):
        # Test manipulación de grafo  en pseudo-código
        g = self.setup()
        g.add_node(node("node_f"))
        g.add_node(node("node_g"))
        g.add_node(node("node_h"))
        g.add_node(node("node_i"))
        g.add_node(node("node_j"))

        g.add_edge("node_d", "node_c")
        g.add_edge("node_e", "node_c")
        g.add_edge("node_c", "node_b")
        g.add_edge("node_b", "node_a")
        g.add_edge("node_g", "node_a")
        g.add_edge("node_h", "node_a")
        g.add_edge("node_f", "node_b")
        g.add_edge("node_i", "node_h")
        g.add_edge("node_j", "node_h")

        # Test DFS
        resultado = g.reverse_bfs("node_a")

        self.assertTrue([str(x) for x in resultado] == ["node_e", "node_d", "node_j", "node_i",
                                                        "node_f", "node_c", "node_h", "node_g",
                                                        "node_b", "node_a"])

    def test_is_dag(self):
        # Test manipulación de grafo  en pseudo-código
        g = self.setup()
        g.add_node(node("node_f"))
        g.add_node(node("node_g"))
        g.add_node(node("node_h"))
        g.add_node(node("node_i"))
        g.add_node(node("node_j"))

        g.add_edge("node_d", "node_c")
        g.add_edge("node_e", "node_c")
        g.add_edge("node_c", "node_b")
        g.add_edge("node_b", "node_a")
        g.add_edge("node_g", "node_a")
        g.add_edge("node_h", "node_a")
        g.add_edge("node_f", "node_b")
        g.add_edge("node_i", "node_h")
        g.add_edge("node_j", "node_h")

        # Test is DAG
        self.assertTrue(g.is_DAG())

        g2 = graph()
        g2.add_node(node("node_1"))
        g2.add_node(node("node_2"))
        g2.add_node(node("node_3"))
        g2.add_edge("node_1", "node_3")
        g2.add_edge("node_2", "node_3")
        g2.add_edge("node_3", "node_2")

        # Test BFS
        self.assertFalse(g2.is_DAG())


if __name__ == '__main__':
    unittest.main()
