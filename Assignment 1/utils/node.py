# Node structure
class Node(object):

    # Initialisation
    def __init__(self, num:str="") -> None:
        super().__init__()
        # Check correct instance and not blank
        if not isinstance(num, str) or num == "":
            raise ValueError("invalid input for num")
        
        # Check that it is an integer
        try:    
            int(num)
        except:
            raise ValueError("num is not a valid integer")

        # Assign values
        self.num = num
        self.distance = float('inf')
        self.visited = False

    # Check if Nodes are the same
    def __eq__(self, o) -> bool:
        return self.num == o.num

    # Ordering less than
    def __lt__(self, o) -> bool:
        if not self._is_valid_operand(o):
            return NotImplemented
        return self.distance < o.distance

    # Ordering more than
    def __gt__(self, o) -> bool:
        if not self._is_valid_operand(o):
            return NotImplemented
        return self.distance > o.distance

    # Ordering less than or equals
    def __le__(self, o) -> bool:
        if not self._is_valid_operand(o):
            return NotImplemented
        return self.distance <= o.distance

    # Ordering more than or equals
    def __ge__(self, o) -> bool:
        if not self._is_valid_operand(o):
            return NotImplemented
        return self.distance >= o.distance

    # Checks if other object has required attribute distance
    def _is_valid_operand(self, o):
        return hasattr(o, "distance")

    # Set Distance
    def set_distance(self, distance:float):
        if distance < self.distance:
            self.distance = distance
            return True
        return False
    
    # Get Distance
    def get_distance(self):
        return self.distance
    
    # Get Num
    def get_num(self):
        return self.num

    def __repr__(self) -> str:
        return f"Node(id:{self.num}, distance:{self.distance})"

    def __str__(self) -> str:
        return f"Node(id:{self.num}, distance:{self.distance})"
    
    def visit(self):
        self.visited = True

    def is_visited(self):
        return self.visited
