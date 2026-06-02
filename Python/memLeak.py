class Solution:
    def memLeak(self, memory1: int, memory2: int) -> list[int]:
        
        i = 1
        while memory1 >= i or memory2 >= i:

            if memory1 >= memory2:
                memory1 -= i
            else:
                memory2 -= i
                    
            print(f"time: {i}, i: {i}, memory1: {memory1}, memory2: {memory2}")
            i += 1
            
        return [i, memory1, memory2]
    

solution = Solution()
memory1 = 8
memory2 = 11
result = solution.memLeak(memory1, memory2)
print(result)