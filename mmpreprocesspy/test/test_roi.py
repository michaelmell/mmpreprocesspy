from unittest import TestCase


class TestRoi(TestCase):
    def test__init__for__equal_n_bounds__raises__ValueError(self):
        from mmpreprocesspy.roi import Roi
        with self.assertRaises(ValueError):
            Roi(1, 2, 3, 2)

    def test__init__for__invalid_n_bounds__raises__ValueError(self):
        from mmpreprocesspy.roi import Roi
        with self.assertRaises(ValueError):
            Roi(1, 4, 3, 2)

    def test__init__for__equal_m_bounds__raises__ValueError(self):
        from mmpreprocesspy.roi import Roi
        with self.assertRaises(ValueError):
            Roi(1, 2, 1, 4)

    def test__init__for__invalid_m_bounds__raises__ValueError(self):
        from mmpreprocesspy.roi import Roi
        with self.assertRaises(ValueError):
            Roi(3, 2, 1, 4)

    def test_roi_initializes_n2_correctly(self):
        from mmpreprocesspy.roi import Roi
        sut = Roi(1, 2, 3, 4)
        self.assertEqual(sut.n2, 4)

    def test_roi_initializes_m2_correctly(self):
        from mmpreprocesspy.roi import Roi
        sut = Roi(1, 2, 3, 4)
        self.assertEqual(sut.m2, 3)

    def test_roi_initializes_n1_correctly(self):
        from mmpreprocesspy.roi import Roi
        sut = Roi(1, 2, 3, 4)
        self.assertEqual(sut.n1, 2)

    def test_roi_initializes_m1_correctly(self):
        from mmpreprocesspy.roi import Roi
        sut = Roi(1, 2, 3, 4)
        self.assertEqual(sut.m1, 1)

