from collections import deque
import copy


class block_world:
    def __init__(self, start, goal, convert):
        self.start = start
        self.goal = goal
        self.visited = {}
        self.piles = len(start)
        self.cue = deque()
        self.convert = convert
        self.expanded = 0

    def hash_(self, piles):
        hesh = []
        for pile in piles:
            if len(pile) != 0:
                val = 0

                for block in pile:
                    val *= 10
                    val += self.convert[block]
                hesh.append(val)
        # hesh.sort()
        hesh = tuple(hesh)

        return hesh

    def move(self, old, pick, put):
        if len(old[pick]) != 0:  # the pile we're going to pick up from should not be empty
            new = copy.deepcopy(old)

            new[put].append(new[pick][-1])  # just the last
            new[pick] = new[pick][:-1]  # everything but the last

            return new

    def actions(self, state):
        new = []
        for pile in range(self.piles):
            piles = [int(i) for i in range(self.piles)]
            piles.remove(pile)

            for others in piles:
                new.append(self.move(state, pile, others))

        return new

    def backtrack(self, state):
        current = state
        path = []
        while current is not None:
            path.append(current)
            current = self.visited[self.hash_(current)]
        path.reverse()
        return path

    def is_goal(self, current):
        if self.hash_(current) == self.hash_(self.goal):
            print("Goal can be achieved ")
            print(f'Node expanded : {self.expanded} ')
            self.print_path(self.backtrack(self.goal))
            return True
        return False

    def expand(self, current):  # only for bfs and dfs
        for node in self.actions(current):
            if node is not None and self.hash_(node) not in self.visited:
                self.cue.append((node, current))

    def bfs(self):
        self.cue.append((self.start, None))

        while len(self.cue) != 0:
            current, old = self.cue.popleft()

            if self.hash_(current) not in self.visited:
                self.expanded += 1
                self.visited[self.hash_(current)] = old

                if self.is_goal(current):
                    return True

                self.expand(current)

        return False

    def dfs(self):
        self.cue.append((self.start, None))

        while self.cue:
            current, old = self.cue.pop()

            self.expanded += 1
            self.visited[self.hash_(current)] = old

            if self.is_goal(current):
                return True

            self.expand(current)

        return False

    def dfs_depth(self, depth):
        self.cue.append((self.start, None, 1))  # node, parent, path length

        while self.cue:
            current, old, path_length = self.cue.pop()

            if path_length <= depth:
                self.expanded += 1
                self.visited[self.hash_(current)] = old

                if self.is_goal(current):
                    return True

                for node in self.actions(current):
                    if node is not None and self.hash_(node) not in self.visited:
                        self.cue.append((node, current, path_length + 1))

        return False

    def iter_dfs(self, max_depth=30):

        for depth in range(max_depth + 1):
            if self.dfs_depth(depth):
                return True
            self.cue.clear()
            self.visited.clear()
        return False

    def print_path(self, path):
        print(f'Path length : {len(path)}')
        print("Path followed : ")
        for node in path:
            self.print(node)

    def print(self, state):
        for pile in state:
            for block in pile:
                print(block, end=" ")
            print()
        print("-----")


# blocks = {'a': 1, 'b': 2, 'c': 3}
# start_at = [['a'], ['c', 'b'], []]
# goal_at = [['a', 'b', 'c'], [], []]

blocks = {'a': 1, 'b': 2, 'c': 3, 'd':4, 'e':5}
start_at = [['b', 'c','a'],['d', 'e'], []]
goal_at = [['e','d','c','b','a'], [], []]

problem = block_world(start_at, goal_at, blocks)
# print(problem.dfs_depth(1))
# print(problem.iter_dfs())
print(problem.bfs())
# print(problem.dfs())
