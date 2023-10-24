class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        total_coins = 0
        num_triples = 0

        for i in range(1, len(piles), 2):
            total_coins += piles[i]
            num_triples += 1

            if num_triples == len(piles) // 3:
                break

        return total_coins