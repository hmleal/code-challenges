import unittest

from matriz import reverse_row, reverse_col, sum_result, change


class TestMatriz(unittest.TestCase):
    def test_reverse_row(self):
        matriz = [[1, 2, 3], [3, 2, 1]]

        self.assertEqual(reverse_row(matriz, 0), [[3, 2, 1], [3, 2, 1]])

    def test_reverse_col(self):
        matriz = [[1, 2, 3], [3, 2, 1]]

        self.assertEqual(reverse_col(matriz, 0), [[3, 2, 3], [1, 2, 1]])

    def test_sum_result(self):
        matriz = [[1, 2, 3], [3, 2, 1]]

        self.assertEqual(sum_result(matriz), 8)

    def test_case(self):
        matriz = [
            [112, 42, 83, 119],
            [56, 125, 56, 49],
            [15, 78, 101, 43],
            [62, 98, 114, 108]
        ]

        self.assertEqual(change(matriz), 414)

if __name__ == '__main__':
    unittest.main()
