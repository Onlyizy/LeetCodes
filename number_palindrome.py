class Solution:
    def isPalindrome(self, x: int) -> bool:
        #convert integer to strin
        strx = str(x)
        xlist=[]
        xlistr=[]
        #split string and copy and reverse
        for i in range(len(strx)):
            xlist.append(strx[i])
            v=len(strx)-1-i
            xlistr.append(strx[v])
        #compare each entry
        for n in range(len(xlist)):
            if xlist[n]==xlistr[n]:
                result=True
            else:
                return False
        return result
        #return result
        
        
