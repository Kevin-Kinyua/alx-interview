def makeChange(coins, total):
    # If total is 0 or less, return 0
    if total <= 0:
        return 0

    # Initialize an array to store the minimum number of coins for each total
    dp = [float('inf')] * (total + 1)

    # Base case: 0 coins needed to make change for 0
    dp[0] = 0

    # Iterate over all possible totals from 1 to the target total
    for t in range(1, total + 1):
        # Try each coin denomination
        for coin in coins:
            # Check if the coin can contribute to the current total
            if coin <= t:
                # Update the minimum number of coins needed for the current total
                dp[t] = min(dp[t], dp[t - coin] + 1)

    # If dp[total] is still the initial value, it means the total cannot be met
    return dp[total] if dp[total] != float('inf') else -1

# Example usage:
coins = [1, 2, 5]
total = 11
result = makeChange(coins, total)
print(result)  # Output: 3 (1 coin of 1, 1 coin of 5, 0 coins of 2)
