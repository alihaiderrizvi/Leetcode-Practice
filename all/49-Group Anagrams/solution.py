class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_copy = strs.copy()
        for i in range(len(strs_copy)):
            
            strs_copy[i] = list(strs_copy[i])
            strs_copy[i].sort()
            strs_copy[i] = ''.join(strs_copy[i])
        
        final_lst = []
        temp = []
        hashmap = {}
        
        for i in range(len(strs_copy)):
            
            if strs_copy[i] in hashmap:
                hashmap[strs_copy[i]].append(i)
            else:
                hashmap[strs_copy[i]] = [i]
        # print(hashmap)
        for j in hashmap:
            temp = []
            for k in hashmap[j]:
                temp.append(strs[k])
            final_lst.append(temp)
        return final_lst
