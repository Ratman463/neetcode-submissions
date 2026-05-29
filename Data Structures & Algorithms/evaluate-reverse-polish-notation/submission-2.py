class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        if len(tokens) < 1:
            return 0

        tk: deque[int] = deque([])
        ops = set(['+', '-', '*', '/'])
        
        for t in tokens:
            if t not in ops:
                tk.append(int(t))
            else:
                op = t
                num1 = tk.pop()
                num2 = tk.pop()
                res = 0
                if op == '+':
                    res = num2 + num1
                elif op == '-':
                    res = num2 - num1
                elif op == '*':
                    res = num2 * num1
                elif op == '/':
                    res = (int)(num2 / num1)
                tk.append(res)


        return tk.pop()