"""
AttendeeManager module for managing attendees in memory.

Manages all attendees in an easily managable manner, not an efficient manner.
Attendees must be Attendee objects for ease of use.

TODO:
    * Implement all methods
"""

from typing import *

from .attendee import Attendee

class AttendeeManager:
    """
    Managers all attendee objects in a convenient fashion.

    Attributes:
        TODO: document attributes
    """

    def __init__(self):
        """
        Constructor
        """
        raise NotImplementedError

    def add_attendee(self, attendee: Attendee, attendee_id: Hashable):
        """
        Add an attendee.

        Args:
            attendee (Attendee): The attendee to add.
            attendee_id (Hashable): How to uniquely identify the attendee.
        
        Raises:
            TypeError if attendee is not an Attendee object.
            TypeError if attendee_id is not hashable.
            ValueError if an attendee with attendee_id already exists.
        """
        raise NotImplementedError
    
    def get_attendee(self, attendee_id: Hashable):
        """
        Get an attendee object from the manager.

        Returns a reference to the attendee, not a copy.

        Args:
            attendee_id (Hashable): The unique identifier for the attendee.
        
        Returns:
            Attendee: The attendee object.
        
        Raises:
            KeyError if attendee does not exist
        """
        raise NotImplementedError

    def remove_attendee(self, attendee_id: Hashable):
        """
        Remove an attendee from the manager.

        Args:
            attendee_id (Hashable): The unique identifier for the attendee.
        
        Raises:
            KeyError if attendee does not exist.
        """
        raise NotImplementedError

    def __iter__(self):
        """Initialise iterator"""
        raise NotImplementedError

    def __next__(self) -> Attendee:
        """Get the next attendee"""
        raise NotImplementedError

    def __len__(self) -> int:
        """Return the number of attendees"""
        raise NotImplementedError