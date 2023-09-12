class Solution:
    def minDeletions(self, s: str) -> int:
        counting_dict = {}
        for a in s:
            if a in counting_dict:
                counting_dict[a] += 1
            else:
                counting_dict[a] = 1
        
        freq_set = set()
        count = 0
        for key in counting_dict:
            freq = counting_dict[key]

            if freq in freq_set:
                while freq in freq_set and freq != 0:
                    freq -= 1
                    count += 1
                
                if freq != 0:
                    freq_set.add(freq)
            else:
                freq_set.add(freq)
        
        return count