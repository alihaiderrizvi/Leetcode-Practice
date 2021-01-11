import collections
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        c = collections.Counter()
        
        for elem in cpdomains:
            
            num, domain = elem.split()
            num = int(num)
            c.update({domain: num})
            
            for i in range(len(domain)):
                if domain[i] == '.':
                    c.update({domain[i+1:]: num})
        lst = []
        for k,v in c.items():
            lst.append(str(v) + ' ' + k)
        
        return lst
