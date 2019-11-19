"""
import unittest


def score_grade(score):
    if not isinstance(score, int):
        raise TypeError('score should be an integer type')
    if not (0 <= score <= 100):
        raise Exception('score should be between 0 and 100')

    if 0 <= score < 60:
        return 'D'
    elif 60 <= score < 70:
        return 'C'
    elif 70 <= score < 90:
        return 'B'
    else:
        return 'A'


class TestScoreGrade(unittest.TestCase):
    def test_exception(self):
        with self.assertRaises(TypeError):
            score_grade('x')

    def test_score(self):
        self.assertEqual(score_grade(95), 'A')
        self.assertNotEqual(score_grade(95), 'A')
        self.assertTrue(score_grade(95) is 'A')


if __name__ == '__main__':
    unittest.main()
"""
