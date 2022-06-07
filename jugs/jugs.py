class JugProblem:

    def __init__(self, jug1, jug2, target):
        self.small = jug1, self.big = jug2 if jug2 > jug1 else self.small = jug2, self.big = jug1
        self.frontier = [[0, 0]]
        self.visited = {self.state_value([0, 0]): True}
        self.target = target

    def state_value(self, jugs):
        return jugs[0] + (self.small + 1) * jugs[1]

    def add_to_frontier(self, jugs_list):

        for jugs in jugs_list:
            if jugs == self.target:
                return True

            if self.state_value(jugs) not in self.visited:
                self.visited[self.state(self, jugs)] = True
                self.frontier.append(jugs)

        return False

    def empty_one_out(self, jugs):
        return [0, jugs[1]], [jugs[0], 0]

    def fill_upto_brim(self, jugs):
        return [[self.small, jugs[1]], [jugs[0], self.big]]

    def pour_into_other(self, jugs):
        case1 = []
        # pouring two into one
        if jugs[0] + jugs[1] > self.small:
            case1 = [self.small, jugs[0] + jugs[1] - self.small]
        else:
            case1 = [jugs[0] + jugs[1], 0]

        case2 = []
        # pouring one into two
        if jugs[0] + jugs[1] > self.big:
            case2 = [jugs[0] + jugs[1] - self.big, self.big]
        else:
            case2 = [0, jugs[0] + jugs[1]]

        return [case1, case2]

    def solve(self):

        while len(self.frontier) != 0:
            current_state = self.frontier.pop(0)

            if self.add_to_frontier(self.empty_one_out(current_state)):
                return True
            if self.add_to_frontier(self.fill_upto_brim(current_state)):
                return True
            if self.add_to_frontier(self.pour_into_other(current_state)):
                return True

        return False

jugs_ 3_4 = JugProblem(input("Enter value of jugs and the target").split())
if jugs_3_4.solve():
    print("Can attain target state")
else :
    print("Can't attain target state")