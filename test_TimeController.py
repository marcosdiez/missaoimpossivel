#!/usr/bin/env python3
import TimeController

import unittest
import time
import datetime


class TestTimeController(unittest.TestCase):
    def setUp(self):
        self.last_time = None

    def print_status(self, tc):
        result = tc.status()
        print(result)
        self.last_time = result
        return result

    def assert_time_did_not_change(self, tc):
        assert tc.status() == self.last_time

    def assert_time_short_less_than(self, tc, seconds):
        result = self.print_status(tc)
        assert result < datetime.timedelta(seconds=seconds)
        assert result > datetime.timedelta(seconds=seconds - 1)

    def test_timecontroller(self):
        print("init...")
        tc = TimeController.TimeController()
        assert tc.is_running() == False
        assert self.print_status(tc) == datetime.timedelta(seconds=0)
        time.sleep(1)
        self.assert_time_did_not_change(tc)
        assert tc.is_running() == False

        print("Starting...")
        tc.start()
        assert tc.is_running() == True
        self.print_status(tc)
        self.assert_time_short_less_than(tc, 1)
        time.sleep(1)
        self.assert_time_short_less_than(tc, 2)
        assert tc.is_running() == True

        print("Pausing....")
        tc.pause()
        assert tc.is_running() == False
        self.assert_time_short_less_than(tc, 2)
        time.sleep(1)
        self.assert_time_did_not_change(tc)
        assert tc.is_running() == False

        print("Unpause...")
        tc.unpause()
        assert tc.is_running() == True
        self.assert_time_short_less_than(tc, 2)
        time.sleep(1)
        self.assert_time_short_less_than(tc, 3)
        assert tc.is_running() == True

        print("PauseOrUnPause... [should pause]")
        tc.pause_or_unpause()
        assert tc.is_running() == False
        self.assert_time_short_less_than(tc, 3)
        time.sleep(1)
        self.assert_time_did_not_change(tc)
        assert tc.is_running() == False

        print("PauseOrUnPause... [should unpause]")
        tc.pause_or_unpause()
        assert tc.is_running() == True
        self.assert_time_short_less_than(tc, 3)
        time.sleep(1)
        self.assert_time_short_less_than(tc, 4)
        assert tc.is_running() == True

        print("PauseOrUnPause2... [should pause]")
        tc.pause_or_unpause()
        assert tc.is_running() == False
        self.assert_time_short_less_than(tc, 4)
        time.sleep(1)
        self.assert_time_did_not_change(tc)
        assert tc.is_running() == False

        print("PauseOrUnPause... [should unpause]")
        tc.pause_or_unpause()
        assert tc.is_running() == True
        self.assert_time_short_less_than(tc, 4)
        time.sleep(1)
        self.assert_time_short_less_than(tc, 5)
        assert tc.is_running() == True

        print("Reset...")
        tc.reset()
        assert tc.is_running() == False
        assert self.print_status(tc) == datetime.timedelta(seconds=0)
        time.sleep(1)
        self.assert_time_did_not_change(tc)
        assert tc.is_running() == False

        print("Done")

    # def test_upper(self):
    #     self.assertEqual('foo'.upper(), 'FOO')

    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)


if __name__ == "__main__":
    unittest.main()
