import unittest
from helper import to_bytes, to_hex_list, to_int_list, to_str

class TestHelper(unittest.TestCase):
    def setUp(self):
        self.my_str = 'hello world'
        self.my_bytes = b'hello world'
        self.my_int_list = [104, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100]
        self.my_hex_list = ['0x68', '0x65', '0x6c', '0x6c', '0x6f', '0x20', '0x77', '0x6f', '0x72', '0x6c', '0x64']

    # TEST to_str()
    def test_str_to_str(self):
        actual = to_str(self.my_str)
        expected = self.my_str
        self.assertEqual(actual, expected)
    
    def test_bytes_to_str(self):
        actual = to_str(self.my_bytes)
        expected = self.my_str
        self.assertEqual(actual, expected)

    def test_int_list_to_str(self):
        actual = to_str(self.my_int_list)
        expected = self.my_str
        self.assertEqual(actual, expected)

    def test_hex_list_to_str(self):
        actual = to_str(self.my_hex_list)
        expected = self.my_str
        self.assertEqual(actual, expected)

    # TEST to_bytes()
    def test_str_to_bytes(self):
        actual = to_bytes(self.my_str)
        expected = self.my_bytes
        self.assertEqual(actual, expected)
    
    def test_bytes_to_bytes(self):
        actual = to_bytes(self.my_bytes)
        expected = self.my_bytes
        self.assertEqual(actual, expected)

    def test_int_list_to_bytes(self):
        actual = to_bytes(self.my_int_list)
        expected = self.my_bytes
        self.assertEqual(actual, expected)

    def test_hex_list_to_bytes(self):
        actual = to_bytes(self.my_hex_list)
        expected = self.my_bytes
        self.assertEqual(actual, expected)

    # TEST to_int_list()
    def test_str_to_int_list(self):
        actual = to_int_list(self.my_str)
        expected = self.my_int_list
        self.assertEqual(actual, expected)
    
    def test_bytes_to_int_list(self):
        actual = to_int_list(self.my_bytes)
        expected = self.my_int_list
        self.assertEqual(actual, expected)

    def test_int_list_to_int_list(self):
        actual = to_int_list(self.my_int_list)
        expected = self.my_int_list
        self.assertEqual(actual, expected)

    def test_hex_list_to_int_list(self):
        actual = to_int_list(self.my_hex_list)
        expected = self.my_int_list
        self.assertEqual(actual, expected)

    # TEST to_hex_list()
    def test_str_to_hex_list(self):
        actual = to_hex_list(self.my_str)
        expected = self.my_hex_list
        self.assertEqual(actual, expected)
    
    def test_bytes_to_hex_list(self):
        actual = to_hex_list(self.my_bytes)
        expected = self.my_hex_list
        self.assertEqual(actual, expected)

    def test_int_list_to_hex_list(self):
        actual = to_hex_list(self.my_int_list)
        expected = self.my_hex_list
        self.assertEqual(actual, expected)

    def test_hex_list_to_hex_list(self):
        actual = to_hex_list(self.my_hex_list)
        expected = self.my_hex_list
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()