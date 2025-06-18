# 🔍 LeetCode Algorithm Solutions

## 🏷 项目简介
**一站式LeetCode题解库** | 每个问题提供：
- 🧠 我的原始解法（保留思考痕迹）
- ⚡ 优化解法（附学习来源）
- 📝 深度注释（复杂度分析 + 优化思路可视化）


## 📜 文件结构

```
bash
LeetCode/
├── 0001_TwoSum.py          # 格式：题号_题目.py
├── 0020_ValidParentheses.py
└── ...                     # 持续更新
```


## 📊刷题统计

![LeetCode Stats](https://leetcard.jacoblin.cool/pan-zhen-ye?theme=light&font=Shippori%20Antique%20B1&ext=activity&site=cn)


## 🧩 代码模板

```python
# 文件名：题号_题目.py (示例：0001_TwoSum.py)

class Solution:
    def mySolution(self, nums: List[int], target: int) -> List[int]:
        """
        📌 初始解法 | 暴力枚举
        💡 思路：双重循环检查所有组合
        ⏰ 时间复杂度：O(n²)
        🏠 空间复杂度：O(1)
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def optimalSolution(self, nums: List[int], target: int) -> List[int]:
        """
        📌 优化解法 | 哈希表
        💡 优化点：空间换时间，查询O(1)
        ⏰ 时间复杂度：O(n) 
        🏠 空间复杂度：O(n)
        🔗 参考：LeetCode官方题解
        """
        seen = {}
        for i, num in enumerate(nums):
            if target - num in seen:
                return [seen[target-num], i]
            seen[num] = i

if __name__ == "__main__":
    sol = Solution()
    print(sol.mySolution([3,2,4], 6))      # 输出：[1,2]
    print(sol.optimalSolution([3,3], 6))   # 输出：[0,1]
```
