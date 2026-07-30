class FreqStack:

    def __init__(self):
        self.freq_map = defaultdict(list)
        self.in_stack_count = defaultdict(int)
        self.max_freq = 0

    def push(self, val: int) -> None:
        freq = self.in_stack_count[val] + 1
        self.in_stack_count[val] = freq
        self.freq_map[freq].append(val)
        self.max_freq = max(freq, self.max_freq)
        return


    def pop(self) -> int:
        ans = self.freq_map[self.max_freq].pop()
        if len(self.freq_map[self.max_freq]) == 0:
            self.max_freq -= 1
        self.in_stack_count[ans] -= 1
        return ans
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()