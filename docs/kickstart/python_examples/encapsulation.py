class MarbleJar:
    def __init__(self, material: str, capacity: int,
                 num_marbles: int = 0):
        self._material = material
        self._capacity = capacity
        self._num_marbles = num_marbles
    
    @property
    def material(self) -> str: return self._material

    @property
    def capacity(self) -> int: return self._capacity

    @property
    def num_marbles(self) -> int: return self._num_marbles

    @num_marbles.setter
    def num_marbles(self, new_num_marbles: int):
        if new_num_marbles < 0:
            raise ValueError("Number of marbles cannot be less than 0")
        
        self._num_marbles = new_num_marbles