import copy
from collections import deque
from queue import PriorityQueue


class hanoi_solver:
    def __init__(self, discs):
        self.num_discs = discs
        self.num_stacks = 3

        # using just lists for stacks
        # to represent a bigger disc we just give it a higher value
        start_stack = [disc for disc in range(discs, 0, -1)]
        self.start = [[], []]
        self.goal = [[], []]
        self.start.insert(0, start_stack)
        self.goal.append(start_stack)

        self.expanded = 0

        self.visited = {}

    def hash_state(self, state):
        value = []
        for stack in state:
            value.append(tuple(stack))

        return tuple(value)

    def heuristic(self, current):
        one = 0
        two = 0
        if current[0]:
            one = current[0][0]
        if current[1]:
            two = current[1][0]
        max_yet = max(one, two)

        stack = current[2]
        # find the largest
        if stack:
            # find the first point of difference
            for disc in range(len(stack)):
                if stack[disc] != self.goal[2][disc]:
                    max_yet = max(max_yet, self.goal[2][disc])
                    break

        return 2 ** max_yet

    def move(self, old, pick_from, put_to):  # pick and put are the stack numbers
        pick = old[pick_from]
        put = old[put_to]
        if pick and pick_from != put_to:
            top = pick[-1]
            if put and put[-1] < top:  # can't put the box on it
                return None

            new = copy.deepcopy(old)
            new[pick_from] = pick[:-1]
            new[put_to].append(top)

            return new
        return None

    def expand(self, state):
        new = []
        for pick in range(3):
            for put in range(3):
                add = self.move(state, pick, put)
                if add is not None and self.hash_state(add) not in self.visited:
                    new.append(add)

        return new

    def backtrack(self, state):
        current = state
        path = []
        while current is not None:
            path.append(current)
            current = self.visited[self.hash_state(current)]
        path.reverse()
        return path

    def bfs(self):
        cue = deque()
        cue.append([self.start, None])

        while cue:
            current, parent = cue.popleft()

            if self.hash_state(current) not in self.visited:
                self.expanded += 1
                self.visited[self.hash_state(current)] = parent

                if current == self.goal:
                    self.print_path(self.backtrack(self.goal))
                    return True

                for state in self.expand(current):
                    cue.append([state, current])

        return False

    def a_star(self):
        cue = PriorityQueue()
        old = None
        cue.put((self.heuristic(self.start), [self.start, old, 0]))
        # priority, [current, parent, path length upto now]

        while not cue.empty():
            [current, old, path_length] = cue.get()[1]

            if self.hash_state(current) not in self.visited:
                self.expanded += 1
                self.visited[self.hash_state(current)] = old

                if current == self.goal:
                    self.print_path(self.backtrack(self.goal))
                    return True

                for node in self.expand(current):
                    cue.put((self.heuristic(node) + path_length + 1, [node, current, path_length + 1]))

        return False

    def print_path(self, path):
        print("Path followed : ")
        for node in path:
            self.pretty_print(node)
            print('-----------')
        print(f'Nodes expanded : {self.expanded}')
        print(f'Path length : {len(path)}')

    def pretty_print(self, state):
        # iterate column wise instead of row wise
        one = state[0]
        two = state[1]
        three = state[2]
        l1 = len(one)
        l2 = len(two)
        l3 = len(three)

        for level in range(max(l1, l2, l3) - 1, -1, -1):
            if l1 > level:
                print(one[level], end='  ')
            else:
                print(' ', end='  ')

            if l2 > level:
                print(two[level], end='  ')
            else:
                print(' ', end='  ')

            if l3 > level:
                print(three[level], end='  ')
            else:
                print(' ', end='  ')
            print()


disks = int(input('Enter the value of N : '))
problem = hanoi_solver(disks)
problem.a_star()
