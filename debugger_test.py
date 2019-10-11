import unittest
import debugger as d

script_name = 'script_to_debug.py'


class DistributedStorageTest(unittest.TestCase):

    def test_debugger_output_without_breakpoints(self):
        handler = d.Handler()

        d.debug(script_name, [], handler)

        self.assertEqual(set(), set(handler.handled_messages))


if __name__ == '__main__':
    unittest.main()
