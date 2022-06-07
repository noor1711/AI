from collections import deque
import numpy


# deque : a two ended queue

def get_graph():  # gets the input and makes a graph out of it
    graph = []

    while True:
        row_in_matrix = input()

        if len(row_in_matrix) == 0:  # empty input
            break
        row_in_matrix = [int(i) for i in row_in_matrix.strip().split()]
        graph.append(row_in_matrix)

    return graph


class BFS:
    def __init__(self, graph):
        self.graph = graph
        self.cue = deque()
        self.rows = len(graph)
        self.cols = len(graph[0])
        self.visited = numpy.zeros((self.rows, self.cols), dtype=bool)

    def in_graph(self, node):  # to check if node is in graph (is the node valid ? )
        row_index = node[0]
        col_index = node[1]
        if row_index >= self.rows or row_index < 0 or col_index >= self.cols or col_index < 0:
            return False
        return True

    def neighbours(self, current_node):  # find the neighbours of a given node
        row_index = current_node[0]
        col_index = current_node[1]

        up = [row_index - 1, col_index]
        down = [row_index + 1, col_index]
        left = [row_index, col_index - 1]
        right = [row_index, col_index + 1]

        return [up, right, down, left]

    def expand_node(self, current_node):  # add the passing neighbours of node to pur bfs queue

        for neighbour in self.neighbours(current_node):
            row = neighbour[0]
            col = neighbour[1]

            if self.in_graph(neighbour) and not self.visited[row][col]:  # neighbour is valid and not visited
                self.cue.append(neighbour)
                self.visited[row][col] = True

    def bfs(self, start_index):  # do bfs on graph, starting at start_vertex

        self.cue.append(start_index)
        self.visited[start_index[0]][start_index[1]] = True

        while len(self.cue) != 0:
            current_node = self.cue.popleft()
            row = current_node[0]
            col = current_node[1]

            print(self.graph[row][col], end=" ")
            self.expand_node(current_node)


bfs_graph = get_graph()
problem = BFS(bfs_graph)
problem.bfs([0, 0])
