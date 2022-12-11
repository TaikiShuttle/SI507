import math

class Node:
    def __init__(self, dict_t:dict, pop_dict_t: dict) -> None:
        '''
        Create a node using the infomation from an element from the JSON, which is a dict. Also use the pop_dict to initialize population
        '''
        # node info
        self.rating = float(dict_t['rating'])
        self.link = dict_t['url']
        self.name = dict_t['name']
        self.price = math.inf
        if "price" in dict_t.keys():
            self.price = float(len(dict_t["price"]))
        else:
            self.price = math.inf
        
        self.zipcode = dict_t['location']['zip_code']

        # try to find the population in the dict, if there is no zipcode, assign 0
        try:
            self.population = float(pop_dict_t[self.zipcode])
        except:
            self.population = 0
        
        # structure info
        self.parent = None
        self.left = None
        self.right = None

    def is_leaf(self):
        if self.left == None and self.right == None:
            return True
        else:
            return False



# k-d tree
# use population as x-axis, rating as y-axis, price as z-axis, name as w-axis
# Path: KDTree.py
class KDTree:
    def __init__(self, list_t:list) -> None:
        self.root = None
        self.list_t = list_t

    def build(self):
        self.root = self.build_helper(self.list_t, 0)
    
    def build_helper(self, list_t:list, depth:int):
        '''
        ---
        build a kdtree from list of Node on current depth
        ---
        Input: list_t, a list of Node
        ---
        Return: the root of the kdtree
        '''
        if len(list_t) == 0:
            return None

        if len(list_t) == 1:
            return list_t[0]
        
        # depend on the depth, choose the discriminator, and find the median as the root of this level
        # sort by x-axis
        if depth % 4 == 0:
            list_t.sort(key=lambda x: x.population)
        # sort by y-axis
        elif depth % 4 == 1:
            list_t.sort(key=lambda x: x.rating)
        # sort by z-axis
        elif depth % 4 == 2:
            list_t.sort(key=lambda x: x.price)
        else:
            list_t.sort(key=lambda x: x.name)
        
        # choose the left one if the length is even
        mid = (len(list_t) - 1) // 2
        node = list_t[mid]
        node.left = self.build_helper(list_t[ :mid], depth + 1)
        node.right = self.build_helper(list_t[mid + 1:], depth + 1)
        if node.left != None:
            node.left.parent = node
        if node.right != None:
            node.right.parent = node
        return node

    def search(self, zipcode: int, rating: float, price: int, name: str):
        return self.search_helper(self.root, zipcode, rating, price, name, 0)

    def search_helper(self, node: Node, population: float, rating: float, price: int, name: str, depth: int):
        '''
        search the node with the given information, return the node if found, otherwise return None
        ---
        Input: node as the root of the subtree, target information
        ---
        Return: the node if found, otherwise return None
        '''
        if node == None:
            return None
        if node.population == population and node.rating == rating and node.price == price and node.name == name:
            return node
        if depth % 4 == 0:
            if population < node.population:
                return self.search_helper(node.left, population, rating, price, name, depth + 1)
            else:
                return self.search_helper(node.right, population, rating, price, name, depth + 1)
        elif depth % 4 == 1:
            if rating < node.rating:
                return self.search_helper(node.left, population, rating, price, name, depth + 1)
            else:
                return self.search_helper(node.right, population, rating, price, name, depth + 1)
        elif depth % 4 == 2:
            if price < node.price:
                return self.search_helper(node.left, population, rating, price, name, depth + 1)
            else:
                return self.search_helper(node.right, population, rating, price, name, depth + 1)        
        else:
            if name < node.name:
                return self.search_helper(node.left, population, rating, price, name, depth + 1)
            else:
                return self.search_helper(node.right, population, rating, price, name, depth + 1)

    def single_search(self, node: Node, query, how = "name"):
        '''
            search the tree rooted in node with the given query, return all the nodes that match the query, return [] if no match
            how indicates which dimension to search
            ---
            Input: node as the root of the subtree, query, how = (name, population, rating, price, zipcode)
            ---
            Return: a list of nodes that match the query
        '''
        # do a depth first search to find the node
        result = []
        if node == None:
            return []
        if how == "name":
            if node.name == query:
                result += [node]
        elif how == "zipcode":
            if node.zipcode == query:
                result += [node]
        elif how == "rating":
            if node.rating == query:
                result += [node]
        elif how == "price":
            if node.price == query:
                result += [node]
        elif how == "population":
            if node.population == query:
                result += [node]
        else:
            return []
        left = self.single_search(node.left, query, how)
        right = self.single_search(node.right, query, how)

        # merge the result
        if left == []:
            return result + right
        elif right == []:
            return result + left
        else:
            return result + left + right

    def delete(self, node: Node, population: float, rating: float, price: int, name: str, depth: int):
        '''
            delete node with the given information
            ---
            Input: 
            Node: the root node to start search
            target node information
            current depth
            ---
            Return: the replaced node
        '''
        if node == None:
            return None

        # if the node is target node
        if node.population == population and node.rating == rating and node.price == price and node.name == name:
            # if the node is leaf, just delete it
            if node.is_leaf():
                if node.parent.left == node:
                    node.parent.left = None
                else:
                    node.parent.right = None
                return node

            # if the node is not a leaf, try to find the smallest element in this dimension in that subtree
            else:
                # first find the smallest element in the right subtree
                if node.right != None:
                    minNode = self.findMin(node.right, depth % 4, depth + 1)

                    # replace node
                    self.nodeCopy(node, minNode)
                
                    # cascade to delete the minNode in the right subtree
                    node.right = self.delete(node.right, minNode.population, minNode.rating, minNode.price, minNode.name, depth + 1)

                # if the node has no right subtree, find the left subtree
                else:
                    maxNode = self.findMax(node.left, depth % 4, depth + 1)

                    # replace node
                    self.nodeCopy(node, maxNode)

                    # cascade to deltete the maxNode in the left subtree
                    node.left = self.delete(node.left, maxNode.population, maxNode.rating, maxNode.price, maxNode.name, depth + 1)

        # if the node is not target node, search in the left or right subtree
        else:
            if depth % 4 == 0:
                if population < node.population:
                    node.left = self.delete(node.left, population, rating, price, name, depth + 1)
                else:
                    node.right = self.delete(node.right, population, rating, price, name, depth + 1)
            elif depth % 4 == 1:
                if rating < node.rating:
                    node.left = self.delete(node.left, population, rating, price, name, depth + 1)
                else:
                    node.right = self.delete(node.right, population, rating, price, name, depth + 1)
            elif depth % 4 == 2:
                if price < node.price:
                    node.left = self.delete(node.left, population, rating, price, name, depth + 1)
                else:
                    node.right = self.delete(node.right, population, rating, price, name, depth + 1)
            else:
                if name < node.name:
                    node.left = self.delete(node.left, population, rating, price, name, depth + 1)
                else:
                    node.right = self.delete(node.right, population, rating, price, name, depth + 1)

        return node

    def print(self):
        self.print_helper(self.root, 0)

    def print_helper(self, node: Node, depth: int):
        if node == None:
            return
        self.print_helper(node.left, depth + 1)
        print('  ' * depth, node.population, node.rating, node.price, node.name)
        self.print_helper(node.right, depth + 1)

    def treeRange(self, node: Node, depth: int):
        '''
            return the range of the tree in all 4 dimensions
        '''
        # use findMin and findMax to find the range
        minNode = self.findMin(node, 0, depth)
        maxNode = self.findMax(node, 0, depth)
        minPopulation = minNode.population
        maxPopulation = maxNode.population

        minNode = self.findMin(node, 1, depth)
        maxNode = self.findMax(node, 1, depth)
        minRating = minNode.rating
        maxRating = maxNode.rating

        minNode = self.findMin(node, 2, depth)
        maxNode = self.findMax(node, 2, depth)
        minPrice = minNode.price
        maxPrice = maxNode.price

        minNode = self.findMin(node, 3, depth)
        maxNode = self.findMax(node, 3, depth)
        minName = minNode.name
        maxName = maxNode.name

        return [minPopulation, maxPopulation, minRating, maxRating, minPrice, maxPrice, minName, maxName]
    
    def rangeSearch(self, node: Node, ranges: list, depth: int):
        '''
            return all the nodes in the given range
            ---
            Input:
            node: the root node to start search
            ranges: the range to search [minPopulation, maxPopulation, minRating, maxRating, minPrice, maxPrice, minName, maxName]
            depth: current depth
            ---
            Return: a list of nodes in the given range
        '''
        if node == None:
            return []

        # if the tree range does not overlap with the given range, return empty list
        if self.treeRange(node, depth)[0] > ranges[1] or self.treeRange(node, depth)[1] < ranges[0] or self.treeRange(node, depth)[2] > ranges[3] or self.treeRange(node, depth)[3] < ranges[2] or self.treeRange(node, depth)[4] > ranges[5] or self.treeRange(node, depth)[5] < ranges[4] or self.treeRange(node, depth)[6] > ranges[7] or self.treeRange(node, depth)[7] < ranges[6]:
            return []

        # if the tree range contained in the given range, return the whole tree
        if self.treeRange(node, depth)[0] >= ranges[0] and self.treeRange(node, depth)[1] <= ranges[1] and self.treeRange(node, depth)[2] >= ranges[2] and self.treeRange(node, depth)[3] <= ranges[3] and self.treeRange(node, depth)[4] >= ranges[4] and self.treeRange(node, depth)[5] <= ranges[5] and self.treeRange(node, depth)[6] >= ranges[6] and self.treeRange(node, depth)[7] <= ranges[7]:
            return self.inorder(node)

        set_t = set()
        # if the node in the given range, add it to the set
        if node.population >= ranges[0] and node.population <= ranges[1] and node.rating >= ranges[2] and node.rating <= ranges[3] and node.price >= ranges[4] and node.price <= ranges[5] and node.name >= ranges[6] and node.name <= ranges[7]:
            set_t.add(node)

        # recursively call rangeSearch on the left and right subtree
        set_t = set_t.union(set(self.rangeSearch(node.left, ranges, depth + 1)))
        set_t = set_t.union(set(self.rangeSearch(node.right, ranges, depth + 1)))

        return list(set_t)


    def inorder(self, node: Node):
        '''
            return the inorder traversal of the tree
        '''
        if node == None:
            return []
        return self.inorder(node.left) + [node] + self.inorder(node.right)
    
    def compareDim(self, Node1, Node2, dimComp, how = "smaller"):
        '''
        compare two nodes in the dimension dimComp, return the smaller/larger one. Use how= to define smaller/larger.
        '''
        # Node1 and Node2 can be none
        if Node1 == None and Node2 == None:
            return None
        elif Node1 == None:
            return Node2
        elif Node2 == None:
            return Node1
        else:
            if how == "smaller":
                if dimComp == 0:
                    return Node1 if Node1.population < Node2.population else Node2
                elif dimComp == 1:
                    return Node1 if Node1.rating < Node2.rating else Node2
                elif dimComp == 2:
                    return Node1 if Node1.price < Node2.price else Node2
                else:
                    return Node1 if Node1.name < Node2.name else Node2
            else:
                if dimComp == 0:
                    return Node1 if Node1.population > Node2.population else Node2
                elif dimComp == 1:
                    return Node1 if Node1.rating > Node2.rating else Node2
                elif dimComp == 2:
                    return Node1 if Node1.price > Node2.price else Node2
                else:
                    return Node1 if Node1.name > Node2.name else Node2

    def findMin(self, node: Node, dimComp: int, depth : int):
        '''
        find the minimum node in the subtree rooted node, in the dimension dimComp (0-3)
        ---
        Input:
            node: the root of the subtree
            dimComp: the dimension to compare
            depth: the depth of the current node
        ---
        Return:
            the minimum node in the subtree in the dimension dimComp
        '''
        if node == None:
            return None

        # no matter what depth is, the left subtree are all candidates
        min = self.findMin(node.left, dimComp, depth + 1)

        # if the current depth is not the comparision dimension, then the right subtree are all candidates
        if(dimComp != depth % 4):
            rightMin = self.findMin(node.right, dimComp, depth + 1)

            # compare the min with the rightMin, return the smaller one in dimension dimComp
            min = self.compareDim(min, rightMin, dimComp, how = "smaller")
        
        return self.compareDim(min, node, dimComp, how = "smaller")

    def findMax(self, node: Node, dimComp: int, depth : int):
        '''
        find the maximum node in the subtree rooted node, in the dimension dimComp (0-3)
        ---
        Input:
            node: the root of the subtree
            dimComp: the dimension to compare
            depth: the depth of the current node
        ---
        Return:
            the maximum node in the subtree in the dimension dimComp
        '''
        if node == None:
            return None

        # no matter what depth is, the right subtree are all candidates
        max = self.findMax(node.right, dimComp, depth + 1)

        # if the current depth is not the comparision dimension, then the left subtree are all candidates
        if(dimComp != depth % 4):
            leftMax = self.findMax(node.left, dimComp, depth + 1)

            # compare the max with the rightMax, return the smaller one in dimension dimComp
            max = self.compareDim(max, leftMax, dimComp, how = "larger")
        
        return self.compareDim(max, node, dimComp, how = "larger")

    def nodeCopy(self, dst: Node, src: Node):
        '''
        copy the information from src to dst
        '''
        dst.population = src.population
        dst.rating = src.rating
        dst.price = src.price
        dst.name = src.name
        dst.zipcode = src.zipcode
        return 


