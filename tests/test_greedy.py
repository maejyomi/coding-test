import unittest

from src.greedy import coin_split, law_of_large_numbers,count_with_three_in_time, k_knight, find_prime


class TestGreedy(unittest.TestCase):
    def test_coin_split(self):
        self.assertEqual(coin_split(total_value=1260), 6)
        self.assertEqual(coin_split(total_value=660), 4)

## 큰 수의 법칙 
### 1. 문제를 이해(입력과 출력의 상관관계)
### 2. 입/출력의 정답을 확인할 수 있는 방법
    def test_law_of_large_numbers(self):
        self.assertEqual(law_of_large_numbers((5,8,3),[2,4,5,4,6]), 46)
        self.assertEqual(law_of_large_numbers((5,3,3),[2,4,5,4,6]), 18)

    def test_count_with_three_in_time(self):
        self.assertEqual(count_with_three_in_time(5),11475)

    def test_k_night(self):
        self.assertEqual(k_knight("a1"),2)

    def test_find_prims(self): # 소수 찾기 프로그래머스 문제
        self.assertEqual(find_prime("17"),3)
        self.assertEqual(find_prime("011"),2)