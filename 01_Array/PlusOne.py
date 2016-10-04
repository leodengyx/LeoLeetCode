"""
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.
"""
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        self.plusOneOnPosition(digits, len(digits)-1)
        return digits

    def plusOneOnPosition(self, digits, pos):
        if digits[pos] != 9:
            digits[pos] += 1
            return
        else:
            digits[pos] = 0
            if pos == 0:
                digits.insert(0, 1)
                return
            else:
                self.plusOneOnPosition(digits, pos-1)

if __name__ == "__main__":
    solution = Solution()
    print(solution.plusOne([9,9,9]))





