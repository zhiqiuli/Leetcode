from collections import defaultdict
class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        # 建立一棵树
        tree = defaultdict(list)
        for i, j in edges:
            tree[i].append(j)
            tree[j].append(i)
        
        # 同时传入node和parent，当i==parent时说明访问方向不正确
        def dfs(node, parent):
            s = 1
            children = []
            for i in tree[node]:
                if i == parent:
                    continue
                size = dfs(i, node)
                s += size
                children.append(size)
            
            if len(set(children)) <= 1:
                self.good_nodes += 1
            
            return s
        
        # 使用一个全局变量存贮结果
        self.good_nodes = 0
        dfs(0, -1)
        return self.good_nodes