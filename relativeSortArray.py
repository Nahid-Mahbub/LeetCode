class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        answer = []
        # freq = {}
        # for num in arr1:
        #     if(num in freq):
        #         freq[num] += 1
        #     else:
        #         freq[num] = 1
        # print(freq)
        # for num in arr2:
        #     for i in range(freq[num]):
        #         answer.append(num)
        #         arr1.remove(num)
        # for num in arr1:
        #     answer.append(num)
        # return answer

        for arr2Num in arr2:
            for i in range(len(arr1)-1, -1, -1):
                if(arr1[i] == arr2Num):
                    answer.append(arr2Num)
                    arr1.pop(i)
        arr1.sort()
        return answer + arr1
            
        
        
solution = Solution()
arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
result = solution.relativeSortArray(arr1, arr2)
print(result)