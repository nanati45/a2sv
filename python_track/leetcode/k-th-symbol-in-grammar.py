class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def grammar (m) :
            m = str(m)
            if m == '0':
                return "01"
            elif m == '1':
                return "10"
        def find(n, k, r):
            if n == 1 :
                return 0

            l = r // 2
            if k > l:
                r -=  l
                k -= l
                y = find( n - 1 , k, r)
                g = grammar(y)
                return int(g[1])
            else:
                r -= l
                y = find( n - 1 , k, r)
                g = grammar(y)
                return int(g[0])
        r = 2 **(n-1)
        return find(n, k , r)
        