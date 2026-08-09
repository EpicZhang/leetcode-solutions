# Time complexity: O(nlogn)
# Space complexity: O(n)
class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        min_sum = 0
        new_prices = sorted(prices, reverse = True)
        new_discounts = sorted(discounts, reverse = True)
        
        if len(new_prices) <= len(new_discounts):
            for i in range(len(new_prices)):
                min_sum += new_prices[i] * (100 - new_discounts[i]) / 100
        else:
            for i in range(len(new_discounts)):
                min_sum += new_prices[i] * (100 - new_discounts[i]) / 100
            for i in range(len(new_discounts), len(new_prices)):
                min_sum += new_prices[i]

        return min_sum



        