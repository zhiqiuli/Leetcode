import collections
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if len(bank) == 0:
            return -1
        bank = set(bank)
        dist = {}
        dist[start] = 0
        queue = collections.deque([start])
        while queue:
            gene = queue.popleft()
            for gene_next in self.make_gene_next(gene):
                if gene_next in bank:
                    if gene_next == end:
                       return dist[gene] + 1                
                    if gene_next not in dist:
                        dist[gene_next] = dist[gene] + 1
                        queue.append(gene_next)
        return -1
    
    def make_gene_next(self, gene):
        availables = ['A', 'C', 'G', 'T']
        res = []
        for i in range(len(gene)):
            for new in availables:
                if gene[i] != new:
                    res.append(gene[:i] + new + gene[i+1:])
        return res