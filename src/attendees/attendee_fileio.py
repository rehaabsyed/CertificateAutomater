"""
Module with functionality to save and load attendees from a CSV file.

Future upgrades should be able to load attendees from an Excel file.

TODO:
    * Implement functions
    * Further detail the OSErrors that can be raised
    * Impement datalogging
"""

import pandas as pd

def load_attendee_record(path: str) -> pd.DataFrame:
    """
    Loads attendees from a file.

    File must be a CSV file.

    Args:
        path (str): The absolute or relative path to the file.
    
    Raises:
        OSError: if file IO error occurs.
    """
    raise NotImplementedError

def save_attendee_record(path: str, attendees: pd.DataFrame):
    """
    Save attendee record to a file.

    Args:
        path (str): Where to save to file, including the filename.
        attendees (pd.DataFrame): The attendee record.
    
    Raises:
        TypeError: if attendees is not a Pandas DataFrame
        OSError: if file IO error occurs
    """
    raise NotImplementedError