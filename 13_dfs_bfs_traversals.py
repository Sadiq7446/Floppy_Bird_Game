""" Python Script to implement Depth First Search, Breadth First Search 
traversals on a graph """

# Write your code from here

# function for depth first search
def dfs(data, start, visited=set()):
    # if not visited print it
    if start not in visited:
        print("\n",start, end=" ")

    visited.add(start)

    for i in data[start] - visited:

        # if not visited gi in depth of it
        dfs(data, i, visited)
    return


# sample data in dictionary form
data = {
        'A': {'B'},
        'B': {'A', 'C', 'D'},
        'C': {'B', 'E'},
        'D': {'B', 'E'},
        'E': {'C', 'D', 'F'},
        'F': {'E'}
        }


if __name__ == '__main__':
    print("Depth first search :")
    dfs(data, 'A')
  
    


# function for Breadth first search
def bfs(data, start, visited=set()):

    queue = [start]

    while queue:
        current_node = queue.pop(0)
        if current_node not in visited:
            print("\n",current_node, end=" ")
        visited.add(current_node)

        for i in data[current_node] - visited:
            queue.append(i)
    return


if __name__ == '__main__':

    data = {
        'A': {'B'}, 'B': {'A', 'C', 'D'}, 'C': {'B', 'E'}, 'D': {'B', 'E'},
        'E': {'C', 'D', 'F'}, 'F': {'E'}
    }
    print("\nBreadth first search :")
    bfs(data, 'A')

## OUTPUT :
"""
Depth first search :
 A 
 B 
 D 
 E 
 C 
 F 

Breadth first search :
 A 
 B 
 D 
 C 
 E 
 F
"""
