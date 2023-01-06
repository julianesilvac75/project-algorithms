def find_duplicate(nums=None):
    if (
        nums is None or
        type(nums) == str
    ):
        return False

    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] == nums [i + 1] and nums[1] > 0:
            return nums[i]

    return False
