def solution(nums):
    if not nums:
        return []

    if len(nums) == 1:
        return [str(nums[0])]

    result = []

    working: Tuple[int, int] = (nums[0], nums[0])
    for n in nums[1:]:
        start, end = working
        if n == end + 1:
            working = (start, n)
        else:
            result.append(
                f"{working[0]}->{working[1]}"
                if working[0] < working[1]
                else str(working[0])
            )
            working = (n, n)

    if working:
        result.append(
            f"{working[0]}->{working[1]}"
            if working[0] < working[1]
            else str(working[0])
        )

    return result
