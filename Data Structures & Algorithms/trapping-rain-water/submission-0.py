class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        from_left = [0] * n
        from_right = [0] * n
        total_trapped_water = 0

        from_left[0] = height[0]
        from_right[n-1] = height[n - 1]

        for i in range(1, n):
            from_left[i] = max(from_left[i-1], height[i])

        for i in range(n - 2, -1, -1):
            from_right[i] = max(from_right[i + 1], height[i])
        
        for i in range(len(height)):
            val = min(from_left[i], from_right[i]) - height[i]
            total_trapped_water += val
            # print(val, from_left[i], from_right[i])
        return total_trapped_water