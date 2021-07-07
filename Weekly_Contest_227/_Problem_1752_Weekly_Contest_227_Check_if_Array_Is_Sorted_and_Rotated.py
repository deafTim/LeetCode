from typing import List
class Solution:
	def check(self, nums: List[int]) -> bool:
		counter = 0
		for i in range(len(nums)-1):
			if nums[i]>nums[i+1]:
				counter += 1
			if counter > 1:
				break
		return counter==0 or (counter==1 and nums[0]>=nums[-1])
    
