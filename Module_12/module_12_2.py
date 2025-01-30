# -*- coding: utf-8 -*-
# Домашнее задание по теме "Методы Юнит-тестирования"

import unittest
from runner_and_tournament import Runner, Tournament


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Усэйн", 10)
        self.andrey = Runner("Андрей", 9)
        self.nik = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f"{value}")

    def test_usain_and_nik(self):
        tournament = Tournament(90, self.usain, self.nik)
        # tournament.start()
        self.all_results["usain_and_nik"] = tournament.start()
        self.assertTrue(self.all_results["usain_and_nik"][max(self.all_results["usain_and_nik"].keys())] == self.nik.name)

    def test_andrey_and_nik(self):
        tournament = Tournament(90, self.andrey, self.nik)
        # tournament.start()
        self.all_results["andrey_and_nik"] = tournament.start()
        self.assertTrue(self.all_results["andrey_and_nik"][max(self.all_results["andrey_and_nik"].keys())] == self.nik.name)

    def test_usain_andrey_and_nik(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nik)
        # tournament.start()
        self.all_results["usain_andrey_and_nik"] = tournament.start()
        self.assertTrue(self.all_results["usain_andrey_and_nik"][max(self.all_results["usain_andrey_and_nik"].keys())] == self.nik.name)


if __name__ == "__main__":
    unittest.main()

