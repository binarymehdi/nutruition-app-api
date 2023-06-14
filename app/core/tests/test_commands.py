"""
Test custom Django commands.
"""
from unittest.mock import patch

from psycopg2 import OperationalError as Psycorpg2Error

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase

@patch('core.managememt.commands.wait_for_db.Command.check')
class DommandsTest(SimpleTestCase):
    """Test Commands"""

    def test_wait_for_db_ready(self, patched_check):
        """Test waiting for database if the database is ready. we do this via mocking"""
        patched_check.return_value = True

        call_command('wait_for_db')
        
        patched_check.assert_called_onnce_with(database=['default']) 