from typing import List, Tuple


def binary_search_upper_bound(arr: List[float], target: float) -> Tuple[int, float]:
    left = 0
    right = len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = (left + right) // 2

        if arr[mid] >= target:
            upper_bound = arr[mid]
            right = mid - 1
        else:
            left = mid + 1

    return iterations, upper_bound


def run_tests():
    test_cases = [
        ([0.2, 1.1, 1.9, 2.5, 3.3, 4.8], 2.0),
        ([0.5, 1.2, 1.7, 2.4, 3.0, 3.6, 4.1], 3.5),
        ([0.1, 0.3, 0.8, 1.0, 1.5], 0.05),
        ([1.0, 2.0, 3.0, 4.0, 5.0], 5.5),  # target larger than all elements
    ]

    for i, (arr, target) in enumerate(test_cases, 1):
        iterations, upper_bound = binary_search_upper_bound(arr, target)
        print(f"Test {i} -> Target: {target}, Iterations: {iterations}, Upper bound: {upper_bound}")
        if upper_bound is not None:
            assert upper_bound >= target and upper_bound in arr
        else:
            print(f"Test {i} -> Target {target} exceeds all array elements.")


def main():
    run_tests()


if __name__ == "__main__":
    main()
