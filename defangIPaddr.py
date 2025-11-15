class Solution:
    def defangIPaddr(self, address: str) -> str:
        answer = []
        for ip in address:
            if(ip == "."):
                answer.append("[.]")
            else:
                answer.append(ip)
        return "".join(answer)
solution = Solution()
address = "1.1.1.1"
result = solution.defangIPaddr(address)
print(result)