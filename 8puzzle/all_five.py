from queue import PriorityQueue
from collections import deque
import copy
# PriorityQueue is a min priority queue
# so heuristic adjusted accordingly


class puzzle_solver:
    def __init__(self, start, goal):
        self.goal = goal
        self.start = start
        self.visited = {}  # quick dictionary for lookup, list for lookup takes O(n), dictionary is a hash
        self.expanded = 0
        self.solved = False
        self.path = []
        self.ROWS = 3
        self.COLS = 3

    def hamming(self, current):
        ok = 0  # correctly placed tiles
        for box in range(self.ROWS * self.COLS):
            if current[box] == self.goal[box]:
                ok += 1

        return ok

    def misplaced(self, current):  # total tiles - correctly placed
        return self.ROWS * self.COLS - self.hamming(current)

    def expand(self, current_state):  # just returns the new states doesn't enque them or anything
        blank_at = current_state.index(0)  # blank tile
        ROWS = self.ROWS
        COLS = self.COLS

        row = blank_at // ROWS
        col = blank_at % COLS

        swaps = []

        if row != 0:
            swaps.append((row - 1) * ROWS + col)
        if row != ROWS - 1:
            swaps.append((row + 1) * ROWS + col)
        if col != 0:
            swaps.append(row * ROWS + col - 1)
        if col != COLS - 1:
            swaps.append(row * ROWS + col + 1)

        ret = []

        for swap in swaps:
            # print(current_state)
            new_state = copy.deepcopy(current_state)
            new_state[blank_at] = new_state[swap]
            new_state[swap] = 0

            if tuple(new_state) not in self.visited:
                ret.append(new_state)

        return ret

    def dfs(self):  # sets up the enviroment for DFS
        if self.solved:
            return True
        return self.DFS(self.start, None)

    def DFS(self, current, old):
        if tuple(current) not in self.visited:
            self.expanded += 1
            self.visited[tuple(current)] = old

            if current == self.goal:
                self.solved = True
                self.back_track()
                return True

            for node in self.expand(current):  # cue is not empty
                if self.DFS(node, current):
                    return True
        return False

    def bfs(self):

        if self.solved:
            return True

        lifo = deque()
        lifo.append((self.start, None))

        while lifo:
            current, old = lifo.popleft()
            self.expanded += 1
            self.visited[tuple(current)] = old

            if current == self.goal:
                self.solved = True
                self.back_track()
                return True

            for node in self.expand(current):
                lifo.append((node, current))

        return False

    def a_star(self):
        cue = PriorityQueue()
        old = None
        cue.put((-self.hamming(self.start), [self.start, old, 0]))  # priority, [current, parent, path length upto now]

        while not cue.empty():
            self.expanded += 1
            [current, old, path_length] = cue.get()[1]
            self.visited[tuple(current)] = old

            if current == self.goal:
                self.solved = True
                self.back_track()
                return True

            for node in self.expand(current):
                cue.put((-(self.hamming(node)) + path_length + 1, [node, current, path_length + 1]))

        return False

    def best_first(self):
        cue = PriorityQueue()

        old = None
        cue.put((-self.hamming(self.start), [self.start, old]))  # priority, [current, parent]

        while not cue.empty():
            self.expanded += 1
            [current, old] = cue.get()[1]
            self.visited[tuple(current)] = old

            if current == self.goal:
                self.solved = True
                self.back_track()
                return True

            for node in self.expand(current):
                cue.put((self.misplaced(node), [node, current]))

        return False

    def hill_climb(self):
        self.visited[tuple(self.start)] = None
        return self.hill_climb_inner(self.start)

    def hill_climb_inner(self, current):
        self.expanded += 1

        if current == self.goal:
            self.solved = True
            self.back_track()
            return True

        nodes = self.expand(current)
        nodes.sort(key=lambda x: self.misplaced(x))

        for node in nodes:  # error checks done by for loop itself so let it stay
            if tuple(node) not in self.visited: # pick the first best, local maxima is considered, so hill climb is not complete
                self.visited[tuple(node)] = current
                if self.hill_climb_inner(node):
                    return True
                break
            else:
                break

        return False

    def back_track(self):
        self.path = [self.goal]
        old_state = self.visited[tuple(self.goal)]

        while old_state is not None:
            self.path.append(old_state)
            old_state = self.visited[tuple(old_state)]

        self.path.reverse()

    def print(self, state):
        br = 1
        if state is None:
            return
        for i in state:
            print(i, end=" ")
            if br == self.ROWS:
                br = 0
                print()
            br += 1
        print("-----")

    def print_path(self):
        for state in self.path:
            self.print(state)

    def pretty_print(self):
        print(f'Path length = {len(self.path)}')
        print("The path followed was : ")
        self.print_path()

    def solution(self):
        print(f'Nodes expanded = {self.expanded}')
        if self.solved:
            self.pretty_print()
        else:
            print("Sorry this puzzle can't be solved")


# puzzle = puzzle_solver([2, 0, 3, 1, 8, 4, 7, 6, 5], [1, 2, 3, 8, 0, 4, 7, 6, 5])
puzzle = puzzle_solver([2, 8, 3, 1, 5, 4, 7, 6, 0], [1, 2, 3, 8, 0, 4, 7, 6, 5])
# ^ not viable to solve it by anything but a_star, will take a while to run
# puzzle = puzzle_solver([1, 2, 3, 8, 0, 4, 7, 6, 5], [2, 8, 1, 0, 4, 3, 7, 6, 5])
# puzzle = puzzle_solver([0, 1, 3, 4, 2, 5, 7, 8, 6], [1, 3, 0, 4, 2, 5, 7, 8, 6])
puzzle.a_star()
puzzle.solution()
