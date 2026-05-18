class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for i in range(len(tokens)):
            #print(stack, tokens[i])
            if tokens[i] not in "*-+/":
                stack.append(int(tokens[i]))
            
            elif tokens[i] == "+":
                a = int(stack[-2]) + int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(a)

            elif tokens[i] == "-":
                a =  int(stack[-2]) - int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(a)

            elif tokens[i] == "*":
                a = int(stack[-2]) * int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(a)
            # division
            elif tokens[i] == "/":
                a = int(float(stack[-2]) / int(stack[-1]))
                stack.pop()
                stack.pop()
                stack.append(a)
        
        return int(stack[-1])
        