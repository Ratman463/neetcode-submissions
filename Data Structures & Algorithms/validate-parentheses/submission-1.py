class Solution:
    def isValid(self, s: str) -> bool:
        q: deque[str] = deque([])
        for chr in s:
            if chr in ['(','{', '[']:
                q.append(chr)
            elif len(q) == 0:
                return False
            else:
                tail = q[-1]
                if chr == ')' and tail == '(':
                    q.pop()
                elif chr == '}' and tail == '{':
                    q.pop()
                elif chr == ']' and tail == '[':
                    q.pop()
                else:
                    return False
        return len(q) == 0