# Question : Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().


# Time Complexity : O(n)


# Space Complexity : O(n)


    def calculate(self, s: str) -> int:
        stack = []
        result = 0
        sign = 1
        i = 0
        while i < len(s):
            if s[i].isdigit():
                num = 0
                while i<len(s) and s[i].isdigit():
                    num = num*10 + int(s[i])
                    i+= 1
                result += sign*num
                continue
            elif s[i] == "+":
                sign = 1
            elif s[i] == "-":
                sign = -1
            elif s[i] == "(":
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif s[i] == ")":
                prev_sign = stack.pop()
                prev_res = stack.pop()

                result =prev_res + prev_sign*result
            i+= 1
        
        return result
