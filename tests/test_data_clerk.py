import unittest
from app.data_clerk import DataClerk, FileLog
from unittest.mock import Mock

class DataClerkTest(unittest.TestCase):
    def test_process_data(self):
        # Arrange
        fl = FileLog()
        cut = DataClerk(fl)

        # Act
        cut.process_data()

        # Assert
        # No assert, just checking that it runs (like the original Java test)
        # Output must be inspected manually or via logging


    def test_files_are_logged_before_8pm_mocked(self):
        # Arrange
        mock_file_log = Mock()
        cut = DataClerk(mock_file_log)

        # Act
        cut.process_data()

        # Assert
        mock_file_log.clear_the_log.assert_called_once()



if __name__ == '__main__':
    unittest.main()

