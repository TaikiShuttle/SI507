import Node
import json
import pop_dict

population_dict = pop_dict.pop_dict

def constructTree():
    # read in the cached data
    f = open("restaurant_info.json")
    restaurant_list = json.loads(f.read())
    
    # construct a list of Node
    node_list = [Node.Node(x, population_dict) for x in restaurant_list]

    # construct a tree
    kdtree = Node.KDTree(node_list)
    kdtree.build()

    return kdtree