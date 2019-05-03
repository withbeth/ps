# Add, edit, or remove tests in this file.
# Treat it as your playground!

from solution import Solution
import unittest


class Testsolution(unittest.TestCase):

    def test_one_path_exists_1_return_true(self):
        testBoard =[
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
        ]
        testWord = "ABCCED"
        expected = True
        self.assertEqual(Solution().exist(testBoard, testWord), expected)

    def test_one_path_exists_2_return_true(self):
        testBoard =[
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
        ]
        testWord = "SEE"
        expected = True
        self.assertEqual(Solution().exist(testBoard, testWord), expected)

    def test_multiple_paths_exist_return_true_1(self):
        testBoard = [
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'E', 'S'],
            ['A', 'D', 'E', 'E']
        ]
        testWord = "ABCESEEEFS"
        expected = True
        self.assertEqual(Solution().exist(testBoard, testWord), expected)

    def test_multiple_paths_exist_return_true_2(self):
        testBoard = [
            ["C", "A", "A"],
            ["A", "A", "A"],
            ["B", "C", "D"]
        ]
        testWord = "AAB"
        expected = True
        self.assertEqual(Solution().exist(testBoard, testWord), expected)

    def test_path_not_exists_return_false(self):
        testBoard =[
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
        ]
        testWord = "ABCB"
        expected = False
        self.assertEqual(Solution().exist(testBoard, testWord), expected)


if __name__ == "__main__":
    unittest.main()
