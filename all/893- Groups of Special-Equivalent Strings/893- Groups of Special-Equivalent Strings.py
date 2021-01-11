class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        sorted_strings = []
        
        for word in A:
            string_even = ''
            string_odd = ''
            
            for even in word[::2]:
                string_even += even
            
            for odd in word[1::2]:
                string_odd += odd
            
            string_even = ''.join(sorted(string_even))
            string_odd = ''.join(sorted(string_odd))
            
            sorted_strings.append(string_even + string_odd)
            
        return len(set(sorted_strings))
