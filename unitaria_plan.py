import unittest

class TestLeerPlan(unittest.TestCase):

    def test_plan_valido(self):
        for plan in ["A", "B", "C"]:
            self.assertIn(plan, ["A", "B", "C"])

    def test_plan_invalido(self):
        self.assertNotIn("D", ["A", "B", "C"])
        self.assertNotIn("Z", ["A", "B", "C"])
        self.assertNotIn("1", ["A", "B", "C"])

if __name__ == "__main__":
    unittest.main()
