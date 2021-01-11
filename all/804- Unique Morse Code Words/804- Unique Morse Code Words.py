class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        letters = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        s = set()
        
        for word in words:
            string = ''
            
            for w in word:
                string += letters[ord(w)-ord('a')]
            
            s.add(string)
        
        return len(s)
