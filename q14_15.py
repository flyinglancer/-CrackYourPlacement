class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        triplets :Set[tuple] = set()

        n  = len(nums)

        for i in range (n-2):
            if i >0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1,n-1

            while left<right:
                curr = nums[i] + nums[left] + nums[right]
                if curr < 0:
                    left += 1
                elif curr > 0:
                    right -= 1
                else:
                    triplets.add((nums[i],nums[left],nums[right]))
                    left += 1
                    right -= 1
                    while left <right and nums[left] == nums[left-1]:
                        left += 1
                    while left <right  and nums[right] == nums[right+1]:
                        right -= 1
        return [list(triplet) for triplet in triplets]
