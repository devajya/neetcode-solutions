class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = self.wordsToLines(words, maxWidth)
        justifiedLines = self.justifiedLines(lines, maxWidth)
        return justifiedLines

    def wordsToLines(self, words: List[str], maxWidth: int) -> List[List[str]]:
        total_line_length = 0
        line = []
        lines = []
        for word in words:
            if total_line_length+len(word) > maxWidth:
                lines.append(line)
                line = []
                total_line_length = 0

            line.append(word)
            total_line_length += len(word) + 1
        
        if line:
            lines.append(line)
        
        return lines
    
    def justifiedLines(self, lines: List[List[str]], maxWidth: int) -> List[List[str]]:
        justifiedLines = []
        for i, line in enumerate(lines):
            isLastLine = i==len(lines)-1
            justifiedLines.append(self.justifyLine(line, maxWidth, isLastLine))

        return justifiedLines

    def justifyLine(self, line: List[str], maxWidth: int, isLastLine: bool) -> str:
        justifiedLine = []

        if isLastLine or len(line)==1:
            justifiedLine = self.leftJustify(line, maxWidth)
        else:
            spaces = self.calculateSpaces(line, maxWidth)
            for pair in zip(line, spaces):
                justifiedLine.extend(pair)

            if len(line) > len(spaces):
                justifiedLine.append(line[-1])
        
        return "".join(justifiedLine)


    def calculateSpaces(self, line, maxWidth):
        gaps = len(line) - 1
        total_spaces = maxWidth - sum(len(w) for w in line)
        base, extra = divmod(total_spaces, gaps)   # gaps > 0 here
        return [" " * (base + (1 if i < extra else 0)) for i in range(gaps)]

    def leftJustify(self, line, maxWidth):
        s = " ".join(line)
        return s + " " * (maxWidth - len(s))
    