class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapp = {}
        res = []

        
        for i, no in enumerate(nums):
            if no in mapp:  
                mapp[no] += 1
            else:
                mapp[no] = 1 

        sorted_mapp = dict(sorted(mapp.items(), key=lambda item: item[1], reverse=True))


        for key in sorted_mapp:
            if sorted_mapp[key] >= 1 and k != 0:
                res.append(key)
                k = k - 1

        return res