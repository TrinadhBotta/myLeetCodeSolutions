class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def backtrack(index, path):
            # If the current combination is complete
            if index == len(digits):
                combinations.append("".join(path))
                return
            
            # Get letters for the current digit
            current_digit = digits[index]
            letters = digit_to_letters[current_digit]
            
            # Explore all possible letters for the current digit
            for letter in letters:
                path.append(letter)  # Choose the letter
                backtrack(index + 1, path)  # Move to the next digit
                path.pop()  # Un-choose the letter

        combinations = []
        backtrack(0, [])
        return combinations