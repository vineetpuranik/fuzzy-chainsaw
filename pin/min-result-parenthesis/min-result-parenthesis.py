class Solution:
    def minimizeResult(self, expression: str) -> str:
        # print all the possible expressions
        # expression : 247 + 38 
        # index of + sign = 3
        # total number of characters in the expression = 6
        # new length would be 6 + 2 = 8 
        # left bracket can go from 0 to + - 1
        # right bracket can go from end to end to + sign index
        
        # store all possible expressions with legal positioning of parenthesis
        expressions = []
        plusIndex = 0
        
        # get the index of + sign 
        for i in range(len(expression)) :
            if expression[i] == '+':
                plusIndex = i
                break
        
        # opening bracket can be placed anywhere from 0th index to 
        # position of plusIndex - 1
        for i in range(0, plusIndex):
            # closing bracket can be placed from index + 1 to end of the               # expression
            for j in range(plusIndex + 1, len(expression)) :
                # initially start with an empty string
                expr = ''
                # iterate through the original expression
                for k in range(len(expression)):
                    # if k is equal to i which is where we can place the opening bracket, we add the opening bracket
                    if k == i :
                        expr += '('
                    # add the actual character from input expression    
                    expr += expression[k]
                    # add the closing bracket
                    if k == j : 
                        expr += ')'
                
                # add the constructed expr to expressions
                expressions.append(expr)
        print(expressions)
        
        # get the values of a, b, c, d
        # a * (b + c) * d
        def getValues(exp):
            current = ''
            a, b, c, d = 1, 1, 1, 1
            for e in exp:
                # if e is opening bracket
                if e == '(':
                    if current != '':
                        a = current 
                        current = ''
                # if e is +        
                elif e == '+':
                    b = current
                    current = ''
                    
                # if e is )
                elif e == ')':
                    c = current
                    current = ''
                
                else:
                    current  += e
               
            if current != '':
                d = current
                
            return (a, b, c, d)    
        
        def getResult(a, b, c, d):
            return int(a) * (int(b) + int(c)) * int(d) 
        
        result = float('inf')
        output = ''
        for expr in expressions:
                
            (a, b, c, d) = getValues(expr)
            currentResult = getResult(a, b, c, d)
            if currentResult < result:
                output = expr
                result = currentResult
            
        return output
