class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Sort the colors in-place: 0s, 1s, and 2s.
        """
        # Initialize three pointers: low, mid, high
        low = 0
        mid = 0
        high = len(nums) - 1
        
        # Traverse the array
        while mid <= high:
            if nums[mid] == 0:
                # If the current element is 0, swap it with the element at the low pointer
                nums[mid], nums[low] = nums[low], nums[mid]
                low += 1
                mid += 1
            elif nums[mid] == 2:
                # If the current element is 2, swap it with the element at the high pointer
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
            else:
                # If the current element is 1, move to the next element
                mid += 1