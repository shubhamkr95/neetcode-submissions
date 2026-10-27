class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left  = [1] * n #[1,1,1,1]
        right = [1] * n #[1,1,1,1]
   
        for i in range(1, n):
        # n = 4
        # range start from 1 to 3 one less than n
        # left[1] = left[1-1] * nums[1-1]   left[1] = [1,1,1,1]
        # left[2] = left[2-1] * nums[2-1]   left[2] = [1,1,2,1]
        # left[3] = left[3-1] * nums[3-1]   left[3] = [1,1,2,8]
            left[i] = left[i-1] * nums[i-1] 

        # range start from 4-2 =2,
        # -1 up to 0 index
        # -1 decrease by -1
        # right[2] = right[2+1] * nums[2+1] = right[2] = [1,1,6,1]
        # right[1] = right[1+1] * nums[1+1] = right[1] = [1,24,6,1]
        # right[0] = right[0+1] * nums[0+1] = right[0] = [48,24,6,1]   
        for i in range(n-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]

        # left = [1,1,2,8]
        # right = [48,24,6,1]
        # left[0] * right[0] = [48,0,0,0]
        # left[1] * right[1] = [48,24,0,0]
        # left[2] * right[2] = [48,24,12,0]
        # left[3] * right[3] = [48,24,12,8]
        return [left[i] * right[i] for i in range(n)]