import unittest
from television import Television

class TestTelevision(unittest.TestCase):
    def setUp(self):
        self.tv = Television()

    def test_initial_state(self):
        self.assertFalse(self.tv.power_state)
        self.assertEqual(self.tv.channel, 0)
        self.assertEqual(self.tv.volume, 0)

    def test_power_toggle(self):
        self.tv.power()
        self.assertTrue(self.tv.power_state)
        self.tv.power()
        self.assertFalse(self.tv.power_state)

    def test_channel_up_down(self):
        self.tv.power()
        self.tv.channel_up()
        self.assertEqual(self.tv.channel, 1)
        self.tv.channel_down()
        self.assertEqual(self.tv.channel, 0)

    def test_volume_up_down(self):
        self.tv.power()
        self.tv.volume_up()
        self.assertEqual(self.tv.volume, 1)
        self.tv.volume_down()
        self.assertEqual(self.tv.volume, 0)

    def test_mute_functionality(self):
        self.tv.power()
        self.tv.volume_up()
        self.assertEqual(self.tv.volume, 1)
        self.tv.mute()
        self.assertEqual(self.tv.volume, 0)

    def test_mute_toggle(self):
        self.tv.power()
        self.tv.volume_up()
        self.tv.mute()
        self.assertEqual(self.tv.volume, 0)
        self.tv.mute()
        self.assertEqual(self.tv.volume, 1)

if __name__ == '__main__':
    unittest.main()