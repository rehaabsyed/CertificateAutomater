"""
Module that converts attendee records between formats.

Can convert between Pandas DataFrame and proprietary AttendeeManager

TODO:
    * Implement functions
    * Implement datalogging
"""

import pandas as pd

from src.attendees.attendee_manager import Attendee, AttendeeManager

def pandas2manager(attendees: pd.DataFrame, ignore: set = None
                  ) -> AttendeeManager:
    """
    Convert Pandas DataFrame attendee record to AttendeeManager.

    Args:
        attendees (pd.DataFrame): The attendees as a Pandas DataFrame.
        ignore (set): Collection of attributes to ignore, if left as ``None`` will not ignore any fields.

    Returns:
        AttendeeManager: The attendees as a ``AttendeeManager``.
    """
    raise NotImplementedError

def manager2pandas(attendees: AttendeeManager, ignore: set = None
                  ) -> pd.DataFrame:
    """
    TODO: Write docstring
    """
    raise NotImplementedError