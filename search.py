# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

import util
result = []
class SearchProblem:
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).
  
  You do not need to change anything in this class, ever.
  """

  def getStartState(self):
     """
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]
  
def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first
  [2nd Edition: p 75, 3rd Edition: p 87]
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm 
  [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].
  
  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:
  
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  """
  "*** YOUR CODE HERE ***"

  """"    1) fringe - something that hasn't been expanded yet
                     - implemented as a stack
                     
        Basic pseudo code from the book""" 
  fringe = util.Stack()
  visited = []
  start = problem.getStartState()
  if problem.isGoalState(start):
    return result
  fringe.push((start,result))
  while fringe.isEmpty():
    return None
  while not fringe.isEmpty():
    node = fringe.pop()
    check = problem.isGoalState(node[0])
    if check:
      return node[1]
    visited.append(start)
    for child in problem.getSuccessors(node[0]):
      step = []
      step= node[1]+ step
      if child[0] not in visited:
        visited.append(child[0])
        step.append(child[1])
        child_pointer = (child[0],step)
        fringe.push(child_pointer)        
  return result
  util.raiseNotDefined() 
 
def breadthFirstSearch(problem):
  """
  Search the shallowest nodes in the search tree first.
  [2nd Edition: p 73, 3rd Edition: p 82]
  """
  "*** YOUR CODE HERE ***"
  fringe = util.Queue()
  visited = []
  start = problem.getStartState()
  if problem.isGoalState(start):
    return result
  pointer = (start,result)
  fringe.push(pointer)
  while fringe.isEmpty():
      return None
  while not fringe.isEmpty():
    node = fringe.pop()
    if problem.isGoalState(node[0]):
      return node[1]
    visited.append(start)
    for child in problem.getSuccessors(node[0]):
      step = []
      step= node[1]+ step
      if not child[0] in visited:
        visited.append(child[0])
        step.append(child[1])
        child_pointer = (child[0],step)
        fringe.push(child_pointer)        
  return result
  util.raiseNotDefined()
      
def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  "*** YOUR CODE HERE ***"
  
  """ The results should be 
   Cost 68719479864 in 0.0 seconds for python pacman.py -l mediumScaryMaze -p StayWestSearchAgent
  Cost 1 in 0.0 seconds for python pacman.py -l mediumDottedMaze -p StayEastSearchAgent"""
  fringe = util.PriorityQueue()
  start = problem.getStartState()
  if problem.isGoalState(start):
    return result
  visited = []
  F = 0
  pointer = (start, result,F)
  fringe.push(pointer,F)
  while fringe.isEmpty():
      return None
  while not fringe.isEmpty():
    node = fringe.pop()
    if problem.isGoalState(node[0]):
      return node[1]
    visited.append(start)
    for child in problem.getSuccessors(node[0]):
      step = []
      step = node[1]+step
      if not child[0] in visited:
        visited.append(child[0])
        step.append(child[1])
        child_pointer = (child[0],step,node[2] + child[2])
        fringe.push(child_pointer, node[2] + child[2])        
  return result
  util.raiseNotDefined()

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  "*** YOUR CODE HERE ***"

  """ PriorityQueue"""
  """number of expanded nodes should be somewhere in between 500-600"""
  start = problem.getStartState()
  if problem.isGoalState(start):
    return result
  open = util.PriorityQueue()
  close = []
  pointer = (start,result)
  F = 0
  open.push(pointer,F)
  while open.isEmpty():
      return None
  while not open.isEmpty():
    node = open.pop()
    if problem.isGoalState(node[0]):
      return node[1]
    close.append(start)
    for child in problem.getSuccessors(node[0]):
      step = []
      step = node[1] + step
      if not child[0] in close:
        close.append(child[0]) 
        step.append(child[1]) 
        child_pointer =(child[0],step) 
        open.push(child_pointer,
                  problem.getCostOfActions(step) + heuristic(child[0],problem))           
  return result  
  util.raiseNotDefined()
      
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
