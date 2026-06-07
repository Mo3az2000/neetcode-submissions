class Solution:  
    # answer = []
    def __init__(self):
        self.answer = []
    
    def gp(self, r: int, l: int, s: str):
        if(l == 0 and r == 0):
            self.answer.append(s)
            return
        else:
            if(r==l):
                self.gp(r,l-1,s+"(")
            elif(r>l):
                self.gp(r-1,l,s+")")
                if(l>0):
                    self.gp(r,l-1,s+"(")

                

    def generateParenthesis(self, n: int) -> List[str]:
        self.gp(r=n,l=(n-1),s="(")
        return self.answer

