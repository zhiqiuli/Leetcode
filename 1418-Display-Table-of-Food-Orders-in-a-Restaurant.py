class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        all_items  = []
        all_tables = {}
        for _, table, item in orders:
            if item not in all_items:
                all_items.append(item)
            
            table = int(table)
            
            all_tables[table] = all_tables.get(table, {})
            
            if item not in all_tables[table]:
                all_tables[table][item] = 1
            else:
                all_tables[table][item] += 1
        
        all_items      = sorted(all_items)
        all_tables_num = sorted(all_tables)
                        
        res = [['Table'] + all_items]
        for table in all_tables_num:
            res_ = [str(table)]
            for item in all_items:
                num = all_tables[table].get(item, 0)
                res_.append(str(num))
            res.append(res_[:])
                
        return res
