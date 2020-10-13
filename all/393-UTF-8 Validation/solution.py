class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        lst = []
        
        for i in data:
            a = bin(i)[2:]
            if len(a) < 8:
                a = '0'*(8-len(a)) + a
            if len(a) > 8:
                a = a[:8]
            
            lst.append(a)
        
        if len(lst) == 1 and lst[0][0] == '0':
            return True
        if len(lst) == 1 and lst[0][0] == '1':
            return False
        
        n_bytes = 0
        
        for num in lst:
            if n_bytes == 0:
                for bit in num:
                    if bit=='0': break
                    n_bytes += 1
                
                if n_bytes == 0:
                    continue
                if n_bytes == 1 or n_bytes > 4:
                    return False
            else:
                if not (num[0] == '1' and num[1] == '0'):
                    return False
            n_bytes -= 1
        
        return n_bytes == 0
