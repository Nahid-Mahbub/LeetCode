class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        counter = 0
        i = 2
        length = len(arr)
        if (length <= 3):
            if (length == 3):
                return sum(arr)*2
            else:
                return sum(arr)
        for _ in range(length//2): # lop for overall
            j = 0
            print(length//2)
            while((length - i) > j): # Loop for len - i
                for k in range(j, j+i+1): # loop for sum
                    # print("Printing length: ", j+i+1)
                    print(arr[k])
                    counter += arr[k]
                print()
                j += 1
            i += 2
        return counter + sum(arr)
solution = Solution()
arr = [1,4,2,5,3]
result = solution.sumOddLengthSubarrays(arr)
print(result)

    

