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
        self._misc = kwargs.copy()
         
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
        for key,value in kwargs.items():
            return value

    # set & get for misc - separate for the miscs
    # need to pass in key & value, changing value, mutating object 

    @property
    def get_fname(self):
        return self._fname

    @property
    def get_lname(self):
        return self._lname
        
    @property
    def get_email(self):
        return self._email

    @property
    def get_file_path(self):
        return self._file_path

    @property
    def get_file_url(self):
        return self._file_url
        
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
        if self._fname == None:
            return False
        else:
            return True
    
    @property
    def has_lname:    
        if self._lname == None:
            return False
        else:
            return True
    
    @property
    def has_email:    
        if self._email == None:
            return False
        else:
            return True

    @property
    def has_file_url:    
        if self._file_url == None:
            return False
        else:
            return True

    @property
    def has_file_path:    
        if self._file_url == None:
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
    def fname(self, value):
        self._fname = value
    
    # is below what needs to be in the verifyFunc function?
        for i in value:
            if i is not in valid_set:
                raise ValueError(f"Name must not contain {i}")

    @lname.setter
    def lname(self, value):
        self._lname = value

    @email.setter
    def email(self, value): # check if string / empty string
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
                
    
