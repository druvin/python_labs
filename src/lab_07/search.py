def linear_search(nums, x) -> int:
    """Возвращает индекс первого вхождения x или -1."""
    for i in range(len(nums)):
        if x == nums[i]:
            return i
    return -1
 
 
def binary_search(sorted_nums, x) -> int:
    """Ищет x  в отсортированном списке.
    Для неотсортированного списка результат не определен."""
    lo = 0
    hi = len(sorted_nums) - 1
    while lo <= hi:
        mid = (lo+hi) // 2

        if sorted_nums[mid] == x:
            print(mid)
        elif sorted_nums[mid]< x:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
 
 
def two_sum_brute(nums, target) -> tuple[int, int] | None:
    """Ищет пару индексов таких чисел, сумма которых равна target."""
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if (nums[i] + nums[j]) == target:
                return (i, j)
    return None
 
 
def two_sum_fast(nums, target) -> tuple[int, int] | None:
    """То же, что two_sum_brute, но за один проход со словарём."""
    seen = {}
    for i in range(len(nums)):
        needed = target - nums[i]
        if needed in seen:
            return (seen[needed], i)
        seen[nums[i]] = i
    return None
