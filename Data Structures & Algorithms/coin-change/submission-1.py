class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        min_coins = [float('inf')]

        visited =set()
        def backtrack(remaining, count):
            # Base case: exact amount reached
            if remaining == 0:
                min_coins[0] = min(min_coins[0], count)
                return

            # Base case: overreached or already worse than current best
            if remaining < 0 or count >= min_coins[0]:
                return
            if (remaining, count) in visited:
                return
            visited.add((remaining, count))
            # Try each coin
            for coin in coins:
                backtrack(remaining - coin, count + 1)

        backtrack(amount, 0)

        return min_coins[0] if min_coins[0] != float('inf') else -1



        