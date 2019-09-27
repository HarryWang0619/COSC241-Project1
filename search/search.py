# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    stack = util.Stack()    # Use a Lifo Queue in DFS
    start = (problem.getStartState(), [])   # get start state
    result = []     # result to return
    explored = []   # explored set

    stack.push(start)   # push the start state in to the lifo queue

    while (not stack.isEmpty()):  
        (state, path) = stack.pop() # pop node
        if problem.isGoalState(state):  # check whether the state is goal state
            result = path
            return result

        if (state not in explored):   
            explored.append(state)

            for s in problem.getSuccessors(state): 
                stack.push((s[0], path + [s[1]])) #pushed child node, and new path

    return result
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    # In breadth first search functions, we need to use a FIFO queue
    # the logic would be pretty similar
    queue = util.Queue()
    start = (problem.getStartState(), [])
    result = []
    explored = []

    queue.push(start)

    while (not queue.isEmpty()):
        (node, path) = queue.pop()
        if problem.isGoalState(node):
            result = path
            return path

        if (node not in explored):
            explored.append(node)

            for n in problem.getSuccessors(node):
                queue.push((n[0], path + [n[1]]))  #pushed child node, and new path

    return result

    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    priorityQueue = util.PriorityQueue()
    start = (problem.getStartState(), [], 0)
    result = []
    explored = []

    priorityQueue.update(start,0)

    while (not priorityQueue.isEmpty()):
        (node, path, cost) = priorityQueue.pop()
        if problem.isGoalState(node):
            result = path
            return result

        if node not in explored:
            explored.append(node)

            for n in problem.getSuccessors(node):
                priorityQueue.update((n[0], path + [n[1]], cost + n[2]), cost + n[2]) # update the queue with node : (child node, path, priority), and priority


    return result


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    # priority = cost & heuristic
    priorityQueue = util.PriorityQueue() # could also try add heuristic here instead of below but I failed ; )
    start = (problem.getStartState(), [], 0) 
    result = []
    explored = []

    priorityQueue.update(start, heuristic(start[0], problem))

    while (not priorityQueue.isEmpty()):
        (node, path, cost) = priorityQueue.pop()

        if problem.isGoalState(node):
            result = path
            return result

        if node not in explored:
            explored.append(node)

            for n in problem.getSuccessors(node):
                priorityQueue.update((n[0], path + [n[1]], cost + n[2]), cost + n[2] + heuristic(n[0], problem)) 
                # update node, priority
                
                # the cost function is the key.

    return result

    util.raiseNotDefined()

# def Path(node):
#     path = []
#     newNode = node
#     while newNode:
#         path = [newNode[0][1]] + path
#         newNode = newNode[1]
#     return path

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
