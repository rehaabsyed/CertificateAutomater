"""
Module for Attendee class.

Designed to be easy to use, not efficient.

TODO:
    * Implement methods
    * Write getters and setters
    * Implement datalogging
    * Implement email address validation
    * Add UTF-8 support for validating names
"""

from typing import *
import string

VerifyFunc = Callable[[Hashable, Any], bool] 
#use docstrings when something accessible outside of program, others need to know what not how
"""
1 sentence summery

Args:
    key (Hashable)

Return:
    bool: True if...
"""
class Attendee:
    """
    """
    valid_name_chars = set(string.ascii_lowercase + string.ascii_uppercase + "'- ") 
    invalid_name_chars = set("'- ")

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
        return self._misc[key] # return specific one passed into get_attr

    @property
    def fname(self):
        return self._fname
        # having func names as nouns rather than verb, not doing anything just returning a value

    @property
    def lname(self):
        return self._lname
        
    @property
    def email(self):
        return self._email

    @property
    def file_path(self):
        return self._file_path

    @property
    def file_url(self):
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
    def has_fname(self):    
        return self._fname == None
    
    @property
    def has_lname(self):    
        return self._lname == None # already gives a boolean, if statements always accept boolean

    # if condtion, if not condition (i.e. else)
    
    @property
    def has_email(self):    
        return self._email == None

    @property
    def has_file_url(self):    
        return self._file_url == None

    @property
    def has_file_path(self):    
        return self._file_url == None
    
    def set_attribute(self, key: Hashable, value: Any,
                     verifyFunc: VerifyFunc = None): #verifyFunc is a function, a callback - the what, for miscellaneous, 
                    # i wont write callback, will use it
        """
        Set an arbitrary attribute of the attendee.

        Will add the attribute if it doesn't exist. First Checks if `verifyFunc`
        is `None`. If `None`, do not verify value, any value is validOnce verified,
        set misc attribute using `key`.

        Args:
            key (Hashable): The name of the attribute.
            value (Any): The attribute value.
            verifyFunc (Callable[[Hashable, Any], bool]): A function to verify
            the value being set, if let as `None`, will not verify value. If
            `True`, value is valid and vice-versa.
        
        Raises:
            TypeError: if `key` is not hashable.
            ValueError: if `key` is "fname", "lname", or "email"
            ValueError: if verifyFunc returns `False`
        """
        if verifyFunc is not None: # if None, dont need to verify
            verifyFunc(key, value) # need to make sure its correct
            if not verifyFunc(key, value):
                # raise error - value is not valid fo this key
                raise NotImplementedError

        self._misc[key] = value

    @classmethod
    def checkString(cls, value):    # checks if string and if empty
        # cls, allows u to use func without creating object. MyClass.func()
        if type(value) != str:
            raise TypeError("Value should be a string")
        if value == "":
            raise ValueError("Value is empty")

    @classmethod
    def verifyName(cls, string): 
        cls.checkString(string)
        if string[0].islower():    # checks for first letter capital
            raise ValueError("Name must start with capital letter")
        
        n = len(string)-1
        if string[n] in cls.invalid_name_chars:    # checks if ends in - ' or space
            raise ValueError(f"Name cannot end with {string[n]}")
        
        # ref a ptr that automatically derefs when using it, all objects refer to w ref
        # == : checks for equivalence, 2 sep objects, for whats inside it
        # is : checks for same thing, 2 references pointing to same thing. 
        # if head is tail for linked list 1 element. head == tail, 'bob' at both tail & head

        for char in string:    # checks if contains alphabet chars only
            if char not in cls.valid_name_char:
                raise ValueError(f"Name must not contain {char}")

        names = ["bob", "charlie", "charlene"]
        for i in range(len(names)):
            names[i]  for loop only does index when using range 

        
    @fname.setter
    def fname(self, value):
        self.verifyName(value)
        self._fname = value # wont get to this line if error is raised
        
    @lname.setter
    def lname(self, value):
        self.verifyName(value)
        self._lname = value

    @email.setter
    def email(self, value): 
        self.checkString(value)
        self._email = value
    
    @file_url.setter
    def file_url(self, value):
        self.checkString(value)
        self._file_url = value
    
    @file_path.setter
    def file_url(self, value):
        self.checkString(value)
        self._file_path = value

    def remove_attribute(self, key: Hashable):
        """
        Remove an attribute from the attendee.

        Args:
            key (Hashable): The name of the attendee.
        
        Raises:
            TypeError: if key is not hashable.
        """
               
        del self._misc[key]
    
