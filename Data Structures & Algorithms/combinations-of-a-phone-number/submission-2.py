class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_to_letters = {
            '2': ["a", "b", "c"], 
            '3': ["d", "e", "f"], 
            '4': ["g", "h", "i"], 
            '5': ["j", "k", "l"], 
            '6': ["m", "n", "o"], 
            '7': ["p", "q", "r", "s"], 
            '8': ["t", "u", "v"], 
            '9': ["w", "x", "y", "z"],    
        }
        if not digits:
            return []

        ans = [""]
        for digit in digits:
            temp = []
            for curr_str in ans:
                for char in num_to_letters[digit]:
                    temp.append(curr_str+char)
            ans = temp
        return ans