import numpy

def bernoulli(p: float) -> int:
    """'p' is probability of getting 1"""
    r = numpy.random.rand()
    return 0 if r > p else 1


class Graph:
    width: int
    height: int
    vertical_connections: numpy.matrix
    horizontal_connections: numpy.matrix
    p: float
    
    def __init__(self, width: int, height: int, p: float) -> None:
        self.width = width
        self.height = height
        self.p = p

        self.vertical_connections = numpy.matrix([[bernoulli(p) for i in range(0, width)] for j in range(0, height-1)])
        self.horizontal_connections = numpy.matrix([[bernoulli(p) for i in range(0, width-1)] for j in range(0, height)])

    def adjacent(self, pointer: tuple[int]) -> list[tuple[int]]:
        result = []
        row,col = pointer

        if row == self.height-1:
            return result
        elif row == 0:
            return [(1, col)]
        elif self.vertical_connections[row, col] == 1:
            result.append((row+1, col))

        if row>0 and self.vertical_connections[row-1, col] == 1:
            result.append((row-1, col))

        if col<self.width-1 and self.horizontal_connections[row,col] == 1:
            result.append((row,col+1))
        
        if col>0 and self.horizontal_connections[row,col-1] == 1:
            result.append((row,col-1))

        return result

    def percolation(self) -> list[tuple[int]]:
        starts = [(0, col) for col in range(0, self.width) if self.vertical_connections[0,col] == 1]
        visited = []

        for start in starts:
            visited.append(start)
            current_path = [start]
            current_pointer = start
            available = [self.adjacent(start)]

            while len(available) > 0:
                while(len(available[-1]) > 0):
                    current_pointer = available[-1].pop(0)
                    if current_pointer[0] == self.height-1:
                        current_path.append(current_pointer)
                        return current_path
                    current_path.append(current_pointer)
                    visited.append(current_pointer)
                    available.append([node for node in self.adjacent(current_pointer) if node not in visited])
                available.pop()
                current_pointer = current_path.pop()
        
        return []

