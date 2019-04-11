class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # Set up seq
        result = []
        words_seq = []
        sentence_seq = []
        for c in p.strip():
            words_seq.append(c)
        for c in s.strip():
            sentence_seq.append(c)
        words_checked = [False] * len(words_seq)

        # Verify pre-condition
        if len(sentence_seq) - len(words_seq) <= 0:
            return result

        for idx in range(0, len(sentence_seq) - len(words_seq) + 1):
            # Check whether following window seq satisfies Anagram condition
            window = sentence_seq[idx: idx + len(words_seq)]
            for w in window:
                if w in words_seq :
                    i = words_seq.index(w)
                    if i and words_checked[i] is False:
                        words_checked[i] = True
                        if len(words_seq) == sum(words_checked):
                            result.append(idx)
        return result

if __name__ == '__main__':
    solution = Solution()
    file = open("test_case3")
    print solution.findAnagrams(file.readline(), file.readline())









