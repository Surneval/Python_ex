# choosing the shportest way
# new graph. neighbors for start are 'a' and 'b', neighbors are a dict: key: keys: a, b; values: 6, 2
#общий граф
graph = {}
#граф от 'старт' и его соседи + стоимости
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2
#print(graph['start'].keys())
# the same for every node
#граф от "а" и его соседи + стоимости
graph['a'] = {}
graph['a']['fin'] = 1
#граф от "b" и его соседи + стоимости
graph['b'] = {}
graph['b']['fin'] = 5
graph['b']['a'] = 3
#граф от "фин" и его соседи + стоимости
graph['fin'] = {}

infinity = float('inf')
# create costs dictionary
costs = {}
costs['a'] = 6 #to reach 'a' you have to spend 6 items
costs['b'] = 2 #to rich 'b' you have to spend 2 items
costs['fin'] = infinity

# create parents nodes for every node
parents = {}
parents['start'] = None
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

#array for processed nodes
processed = []
# main code

def find_lowest_cost_node(costs):
    lowest_cost = infinity
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs=costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
            way = 'start'
            way += f' -> {parents[n]}'
    processed.append(node)
    node = find_lowest_cost_node(costs=costs)
way += f" -> {'fin'}"



print(f'Dijkstra algorythm: the shortest way will be "{way}".\nThe cost will be {costs["fin"]}')
