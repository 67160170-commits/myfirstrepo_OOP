import matplotlib.pyplot as plt
import networkx as nx
from collections import deque

class Graph_Structure:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbor):
        """เพิ่มเส้นเชื่อมระหว่าง node และ neighbor"""
        if node not in self.graph:
            self.graph[node] = []
        if neighbor not in self.graph:
            self.graph[neighbor] = []
        self.graph[node].append(neighbor)
        self.graph[neighbor].append(node)

    def show_graph(self):
        """แสดงรายการโหนดและเส้นเชื่อม"""
        for node, neighbors in self.graph.items():
            print(f"{node} -> {neighbors}")

    def plot_graph(self, highlight_nodes=None, title="Graph Structure"):
        """แสดงกราฟด้วย NetworkX"""
        G = nx.Graph(self.graph)
        pos = nx.spring_layout(G, seed=42)
        plt.figure(figsize=(6, 4))

        # สีของ node (แยกเฉพาะโหนดที่ถูก highlight)
        node_colors = []
        for n in G.nodes():
            if highlight_nodes and n in highlight_nodes:
                node_colors.append("lightcoral")
            else:
                node_colors.append("skyblue")

        nx.draw(
            G, pos,
            with_labels=True,
            node_color=node_colors,
            node_size=1200,
            font_size=12,
            font_weight='bold',
            edge_color='gray'
        )
        plt.title(title)
        plt.show()

    def bfs(self, start):
        """Breadth-First Search"""
        visited = []
        queue = deque([start])

        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.append(node)
                # เพิ่มเพื่อนบ้านที่ยังไม่ถูกเยี่ยมชม
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)

        print("BFS Order:", visited)
        self.plot_graph(highlight_nodes=visited, title="BFS Traversal")
        return visited

    def dfs(self, start):
        """Depth-First Search"""
        visited = []
        stack = [start]

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.append(node)
                # เพิ่มเพื่อนบ้านใน stack (ย้อนกลับเพื่อเรียงซ้ายไปขวา)
                for neighbor in reversed(self.graph[node]):
                    if neighbor not in visited:
                        stack.append(neighbor)

        print("DFS Order:", visited)
        self.plot_graph(highlight_nodes=visited, title="DFS Traversal")
        return visited

if __name__ == "__main__":
    g = Graph_Structure()
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('C', 'D')
    g.add_edge('D', 'E')

    print("Graph Structure:")
    g.show_graph()

    g.bfs('A')
    g.dfs('A')