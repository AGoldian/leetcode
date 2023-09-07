from collections import Counter

s = 'vvvlov'


class Solution:
    def reorganizeString(self, s: str) -> str:
        hashmap = Counter(s)
        res = ''
        char1, char2 = hashmap.most_common(2)

        while hashmap[char1[0]] and hashmap[char2[0]] != 0:
                res += char1[0]
                res += char2[0]

                hashmap[char1[0]] -= 1
                hashmap[char2[0]] -= 1
                char1, char2 = hashmap.most_common(2)
                print(hashmap)

        print()
        print(hashmap)

        print(res)
        if len(res) != len(s):
            return ''
        
        return res
        

print(Solution().reorganizeString(s))

