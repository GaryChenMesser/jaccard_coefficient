import networkx as nx
import time

def _apply_prediction(G, func, ebunch=None):
    if ebunch is None:
        ebunch = nx.non_edges(G)
    return ((u, v, func(u, v)) for u, v in ebunch)
'''
def number_of_common_neighbors(G, u, v):
	number = 0
	for a in G[u]:
		if a in G[v]:
			number += 1
	return number
'''
def my_jaccard_coefficient(G, ebunch=None):
	def predict(u, v):
		intersection_size = len(set(G[u]) & set(G[v]))
		union_size = len(set(G[u]) | set(G[v]))
		if union_size == 0:
			return 0
		#return number_of_common_neighbors(G, u, v) / union_size
		return intersection_size / union_size
	return _apply_prediction(G, predict, ebunch)

nodes = 50
loop = 4
my_time = []
off_time = []
my_grow = []
off_grow = []
for a in range(loop):
	G = nx.gnp_random_graph(nodes, 0.1)
	ending = time.process_time()
	off_jc = list(nx.jaccard_coefficient(G))
	start = time.process_time()
	my_jc = list(my_jaccard_coefficient(G))
	_time = time.process_time()
	off_time.append(start - ending)
	my_time.append(_time - start)
	nodes *= 2

for a in range(loop - 1):
	off_grow.append(off_time[a + 1] / off_time[a])
	my_grow.append(my_time[a + 1] / my_time[a])

print('jaccard_coefficient : ', off_time)
print(off_grow)
print('my_jaccard_coefficient : ', my_time)
print(my_grow)
print(off_jc == my_jc)
