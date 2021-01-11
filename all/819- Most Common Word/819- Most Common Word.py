import collections

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        alphabets = set()
        alphabets.add(' ')
        
        for i in range(ord('a'), ord('z')+1):
            alphabets.add(chr(i))
        
        new_para = ''
        for letter in paragraph:
            if letter in alphabets:
                new_para += letter
            else:
                new_para += ' '
        
        lst_para = new_para.split()
        counter = collections.Counter(lst_para)
        
        for elem in banned:
            del counter[elem]
        
        max_count = 0
        max_key = ''
        
        for k in counter:
            if counter[k] > max_count:
                max_count = counter[k]
                max_key = k
        
        return max_key
