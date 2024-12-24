class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = []
        max_swap = num
        while num != 0:
            nums.append(num % 10)
            num //= 10
        nums = nums[::-1]

        cur_max = 0
        cur_max_ind = 0
        cur_max_arr = [0 for i in range(len(nums))]
        cur_max_ind_arr = [0 for i in range(len(nums))]
        for i in range(len(nums) - 1, -1, -1):
            if cur_max < nums[i]:
                cur_max = nums[i]
                cur_max_ind = i
            cur_max_arr[i] = cur_max
            cur_max_ind_arr[i] = cur_max_ind

        for i in range(0, len(nums)):
            if nums[i] < cur_max_arr[i]:
                new_nums = nums[::]
                new_nums[i], new_nums[cur_max_ind_arr[i]] = cur_max_arr[i], new_nums[i]
                new_swap = int(''.join(map(str, new_nums)))
                if new_swap > max_swap:
                    max_swap = new_swap

        return max_swap
    
# Time Complexity: O(n)
# Space Complexity: O(n)