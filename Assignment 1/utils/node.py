from json import load
from math import sqrt

# Load Coordinate data
with open('utils/Coord.json', 'r') as f:
        Coord = load(f)

# Node structure
class Node(object):

    # Initialisation
    def __init__(self, num:str, budget:float=float('inf')) -> None:
        """Creates new node from given node number.

        Args:
            num (str): The node number as a string from the format in the JSON files.
            budget (int): The energy budget of the current traversal.

        Raises:
            ValueError: Input is not a string, the string is empty or when the given value is not an integer.
        """
        super().__init__()
        # Check correct instance and not blank for num
        if not isinstance(num, str) or num == "":
            raise ValueError("invalid input for num")
        
        # Check that it is an integer
        try:    
            int(num)
        except:
            raise ValueError("num is not a valid integer")

        # check correct instance of budget
        if not isinstance(budget, float):
            raise ValueError("invalid input for budget")

        # Assign values
        self.num = num
        self.distance = float('inf')
        [self.x, self.y] = Coord[self.num]
        self.energy = float('inf')
        self.visited = False
        self.budget = budget

    # Check if Nodes are the same
    def __eq__(self, o) -> bool:
        """Checks to see if two node objects are referring to the same node. Not to be confused with checking equality of the distances of two nodes.

        Args:
            o (object): The node to be compared with.

        Returns:
            bool: True if the node numbers are the same. False otherwise.
        """
        return self.num == o.num

    # Ordering less than
    def __lt__(self, o) -> bool:
        """Checks if current node is closer to origin or uses less energy than the node to be compared with.

        Args:
            o (object): The node to be compared with.

        Returns:
            bool: True if current node distance is lower than the other node.
        """
        if not self._is_valid_operand(o):
            return NotImplemented
        return self.distance < o.distance
    # Ordering more than
    def __gt__(self, o) -> bool:
        """Checks if current node is further to origin or uses more energy than the node to be compared with.

        Args:
            o (object): The node to be compared with.

        Returns:
            bool: True if current node distance is greater than the other node.
        """
        if not self._is_valid_operand(o):
            return NotImplemented
        return self.distance > o.distance
    # Ordering less than or equals
    def __le__(self, o) -> bool:
        """Checks if current node is closer or equidistant to origin or uses less or equal energy than the node to be compared with.

        Args:
            o (object): The node to be compared with.

        Returns:
            bool: True if current node distance is lower or equal to the other node.
        """
        if not self._is_valid_operand(o):
            return NotImplemented
        return self.distance <= o.distance

    # Ordering more than or equals
    def __ge__(self, o) -> bool:
        """Checks if current node is further or equidistant to origin or uses more or equal energy than the node to be compared with.

        Args:
            o (object): The node to be compared with.

        Returns:
            bool: True if current node distance is greater or equal to the other node.
        """
        if not self._is_valid_operand(o):
            return NotImplemented
        return self.distance >= o.distance

    # String representation
    def __repr__(self) -> str:
        """The string representation of this node so that it is easier to read in console and the debugger.

        Returns:
            str: The string representation as Node(id:_, distance:_).
        """
        return f"Node(id:{self.num}, d:{self.distance}, e:{self.energy}, b:{self.budget}, x:{self.x}, y:{self.y})"

    # String representation
    def __str__(self) -> str:
        """The string representation of this node so that it is easier to read in console and the debugger.

        Returns:
            str: The string representation as Node(id:_, distance:_).
        """
        return f"Node(id:{self.num}, d:{self.distance}, e:{self.energy}, b:{self.budget}, x:{self.x}, y:{self.y})"

    # Checks if other object has required attribute distance
    def _is_valid_operand(self, o) -> bool:
        """Checks if the object to be compared with has the necessary distance attribute.

        Args:
            o (object): The object to be compared with.

        Returns:
            bool: True if the object has the required attribute, False if it does not.
        """
        return hasattr(o, "distance") and hasattr(o, "energy")

     # Checks if other object has required coordinate attributes
    def _is_valid_coordinate(self, o) -> bool:
        """Checks if the object to be compared with has the necessary coordinate attribute.

        Args:
            o (object): The object to be compared with.

        Returns:
            bool: True if the object has the required attributes, False if it does not.
        """
        return hasattr(o, "x") and hasattr(o, "y")

    # Set Distance
    def set_distance(self, distance:float, energy:float=float('inf')) -> bool:
        """Sets the new lowest distance of the current node from the origin.

        Args:
            distance (float): The distance from the origin node.
            energy (float): The used to travel from the origin node.

        Returns:
            bool: True if the new distance was lower than the distance of the node and energy is lower or equal to the energy of the node. False otherwise.
        """
        if energy <= self.energy and distance < self.distance and energy <= self.budget:
            self.distance = distance
            self.energy = energy
            return True
        return False
    
    # Get Distance
    def get_distance(self) -> float:
        """Returns the current distance of the node from the origin node.

        Returns:
            float: The distance of the node from the origin.
        """
        return self.distance
    
    # Get Energy
    def get_energy(self) -> float:
        """Returns the current energy of the node from the origin node.

        Returns:
            float: The energy of the node from the origin.
        """
        return self.energy
    
    # Get Num
    def get_num(self) -> str:
        """The node number as a string.

        Returns:
            str: The id of the node as a string as per the JSON files.
        """
        return self.num
    
    # Marks node as visited
    def visit(self) -> None:
        """Sets the current node as visited.
        """
        self.visited = True

    # Checks if node is visited
    def is_visited(self) -> bool:
        """Returns a boolean representing if the current node has been visited.

        Returns:
            bool: True if node has been visited, False otherwise.
        """
        return self.visited

    # Euclidian Distance between 2 nodes
    def distance(self, o) -> float:
        """Returns the Euclidian distance between 2 nodes.

        Args:
            o (Node): The other node in the computation.

        Returns:
            float: The distance betwen 2 nodes.
        """
        if not self._is_valid_coordinate(o):
            return NotImplemented
        return sqrt((self.x - o.x)**2 + (self.y - o.y)**2)

