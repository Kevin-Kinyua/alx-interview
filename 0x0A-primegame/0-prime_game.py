def isWinner(x, nums):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_primes(n):
        primes = []
        for i in range(2, n + 1):
            if is_prime(i):
                primes.append(i)
        return primes

    def game_winner(n):
        primes = get_primes(n)
        memo = {}

        def can_win(num):
            if num in memo:
                return memo[num]
            for prime in primes:
                if prime > num:
                    break
                if not can_win(num - prime):
                    memo[num] = True
                    return True
            memo[num] = False
            return False

        return "Maria" if can_win(n) else "Ben"

    results = [game_winner(n) for n in nums]

    maria_wins = results.count("Maria")
    ben_wins = results.count("Ben")

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None

# Example usage
x = 3
nums = [4, 5, 1]
result = isWinner(x, nums)
print(result)
