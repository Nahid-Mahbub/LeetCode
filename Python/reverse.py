class Solution:
    def reverse(self, x: int) -> int:
        
        num_list = [str(num) for num in str(x)]
        length = len(num_list)

        if(length == 1):
            return x
        if(num_list[length - 1] == "0" or num_list[0] == "-"):
            if(num_list[length - 1] == "0"):
                num_list.pop()
            if(num_list[0] == "-"):
                num_list.pop(0)
                num_list.append("-")

        value = int("".join(num_list[::-1]))
        if(-2147483648 < value < 2147483647):
             return value
        else:
            return 0
    
solution = Solution()
x = 1234
result = solution.reverse(x)
print(result)