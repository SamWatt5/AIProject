class Problem:
    def __init__(self, initialState, goalState):
        self.initialState = initialState
        self.goalState = goalState

    def actions(self, state):
        # return all actions possible from a state
        actions_list = []
        actions_list

    def result(self, state, action):
        # do action on state and return new state, action is in actions_list in actions function
        new_state = state + action
        return new_state

    def test_if_goal(self, state):
        return state == self.goalState

    def path_cost(self, cost, state1, action, state2):
        # return cost of a solution path that arrives at state2 from state1 via action, default cost = 1,
        return cost+1


class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def child_node(self, problem, action):
        next_state = problem.result(self.state, action)
        next_node = Node(next_state, self, action, problem.path_cost(
            self.path_cost, self.state, action, next_state))
        return next_node

    def expand(self, problem, action):
        # get list of all possible states from this state
        children = []
        for action in problem.actions(self.state):
            children.append(self.child_node(problem, action))
        return children

    def path(self):
        # find a path of nodes to this node
        node = self
        path = []
        while node:
            path.append(node)
            node = node.parent
        return list(reversed(path))

    def solution(self):
        # return every action in the path
        actions = []
        for node in self.path()[1:]:
            actions.append(node.action)
        return actions


class Frontier:
    def __init__(self):
        pass
