class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:

        i = 0
        while i < len(arr):
            flag = 0
            j = i+1
            while j < len(arr):
                print(i, j)
                if(arr[i] == arr[j]):
                    flag = 1
                    print(j)
                    arr.pop(j)
                    j -= 1
                j += 1
            if(flag == 1):
                arr.pop(i)
                i -= 1
            i += 1
            print("Value :", arr)
        
        if (len(arr) < k):
            return ""
        else:
            return arr[k-1]
        
solution = Solution()
arr = ["b","a","c","a"]
k = 2
result = solution.kthDistinct(arr, k)
print(result)