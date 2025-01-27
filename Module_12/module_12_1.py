# -*- coding: utf-8 -*-
# Домашнее задание по теме "Простые Юнит-Тесты"

import unittest
import runner

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        r = runner.Runner("Runner")
        for _ in range(10):
            r.walk()
        self.assertEqual(r.distance, 50)

    def test_run(self):
        r = runner.Runner("Runner")
        for _ in range(10):
            r.run()
        self.assertEqual(r.distance, 100)

    def test_challenge(self):
        r1 = runner.Runner("Runner 1")
        r2 = runner.Runner("Runner 2")
        for _ in range(10):
            r1.run()
            r2.walk()
        self.assertNotEqual(r1.distance, r2.distance)


if __name__ == '__main__':
    unittest.main()
