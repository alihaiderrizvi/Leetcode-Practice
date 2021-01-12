import collections
class Solution:
    def frequencySort(self, s: str) -> str:
        
        ## APPROACH 1:
        c = collections.Counter(s)
        ans = ''
        while c:
            max_val = 0
            max_key = ''
            
            for k in c:
                if c[k] > max_val:
                    max_val = c[k]
                    max_key = k
            
            ans += max_key*max_val
            del c[max_key]
        
        return ans
        
        
        ## APPROACH 2:
#         d = {}
#         check = set()
#         for i in s:
#             if i not in check:
#                 check.add(i)
#                 count = s.count(i)
#                 if count in d:
#                     d[count].add(i)
#                 else:
#                     d[count] = set(i)
#         items = list(d.items())
#         items = sorted(items, key=lambda x: x[0], reverse=True)
#         ans = ''
#         for i,j in items:
#             for k in j:
#                 ans += k*i
        
#         return ans
        
        
