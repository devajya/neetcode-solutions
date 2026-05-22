class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        map_pattern_to_word = defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                map_pattern_to_word[pattern].append(word)
        
        q = deque([beginWord])
        visited = set([beginWord])
        distance = 1

        while q:
            level_count = len(q)
            for i in range(level_count):
                word = q.popleft()
                if word == endWord:
                    return distance

                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for matched_word in map_pattern_to_word[pattern]:
                        if not matched_word in visited:
                            q.append(matched_word)
                            visited.add(matched_word)

            distance += 1

        return 0
