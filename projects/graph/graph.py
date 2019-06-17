"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}


    def add_vertex(self, vertex):
        verts = self.vertices
        if verts.get(vertex) == None:
            verts[vertex] = set()

    def add_edge(self, v1, v2):
        verts = self.vertices
        if v1 in verts and v2 in verts:
            verts[v1].add(v2)
        else:
            raise Exception

    def _unvisited_edges(self, vertex, visited):
            return [i for i in self.vertices.get(vertex) if i not in visited]

    def bft(self, starting_vertex):
        queue = []
        visited = { starting_vertex }
        verts = self.vertices
        queue.extend(verts.get(starting_vertex))

        for i in range(len(verts)):
            visit = queue.pop(0)
            queue.extend(self._unvisited_edges(visit, visited))
            visited.add(visit)
            if len(queue) == 0:
                break

        print(visited)

    def dft(self, starting_vertex):
        stack = []
        visited = set()
        verts = self.vertices
        stack.append(starting_vertex)

        for i in range(len(verts)):
            visit = stack[len(stack) -1]

            if visit not in visited:
                visited.add(visit)

            edges = self._unvisited_edges(visit, visited)

            while len(edges) == 0:
                try:
                    stack.pop()
                    visit = stack[len(stack) -1]
                    edges = self._unvisited_edges(visit, visited)
                except IndexError:
                    break

            if len(edges) > 0:
                stack.append(edges[0])

        print(visited)

    def dft_recursive(self, starting_vertex):
        # stack = []
        # visited = [starting_vertex]
        # verts = self.vertices
        # stack.extend(verts.get(starting_vertex))
        pass

    def bfs(self, starting_vertex, destination_vertex):
        verts = self.vertices

        queue = [ [starting_vertex] ]
        visited = { starting_vertex }


        for i in range(len(verts)):
            path = queue.pop(0)
            visit = path[-1]
            visited.add(visit)
            branches = set(self._unvisited_edges(visit,visited))
            if destination_vertex in branches:
                path.append(destination_vertex)
                break

            for i in branches:
                queue.append(path + [i])

        print(path)

    def dfs(self, starting_vertex, destination_vertex):
        verts = self.vertices

        stack = [ [starting_vertex] ]
        visited = set()
        ends = set()

        for i in range(len(verts)):
            path = stack.pop()
            visit = path[-1]
            visited.add(visit)

            branches = self._unvisited_edges(visit, visited)
            while len(branches) == 0:
                try:
                    ends.add(visit)
                    path = stack.pop()
                    visit = path[-1]
                    branches = self._unvisited_edges(visit, visited)
                except IndexError:
                    break

            if destination_vertex in branches:
                path.append(destination_vertex)
                break

            for i in branches:
                stack.append(path + [i])

        print(path)



if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
