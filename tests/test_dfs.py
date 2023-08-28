import unittest
from src.dfs.ice import ice

class TestDFS(unittest.TestCase):
    def test_ice(self):
        m = [[0,0,1,1,0],
            [0,0,0,1,1],
            [1,1,1,1,1],
            [0,0,0,0,0]]    
        self.assertEqual(ice(m), 3)