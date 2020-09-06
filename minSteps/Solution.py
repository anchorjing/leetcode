# 最初在一个记事本上只有一个字符 'A'。你每次可以对这个记事本进行两种操作：
#
# Copy All (复制全部) : 你可以复制这个记事本中的所有字符(部分的复制是不允许的)。
# Paste (粘贴) : 你可以粘贴你上一次复制的字符。
# 给定一个数字 n 。你需要使用最少的操作次数，在记事本中打印出恰好 n 个 'A'。输出能够打印出 n 个 'A' 的最少操作次数。
#
# 示例 1:
#
# 输入: 3
# 输出: 3
# 解释:
# 最初, 我们只有一个字符 'A'。
# 第 1 步, 我们使用 Copy All 操作。
# 第 2 步, 我们使用 Paste 操作来获得 'AA'。
# 第 3 步, 我们使用 Paste 操作来获得 'AAA'。
# 说明:
#
# n 的取值范围是 [1, 1000]

class Solution():
    def minSteps(self, n):
        if n == 1:
            return 0
        if Solution().is_prime(n):
            return n
        times = 0
        while not Solution.is_prime(n):
            k = n - 1
            while n % k != 0:
                k -= 1
            times += n / k
            n = k
        return int(n + times)

    @staticmethod
    def is_prime(n):
        if n > 2:
            if n % 2 == 0:
                return False
            for i in range(2, int(n / 2) + 1):
                if n % i == 0:
                    return False
        return True


if __name__ == "__main__":
    while True:
        n = int(input("input n: "))
        print(Solution().minSteps(n))