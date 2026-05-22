class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        inter_pattern_to_words = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(0, len(word)):
                pattern = word[0:i] + "*" +word[i+1:]
                inter_pattern_to_words[pattern].append(word)

        visited = set([beginWord])
        q = deque([beginWord])
        distance = 1
        while q:
            level_count = len(q)
            for i in range(level_count):
                word = q.popleft()
                if word==endWord:
                    return distance
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for pattern_matched_word in inter_pattern_to_words[pattern]:
                        if pattern_matched_word not in visited:
                            q.append(pattern_matched_word)
                            visited.add(pattern_matched_word)
            distance += 1
        
        return 0

