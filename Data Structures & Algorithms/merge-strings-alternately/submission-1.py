class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l= 0
        r = 0
        w1 = list(word1)
        w2 = list(word2)
        output = []
        while l<len(w1) and r<len(w2):
            output.append(w1[l])
            l+=1
            output.append(w2[r])
            r+=1
        if l>=len(w1):
            for i in range(r,len(w2)):
                output.append(w2[i])
        
        elif r>=len(w2):
            for i in range(l,len(w1)):
                output.append(w1[i])
        
        return "".join(output)


            
        
            

