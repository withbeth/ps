class Solution(object):

    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # Set up seq
        result = []
        words_seq = [c for c in p.strip()]
        sentence_seq = [c for c in s.strip()]

        # Verify pre-conditions
        if len(sentence_seq) == 0 or len(words_seq) == 0:
            return result
        elif len(sentence_seq) - len(words_seq) <= 0:
            return result

        # Set up caches
        words_freq_cache = {}
        for c in p.strip():
            if c in words_freq_cache:
                words_freq_cache[c] += 1
            else:
                words_freq_cache[c] = 1

        window_freq_cache = {}
        for c in sentence_seq[:len(words_seq) - 1]:
            if c in window_freq_cache:
                window_freq_cache[c] += 1
            else:
                window_freq_cache[c] = 1

        # Iterate
        for idx in range(0, len(sentence_seq) - len(words_seq) + 1):

            window = sentence_seq[idx:idx + len(words_seq)]

            # Cache last index one
            if window_freq_cache.has_key(window[-1]):
                window_freq_cache[window[-1]] += 1
            else:
                window_freq_cache[window[-1]] = 1

            # Check anagram condition
            if words_freq_cache == window_freq_cache:
                result.append(idx)

            # Decrease first index count since window will be shifting RIGHT
            window_freq_cache[window[0]] -= 1
            if window_freq_cache[window[0]] == 0:
                del window_freq_cache[window[0]]

        return result

