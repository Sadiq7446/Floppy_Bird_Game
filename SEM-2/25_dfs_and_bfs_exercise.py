
## dfs question :-

"""
Given a data containing managers and their employees as a dictionary of sets, print all employees reporting to a given manager.

data = {
        "karan": {"darshan","nikhil"},
        "darshan": {"khantil", "tanuj"},
        "tanuj": {"nikhil"},
        "krinish": {"hetul"},
        "khantil" : set(),
        "nikhil" : set()
 }

Example: Darshan and Nikhil are reporting to Karan. Khantil and Tanuj are reporting to Darshan.

Q. Find all employees who are reporting to Karan.
"""

## Code from here

def find_employees(data, start, employee, visited=set()):
    # if not visited print it
    if start not in visited:
        print(start, end=" ")
        if start == employee:
            print(":", end=" ")
    visited.add(start)

    for i in data[start] - visited:
        # if not visited go in depth of it
        find_employees(data, i, visited)
    return


# sample data in dictionary form
data = {
    "karan": {"darshan", "nikhil"},
    "darshan": {"khantil", "tanuj"},
    "tanuj": {"nikhil"},
    "krinish": {"hetul"},
    "khantil": set(),
    "nikhil": set()
}


if __name__ == '__main__':

    find_employees(data, "karan", "karan")

## OUTPUT
"""
karan : darshan khantil tanuj nikhil
"""


## bfs question:-

"""
Implement a function to find whether a path exists for a given set of airline routes. The routes are depicted using graphs as a dictionary of sets, where keys represent as source and elements of sets represent destinations. Print the path if it exists.

Example: A, B, C, D, E, F are the nodes of the graph.
For example, if you are given following data:

data = {
        'A': {'B'},
        'B': {'A', 'C', 'D'},
        'C': {'B', 'E'},
        'D': {'B', 'E'},
        'E': {'C', 'D', 'F'},
        'F': {'E'}
}

Example: Source is A, Destination is D.

Expected Output:
Path : A->B->D
"""

## Code from here,

def bfs(data, start, end, visited=[]):
    queue = [start]

    while queue:
        current_node = queue.pop(0)
        if current_node==end:
            print("Path: " + "->".join(visited) + "->" + end)
            return
        visited.append(current_node)

        for i in data[current_node] - set(visited):
            queue.append(i)
    print("Path does not exist!")    
    return


if __name__ == '__main__':
  data = {
    'A': {'B'},
    'B': {'C', 'D'},
    'C': {'E'},
    'D': {'E'},
    'E': {'F'},
    'F': set()
  }
  bfs(data, 'A', 'D')

## OUTPUT 
"""
Path: A->B->D
"""
