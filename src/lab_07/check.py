import random
from src.lab_07.sorting import bubble_sort, insertion_sort, selection_sort
from src.lab_07.search import (
    linear_search,
    binary_search,
    two_sum_brute,
    two_sum_fast
)
 
 
def check_sorting(fn, trials=100) -> None:
    """Проверяет сортировку на случайных списках"""
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        original = list(nums)
        result = fn(nums)
        assert result == sorted(nums), f"{fn.__name__} ошиблась на {nums}: {result}"
        assert nums == original, f"{fn.__name__} изменила исходный список"
 
def check_search() -> None:
    for _ in range(100):
        n = random.randint(0, 50)
        nums = [random.randint(-100,100) for _ in range(n)]
        sorted_nums = sorted(nums)
        original = list(nums)
        
        targets = [101]
        if nums:
            targets.append(nums[0])
            targets.append(nums[-1])
            targets.append(random.choice(nums))
        
        for x in targets:
            try:
                expexted = nums.index(x)
            except ValueError:
                expected = -1
            
            result = linear_search(nums, x)
            assert result == expected, f"Ошибка линейного поиска: {nums}, {x}"

            result = binary_search(sorted_nums, x)
            if x in sorted_nums:
                assert 0 <= result <= len(nums)
                assert nums[result] == x
            else:
                result = -1

def check_two_sum(trials=100) -> None:
    for _ in range(trials):
        n = random.randint(2,30)
        nums = [random.randint(-50,50) for _ in range(n)]

        target = random.randint(-200, 200)
        expected = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j]) == target:
                    expected.append((i, j))

        result_brute = two_sum_brute(nums, target)
        result_fast = two_sum_fast(nums, target)
        if expected:
            assert result_brute in expected, f"Поиск индексов двумя циклами элементов, образующих сумму не выполнен верно: {nums}, {target}"
            assert result_fast in expected, f"Поиск индексов словарем элементов, образующих сумму не выполнен верно: {nums}, {target}"
        else:
            assert result_brute  is None
            assert result_fast is None


    
if __name__ == "__main__":
    random.seed(42)
    for fn in (bubble_sort, insertion_sort, selection_sort):
        check_sorting(fn)
    check_search()
    check_two_sum()
    print("OK: все проверки пройдены")