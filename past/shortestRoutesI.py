import heapq


def shortestRoutesI(graph):
    n = len(graph)

    distances = [float("inf") for _ in range(n)]
    distances[1] = 0

    pq = [(0, 1)] # distance, node
    while len(pq) > 0:
        currentDistance, currentNode = heapq.heappop(pq)

        if currentDistance > distances[currentNode]:
            continue
    
        for neighbor, distanceToNeighbor in graph[currentNode]:
            totalDistanceToNeighbor = distanceToNeighbor + currentDistance
            if totalDistanceToNeighbor < distances[neighbor]:
                distances[neighbor] = totalDistanceToNeighbor
                heapq.heappush(pq, (totalDistanceToNeighbor, neighbor))
    
    return distances[1:]




def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)] # (vertex, edge weight)

    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
    
    shortestDistances = map(str, shortestRoutesI(graph))
    print(" ".join(shortestDistances))

main()