# Imports
from queue import PriorityQueue
from json import load
from utils.node import Node

# Main function
def main():
    # Search Space
    start_node = Node('1')
    end_node = Node('50')

    # Priority Queue
    queue = PriorityQueue(maxsize=0)

    # Load first node into Queue
    start_node.set_distance(0)
    queue.put(start_node)

    # Pointer Dictionary
    pointer = {}
    pointer['1'] = None

    # All Nodes
    nodes = []
    nodes.append(start_node)
    
    # Load Data
    with open('utils/Coord.json', 'r') as f:
        Coord = load(f)
    with open('utils/Cost.json', 'r') as f:
        Cost = load(f)
    with open('utils/Dist.json', 'r') as f:
        Dist = load(f)
    with open('utils/G.json', 'r') as f:
        G = load(f)
    
    # Main search
    while not queue.empty():

        # Get smallest value
        cur_node: Node = queue.get()

        # Check if the current node has been visited
        if cur_node.is_visited():
            continue
        else:
            cur_node.visit()

        # Check if destination
        if cur_node.get_num() == end_node.get_num():
            end_node = cur_node
            break

        # For each adjacent node
        for adj_node in G[cur_node.get_num()]:

            # convert to Node class
            adj_node: Node = Node(adj_node)

            # if node has already been created then fetch that node else add new node to the list of nodes
            if adj_node in nodes:
                for node in nodes:
                    if node == adj_node:
                        adj_node = node
                        break
            else:
                nodes.append(adj_node)

            # Set new distance
            if adj_node.set_distance(cur_node.get_distance() + Dist[cur_node.get_num() + ',' + adj_node.get_num()]) and pointer.get(cur_node.get_num()) != adj_node.get_num():
                pointer[adj_node.get_num()] = cur_node.get_num()

            # Add item to queue
            if adj_node not in list(queue.queue):
                queue.put(adj_node)
    
    print("Distance: ", end_node.get_distance())
    
    # Rebuild path
    cur = end_node.get_num()
    print(cur, end=' ')
    while pointer[cur] != None:
        cur = pointer[cur]
        print('<-', cur, end=' ')
    print()

# Run program
if __name__ == '__main__':
    main()