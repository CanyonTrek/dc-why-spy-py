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


    def test_files_are_wrongly_logged_after_8pm_mocked(self):
        # This test will fail if the real system time is before 8pm
        # because DataClerk uses current time in its logic.
        # In Git tag v1.4, DataClerk was updated to accept the current time as an argument.

        # Arrange
        mock_file_log = Mock()
        cut = DataClerk(mock_file_log)

        # Act
        # WARNING: This uses real system time and fails before 8pm
        cut.process_data()

        # Assert
        mock_file_log.clear_the_log.assert_not_called()



if __name__ == '__main__':
    unittest.main()

