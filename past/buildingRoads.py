class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n + 1)]
        self.sizes = [1 for _ in range(n + 1)]

    def findRepresentatives(self):
        result = []
        for i in range(1, len(self.parents)):
            if self.find(i) == i:
                result.append(i)
        return result

    def find(self, x):
        """
        Returns the representative of x. 
        """
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False

        if self.sizes[rx] > self.sizes[ry]:
            rx, ry = ry, rx
        
        self.parents[rx] = ry
        self.sizes[ry] += self.sizes[rx]

        return True


def main():
    n, m = map(int, input().split())

    cities = UnionFind(n)

    for _ in range(m):
        a, b = map(int, input().split())
        cities.union(a, b)

    representativeCities = cities.findRepresentatives()
    print(len(representativeCities) - 1) # Number of new roads needed
    for i in range(len(representativeCities) - 1):
        print(f"{representativeCities[i]} {representativeCities[i + 1]}")


    
main()

