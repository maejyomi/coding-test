import unittest
from src.bfs.word_conversion import word_conversion
from src.bfs.short import shorttest

class TestBFS(unittest.TestCase):
    def test_word_conversion(self):
        self.assertEqual(word_conversion("hit", "cog", ["hot", "dot","dog","lot","log","cog"]), 4)
    
    def test_short(self):
        self.assertEqual(shorttest(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]), 3)
