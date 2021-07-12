"""
AttendeeManager module for managing attendees in memory.

Manages all attendees in an easily managable manner, not an efficient manner.
Attendees must be Attendee objects for ease of use.

TODO:
    * Implement all methods
    * Impement datalogging
"""

from typing import *

from src.attendees.attendee import Attendee

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

    def add_attribute(self, key: Hashable, values: Dict[Hashable, Any] = {}):
        """
        Add an attribute for all attendees.

        Useful for adding attribute for all attendees in one line of code.
        Will overwrite values if attribute already exists.

        Args:
            key (Hashable): The key/name of the attribute.
            values (Dict[Hashable, Any]): A mapping from attendee ID to initial
            value of the new attribute. Defaults to empty dictionary (no
            initialision).
        
        Raises:
            TypeError if key is not Hashable.
            TypeError if values is not a dictionary.
        """
        raise NotImplementedError

    def remove_attribute(self, key: Hashable):
        """
        Removes an attribute for all attendees.

        Useful for removing attribute for all attendees in one line of code.
        Does nothing if no attendees has the attribute.

        Args:
            key (Hashable): The key/name of the attribute.

        Raises:
            TypeError if key is not Hashable.
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