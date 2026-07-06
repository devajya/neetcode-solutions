class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # start at 0
        # see a new character put in the substring till its last index
        # for each of the elements within decrmeent count
        # is all of their counts hit 0 add to substring move up starting index
        # otherwise look at the elements that have not hit 0, get the maximum index in the string from them all and add 
        # repeat

        subs = []
        last_index_map = defaultdict(int)
        for i, c in enumerate(s):
            last_index_map[c] = i
        
        i=0
        while i<len(s):
            j=i
            max_index_found = last_index_map[s[j]]

            sub = ""
            while j <= max_index_found:
                max_index_found = max(max_index_found, last_index_map[s[j]])
                sub+=s[j]
                j+=1
            
            subs.append(sub)
            i=j


        return [len(t) for t in subs]
            