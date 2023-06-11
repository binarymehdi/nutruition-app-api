"""
Test custom Django commands.
"""
from unittest.mock import patch

from psycopg2 import OperationalError as Psycorpg2Error
