class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 保证 nums1 是较短的数组，二分在短数组上做
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total_left = (m + n + 1) // 2  # 左半部分元素个数

        # 二分查找 partition_i: nums1 中左半部分的元素个数
        lo, hi = 0, m

        while lo <= hi:
            i = (lo + hi) // 2        # nums1 的分割点
            j = total_left - i        # nums2 的分割点

            # nums1[i-1] <= nums2[j] ?
            # nums2[j-1] <= nums1[i] ?
            if i < m and nums2[j - 1] > nums1[i]:
                # nums2 左半最大值太大 → i 需要右移
                lo = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                # nums1 左半最大值太大 → i 需要左移
                hi = i - 1
            else:
                # 找到合法分割，计算 median
                # 左半最大值
                if i == 0:
                    left_max = nums2[j - 1]
                elif j == 0:
                    left_max = nums1[i - 1]
                else:
                    left_max = max(nums1[i - 1], nums2[j - 1])

                # 奇数总长度 → 中位数就是左半最大值
                if (m + n) % 2 == 1:
                    return float(left_max)

                # 偶数总长度 → 还需要右半最小值
                if i == m:
                    right_min = nums2[j]
                elif j == n:
                    right_min = nums1[i]
                else:
                    right_min = min(nums1[i], nums2[j])

                return (left_max + right_min) / 2.0


# ============================================================
# 测试
# ============================================================
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        # (nums1, nums2, expected)
        ([1, 2], [3], 2.0),
        ([1, 3], [2, 4], 2.5),
        ([1, 3], [2], 2.0),
        ([], [1], 1.0),
        ([], [2, 3], 2.5),
        ([1, 2], [1, 2], 1.5),
        ([1], [1], 1.0),
        ([1, 2, 3], [4, 5, 6], 3.5),
        ([4, 5, 6], [1, 2, 3], 3.5),
        ([1, 3, 5, 7], [2, 4, 6, 8], 4.5),
        ([3], [-2, -1], -1.0),
        ([1, 2], [-1, 3], 1.5),
    ]

    all_pass = True
    for nums1, nums2, expected in test_cases:
        result = sol.findMedianSortedArrays(nums1[:], nums2[:])
        ok = abs(result - expected) < 1e-9
        if not ok:
            all_pass = False
        status = "OK" if ok else "FAIL"
        print(f"nums1={nums1}, nums2={nums2} => {result} (expected {expected}) [{status}]")

    print(f"\n{'All passed!' if all_pass else 'Some tests FAILED!'}")