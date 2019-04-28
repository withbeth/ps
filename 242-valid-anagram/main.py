import os
from solution import Solution
test_dir = "test_case"

if __name__ == '__main__':
    for test_file in os.listdir(test_dir):
        solution = Solution()
        file = open(os.path.join(test_dir, test_file))
        print solution.isAnagram(file.readline(), file.readline())
