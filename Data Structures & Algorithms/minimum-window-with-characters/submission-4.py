class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target_counts = [0]*52
        seen_counts = [0]*52

        for c in t:
            target_counts[self.charIndex(c)] += 1
    
        chars_needed = sum(1 for count in target_counts if count > 0)
        chars_met = 0

        start = -1
        end = -1
        min_len = float("inf")

        i = 0
        for j in range(0, len(s)):
            char_end = s[j]
            end_counts_idx = self.charIndex(char_end)

            seen_counts[end_counts_idx] += 1

            e_needed = target_counts[end_counts_idx] > 0
            e_reached = seen_counts[end_counts_idx] == target_counts[end_counts_idx]

            if e_needed and e_reached:
                chars_met += 1
            
            while chars_met == chars_needed:
                char_start = s[i]
                start_counts_idx = self.charIndex(char_start)
                
                # update ans
                if j-i+1 < min_len:
                    start = i
                    end = j
                    min_len = j-i+1
                
                # shrink substr
                seen_counts[start_counts_idx] -= 1
                s_needed = target_counts[start_counts_idx] > 0
                s_unreached = seen_counts[start_counts_idx] < target_counts[start_counts_idx]
                if s_needed and s_unreached:
                    chars_met -= 1
                
                i+=1
            
        return s[start:end+1] if start != -1 else ""

    def charIndex(self, c:str) -> int:
        if c.islower():
            return ord(c) - ord('a')
        return 26 + ord(c) - ord('A')