class Solution:
    def isValid(self, s: str) -> bool:
        if (len(s) %2 != 0):
            return False
        stack = []
        # list_s = []
        # for string in s:
        #     list_s.append(string)

        # braket = {
        #     "(": ")",
        #     "{": "}",
        #     "[": "]"
        # }
        # for i in range(len(list_s)//2):
        #     print("In first while-----------", list_s[0])
        #     j = len(list_s) - 1
        #     while 0 < j :
        #         print("In second while")
        #         if (braket[list_s[0]] == list_s[j]):
        #             print(braket[list_s[0]], list_s[j], list_s[0])
        #             list_s.pop(j)
        #             list_s.pop(0)                    
        #             break
        #         j -= 1
        # if (len(list_s) == 0):
        #     print(list_s)
        #     return True
        # else:
        #     print(list_s)
        #     return False
        for val in s:
            if (val == "("):
                stack.append(")")
            elif (val == "{"):
                stack.append("}")
            elif (val == "["):
                stack.append("]")
            elif ((len(stack) == 0) or val == stack[len(stack)-1]):
                if (len(stack) == 0):
                    return False
                stack.pop()
            elif (val != stack[len(stack)-1]):
                return False
            
            
        return not stack
            



        
solution = Solution()
s = "([}}])"
result = solution.isValid(s) #"(){}[][({})]"
print(result)