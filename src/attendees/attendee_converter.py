"""
Module that converts attendee records between formats.

Can convert between Pandas DataFrame and proprietary AttendeeManager

TODO
    * Implement functions
    * Implement datalogging
"""

import pandas as pd

from .attendee_manager import Attendee, AttendeeManager

def pandas2manager(attendees: pd.DataFrame) -> AttendeeManager:
    """
    Convert Pandas DataFrame attendee record to AttendeeManager.

    Args:
        attendees (pd.DataFrame): The attendees as a Pandas DataFrame.

    Returns:
        AttendeeManager: The attendees as a AttendeeManager.
    """
    raise NotImplementedError

def manager2pandas(attendees: AttendeeManager) -> pd.DataFrame:
    """
    TODO: Write docstring
    """
    raise NotImplementedError