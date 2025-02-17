from collections import Counter

class Solution:
    def equalFrequency(self, word: str) -> bool:
        freq = Counter(word)
        freq_of_freq = Counter(freq.values())

        if len(freq_of_freq) == 2:
            (freq1, count1), (freq2, count2) = freq_of_freq.items()
            return (count1 == 1 and (freq1 - 1 == freq2 or freq1 - 1 == 0)) or \
                   (count2 == 1 and (freq2 - 1 == freq1 or freq2 - 1 == 0))

        if len(freq_of_freq) == 1:
            (freq, count) = freq_of_freq.popitem()
            return freq == 1 or count == 1

        return False
