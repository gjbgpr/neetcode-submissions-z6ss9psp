class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        line, length = [], 0
        i = 0

        while i < len(words):
            if length + len(words[i]) + len(line) <= maxWidth:
                line.append(words[i])
                length += len(words[i])
                i += 1
            else:
                extra_space = maxWidth - length
                ramainder = extra_space % max(1, (len(line) - 1))
                spaces = extra_space // max(1, (len(line) - 1))
                for j in range(max(1, len(line) - 1)):
                    line[j] += " " * spaces
                    if ramainder:
                        line[j] += " "
                        ramainder -= 1
                result.append("".join(line))
                line, length = [], 0
        
        last_line = ' '.join(line)
        trail_space = maxWidth - len(last_line)
        result.append(last_line + ' ' * trail_space)
        return result