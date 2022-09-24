import unittest
from app import checksum_file
import os

class TestChecksumFile(unittest.TestCase):

    FILE_ADDRESS = ""
    def test_file_address(self):
        self.assertEqual(type(checksum_file(self.FILE_ADDRESS)) , str )
        self.assertEqual(len(checksum_file(self.FILE_ADDRESS)) , 32 )



if __name__ == "__main__":
    TestChecksumFile.FILE_ADDRESS = os.environ.get('FILE_ADDRESS')
    unittest.main()