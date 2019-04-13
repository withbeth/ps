class Solution(object):

    def quick_sorted(self, arr):
        if len(arr) > 1:
            pivot = arr[len(arr) - 1]
            left, mid, right = [], [], []
            for i in range(len(arr) - 1):
                if arr[i] < pivot:
                    left.append(arr[i])
                elif arr[i] > pivot:
                    right.append(arr[i])
                else:
                    mid.append(arr[i])
            mid.append(pivot)
            return self.quick_sorted(left) + mid + self.quick_sorted(right)
        else:
            return arr

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

        # Verify pre-condition
        if len(sentence_seq) - len(words_seq) <= 0:
            return result

        for idx in range(0, len(sentence_seq) - len(words_seq) + 1):
            # Check whether following sub seq satisfies Anagram condition
            sub_seq = sentence_seq[idx: idx + len(words_seq)]
            if self.quick_sorted(sub_seq) == self.quick_sorted(words_seq) :
                result.append(idx)

        return result









