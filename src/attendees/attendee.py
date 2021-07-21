"""
Module for Attendee class.

Designed to be easy to use, not efficient.

TODO:
    * Implement methods
    * Write getters and setters
    * Implement datalogging
"""

## getters & setters - @property 

from typing import *

VerifyFunc = Callable[[Hashable, Any], bool]

class Attendee:
    """
    """

    def __init__(self, fname: str, lname: str, email: str,
                 file_path: str = None, file_url: str = None, **kwargs):
        """
        Constructor.

        Args:
            fname (str): The first or given name of the attendee.
            lname (str): The last or family name of the attendee.
            email (str): Email address of the attendee.
            file_path (str): The path to the certificate file, defaults to None.
            file_url (str): The URL to the certificate file, defaults to None.
            kwargs (dict): All other attributes of the attendee.
        """
        self.fname = fname
        self.lname = lname
        self.email = email
        self.file_path = file_path
        self.file_url = file_url

        raise NotImplementedError

    # TODO: Write getters for fname, lname, email, file_path, and file_url

    def get_attribute(self, key: Hashable) -> Any:
        """
        Get an arbitrary attribute of the attendee.

        Args:
            key (Hashable): The name of the attribute.
        
        Returns:
            Any: The attribute value.
        
        Raises:
            TypeError if key is not hashable.
            KeyError if attendee does not have attribute with name key.
        """
        return self.key

        raise NotImplementedError

    def has_attribute(self, key: Hashable) -> bool:
        """
        Checks if Attendee has a specificed attribute.

        Args:
            key (Hashable): The key/name of the attribute.
        
        Returns:
            bool: True if Attendee has attribute and vice-versa.
        """
        raise NotImplementedError

    def set_attribute(self, key: Hashable, value: Any,
                     verifyFunc: VerifyFunc = None):
        """
        Set an arbitrary attribute of the attendee.

        Will add the attribute if it doesn't exist.

        Args:
            key (Hashable): The name of the attribute.
            value (Any): The attribute value.
            verifyFunc (Callable[[Hashable, Any], bool]): A function to verify
            the value being set, if let as None, will not verify value.
        
        Raises:
            TypeError if key is not hashable.
            ValueError if key is "fname", "lname", or "email"
        """
        self.key = key
        self.value = value
        self.verifyFunc = verifyFunc

        raise NotImplementedError
        
        if type(key) is not Hashable:
            raise TypeError("key is not hashable")

        if key is 'fname'
            raise ValueError("key cannot be 'fname'")

    def remove_attribute(self, key: Hashable):
        """
        Remove an attribute from the attendee.

        Args:
            key (Hashable): The name of the attendee.
        
        Raises:
            TypeError if key is not hashable.
        """
        
        raise NotImplementedError
                
        raise TypeError

