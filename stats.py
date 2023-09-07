import numpy
from graph import Graph
from matplotlib import pyplot as plt


# Parameters
WIDTH = 100
HEIGHT = 100
N = 100

ps = numpy.linspace(0,1,20)
percolations = []

for p in ps:
    print(p)
    prop = 0
    for i in range(0, N):
        graph = Graph(WIDTH, HEIGHT, p)
        percolation = graph.percolation()
        if len(percolation) > 0:
            prop += 1
        
    percolations.append(prop / N)

plt.plot(ps, percolations)
plt.show()


