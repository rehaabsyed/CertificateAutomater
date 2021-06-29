class MarbleJar:
    def __init__(self, material, capacity, num_marbles = 0):
        self._material = material
        self._capacity = capacity
        self._num_marbles = num_marbles
    
    @property
    def material(self): return self._material

    @property
    def capacity(self): return self._capacity

    @property
    def num_marbles(self): return self._num_marbles

    @num_marbles.setter
    def num_marbles(self, new_num_marbles):
        if new_num_marbles < 0:
            raise ValueError("Number of marbles cannot be less than 0")
        
        self._num_marbles = new_num_marbles