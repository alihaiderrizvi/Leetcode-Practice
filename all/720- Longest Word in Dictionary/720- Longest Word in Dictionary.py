class Solution:
    def longestWord(self, words: List[str]) -> str:
        s = set(words)
        good = set()
        
        for word in words:
            n = len(word)
            flag = True
            
            while n >= 1:
                if word[:n] not in s:
                    flag = False
                n -= 1
            
            if flag:
                good.add(word)
        
        good = list(good)
        
        d = {}
        for i in good:
            if len(i) not in d:
                d[len(i)] = [i]
            else:
                d[len(i)].append(i)
        
        max_count = max(list(d.keys()))
        main_ans = d[max_count]
        main_ans.sort()
        return main_ans[0]
