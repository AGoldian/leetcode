words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16

class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        str_power = 0
        i = 0
        result = []
        prev = []

        while i < len(words):
            word = words[i]
            if str_power + len(word) > maxWidth:
                str_power = 0
                result.append(prev)
                prev = []

            prev.append(word)
            str_power += len(word)

            if len(prev) != 0:
                str_power += 1
            i += 1
        
        result.append(prev)
        print(result)
        result2 = []
        
        for row in result:
            if len(row) == 1:
                result2.append(row[0].ljust(maxWidth, ' '))
            else:
                char = sum(list(map(len, row)))
                space = maxWidth - char
                s = row[0]
                for word in row:
                    s += space // len

                    


        return result2
    
print(Solution().fullJustify(words, maxWidth))


            


