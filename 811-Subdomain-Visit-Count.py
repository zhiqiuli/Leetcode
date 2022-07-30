class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counter = {}
        for cp in cpdomains:
            count  = int(cp.split(' ')[0])
            domain = cp.split(' ')[1]
            while '.' in domain:
                counter[domain] = counter.get(domain, 0) + count
                
                # look for next domain
                domain = domain[domain.find('.')+1:]
            
            # the very last one of the domain
            counter[domain] = counter.get(domain, 0) + count        
        
        return [str(counter[key]) + ' ' + key for key in counter]