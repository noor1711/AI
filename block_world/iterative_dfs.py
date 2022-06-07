import environment


def iterative_dfs():

    for depth in range(1, 20):
        while len(environment.cue) != 0:
            current = environment.cue.pop()
            if environment.visited[environment.hash_(current)][1] < depth and environment.check(current):
                return True
            environment.actions(current)
        environment.visited.clear()
        print(environment.visited)
    return False


print(iterative_dfs())
