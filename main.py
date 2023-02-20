class Solution():
    n=3
    k=1
    t=0
    def tree(self,n, c='*',k,t):
        while t!=0:
            print(c*k)
            t+=1
            k+=2
    pass

a=Solution
print(a.tree(1, 2, 3,4,5))


