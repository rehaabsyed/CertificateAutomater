"""
Module for Attendee class.

Designed to be easy to use, not efficient.

TODO:
    * Implement methods
    * Write getters and setters
    * Implement datalogging
"""

from typing import *
import string

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
        self._fname = fname
        self._lname = lname
        self._email = email
        self._file_path = file_path
        self._file_url = file_url
        
        #for item in kwargs.items():
            #return/ ignore item?

    # TODO: Write getters for fname, lname, email, file_path, and file_url

    def get_attribute(self, key: Hashable) -> Any:
        """
        Get an arbitrary attribute of the attendee.

        Args:
            key (Hashable): The name of the attribute.
        
        Returns:
            Any: The attribute value.
        
        Raises:
            TypeError: if key is not hashable.
            KeyError: if attendee does not have attribute with name key.
        """

    @property
    def get_fname(self):
        if self._fname.values() = None:
            raise KeyError('Attendee does not have attribute with name key')
        else:
            return self._fname.values()

    @property
    def get_lname(self):
        return self._lname.values()
        
    @property
    def get_email(self):
        return self._email.values()

    @property
    def get_file_path(self):
        return self._file_path.values()

    @property
    def get_file_url(self):
        return self._file_url.values()
        
    def has_attribute(self, key: Hashable) -> bool:
        """
        Checks if Attendee has a specificed attribute.

        Args:
            key (Hashable): The key/name of the attribute.
        
        Returns:
            bool: True if Attendee has attribute and vice-versa.
        """
    @property
    def has_fname:    
        if self.fname == None:
            return False
        else:
            return True

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
            TypeError: if key is not hashable.
            ValueError: if key is "fname", "lname", or "email"
        """

        global valid_set
        a = string.ascii_lowercase
        valid_set = set(a) 
        
        @fname.setter
        def set_fname(self, value):
            self._fname = value
        
        # is below what needs to be in the verifyFunc function?
            for i in value:
                if i is in valid_set:
                    None
            elif:
                raise ValueError(f"Name must not contain {i}")

        @lname.setter
        def set_lname(self, value):
            self._lname = value

        @email.setter
        def set_email(self, value):
            self._email = value

    def remove_attribute(self, key: Hashable):
        """
        Remove an attribute from the attendee.

        Args:
            key (Hashable): The name of the attendee.
        
        Raises:
            TypeError: if key is not hashable.
        """
        
        del(self._fname.values())
                
    
