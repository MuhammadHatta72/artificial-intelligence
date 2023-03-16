from unittest import result


DAG = {
        'A' : {'C' : 4, 'G' : 9},
        'G' : {'E' : 6},
        'C' : {'D' : 6, 'H' : 12},
        'D' : {'E' : 7},
        'H' : {'F' : 15},
        'E' : {'F' : 8},
        'F' : {'B' : 5}}
        
def shortest_path(graph, source, dest):
    result = []
    result.append(source)

    while dest not in result:
        current_node = result[-1]
        local_max = min(graph[current_node].values())
        for node, weight in graph[current_node].items():
            if weight == local_max:
                result.append(node)
    return result


print(shortest_path(DAG, 'A', 'F'))

def dijsktra(graph, source, dest):
    shortest_distance = {source: (None, 0)}
    current_node = source
    visited = set()

    while current_node != dest:
        visited.add(current_node)
        destinations = graph[current_node]
        weight_to_current_node = shortest_distance[current_node][1]

        for next_node in destinations:
            weight = graph[current_node][next_node] + weight_to_current_node
            if next_node not in shortest_distance:
                shortest_distance[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_distance[next_node][1]
                if current_shortest_weight > weight:
                    shortest_distance[next_node] = (current_node, weight)
        
        next_destinations = {node: shortest_distance[node] for node in shortest_distance if node not in visited}
        if(not next_destinations):
            return "Route Not Possible"

        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])

    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_distance[current_node][0]
        current_node = next_node

    path = path[::-1]
    return path

print(dijsktra(DAG, 'A', 'F'))