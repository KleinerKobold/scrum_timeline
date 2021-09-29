import unittest
from util import getBackground

class TestGetBackground(unittest.TestCase):

    def test_intervention(self):
        self.assertEqual(getBackground('Intervention'), 'blue')

    def test_inpediment(self):
        self.assertEqual(getBackground('Impediment'), 'orange')

if __name__ == '__main__':
    unittest.main()