"""
Simple graph implementation
"""
# from util import Stack, Queue  # These may come in handy


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        verts = self.vertices
        if verts.get(vertex) == None:
            verts[vertex] = set()

    def add_parents(self, v1, v2):
        verts = self.vertices
        if v1 not in verts:
            self.add_vertex(v1)
        if v2 not in verts:
            self.add_vertex(v2)
        if v1 in verts and v2 in verts:
            verts[v2].add(v1)
        else:
            raise Exception

    def _unvisited_edges(self, vertex, visited):
        return [i for i in self.vertices.get(vertex) if i not in visited]

    def bft(self, starting_vertex):
        queue = []
        visited = {starting_vertex}
        verts = self.vertices
        queue.extend(verts.get(starting_vertex))

        for i in range(len(verts)):
            visit = queue.pop(0)
            queue.extend(self._unvisited_edges(visit, visited))
            visited.add(visit)
            if len(queue) == 0:
                break

        print(visited)

    def dft_recursive(self, starting_vertex):
        # stack = []
        # visited = [starting_vertex]
        # verts = self.vertices
        # stack.extend(verts.get(starting_vertex))
        pass

    def bfs(self, starting_vertex, destination_vertex):
        verts = self.vertices

        queue = [[starting_vertex]]
        visited = {starting_vertex}

        for i in range(len(verts)):
            path = queue.pop(0)
            visit = path[-1]
            visited.add(visit)
            branches = set(self._unvisited_edges(visit, visited))
            if destination_vertex in branches:
                path.append(destination_vertex)
                break

            for i in branches:
                queue.append(path + [i])

        print(path)

    def dfs(self, starting_vertex, destination_vertex):
        verts = self.vertices

        stack = [[starting_vertex]]
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

    def earliest_ancestor(self, child):
        verts = self.vertices

        queue = [[child]]
        visited = {child}
        ancestries = []

        for i in range(len(verts)):
            try:
                path = queue.pop(0)
                visit = path[-1]
                visited.add(visit)
                branches = set(self._unvisited_edges(visit, visited))
                if len(branches) == 0:
                    ancestries.append(path)
                else:
                    for i in branches:
                        queue.append(path + [i])
            except IndexError:
                longest_lineage = max([len(i) for i in ancestries])
                earliest_ancestries = [i for i in ancestries if len(i) >= longest_lineage]
                earliest_ancestor = min([i[-1] for i in earliest_ancestries])
                break
            except TypeError:
                earliest_ancestor = -1
                break

        if earliest_ancestor == child:
            earliest_ancestor = -1


        print(earliest_ancestor)


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png

    graph.add_parents(1, 3)
    graph.add_parents(2, 3)
    graph.add_parents(3, 6)
    graph.add_parents(5, 6)
    graph.add_parents(5, 7)
    graph.add_parents(4, 5)
    graph.add_parents(4, 8)
    graph.add_parents(8, 9)
    graph.add_parents(11, 8)
    graph.add_parents(10, 1)


    print(graph.vertices)
    # select longest length test:
    graph.earliest_ancestor(6) # Earliest ancestor is 10
    # select lowest ID test:
    graph.earliest_ancestor(9) # Earliest ancestor is 4
    # handle no parentage test:
    graph.earliest_ancestor(11) # No parents, returns -1
    # handle unmapped input test:
    graph.earliest_ancestor(12) # Invalid, returns -1

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)

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
    

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    # print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # print(graph.dfs(1, 6))
