class Solution:
    def isHappy(self, n: int) -> bool:
        fast, slow = n, n
        def square_digits(num):
            count = 0
            for i in str(num):
                count += int(i)** 2 
            return count

        fast = square_digits(square_digits(fast))
        slow = square_digits(slow)

        while fast != slow:

            fast = square_digits(square_digits(fast))
            slow = square_digits(slow)

        return fast == 1