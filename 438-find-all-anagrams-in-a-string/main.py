# Refer https://leetcode.com/problems/find-all-anagrams-in-a-string/
import os
from solution import Solution
import time

test_dir = "test_case"

if __name__ == '__main__':
    solution = Solution()
    for test_file in os.listdir(test_dir):
        start_time = time.time()
        file = open(os.path.join(test_dir, test_file))
        #file = open("test_case/test_case4")
        end_time = time.time()
        print solution.findAnagrams(file.readline(), file.readline())
        print time.strftime("%H:%M:%S", time.gmtime(end_time - start_time))
