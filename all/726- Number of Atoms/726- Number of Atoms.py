class Solution:
    def countOfAtoms(self, formula: str) -> str:
        n = len(formula)
        stack = [collections.Counter()]
        i = 0
        
        while i < n:
            if formula[i] == '(':
                stack.append(collections.Counter())
                i += 1
            
            elif formula[i] == ')':
                top = stack.pop()
                i += 1
                v_start = i
                while i < n and formula[i].isdigit():
                    i += 1
                
                v_stop = i
                mul = int(formula[v_start : v_stop] or 1)
                
                for key, val in top.items():
                    stack[-1][key] += val * mul
                
            else:
                start = i
                i += 1
                
                while i < n and formula[i].islower():
                    i += 1
                
                key = formula[start:i]
                start = i
                
                
                while i < n and formula[i].isdigit():
                    i += 1
                
                mul = int(formula[start : i] or 1)
                stack[-1][key] += mul
            
        items = list(stack[0].items())
        items = sorted(items, key = lambda x:x[0])
        ans = ''
        for i, j in items:
            ans += i
            if j > 1:
                ans += str(j)
        
        return ans
