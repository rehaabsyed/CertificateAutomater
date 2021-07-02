"""
Module for creating certificates given a template and the attendees.

Currently only accepts .docx files as templates. Templates must have merge
fields or variables to substitute into. Certificates will be saved as PDF files.

TODO
    * Implement functions
    * Use multiprocessing to speed up certificate creation.
    * Impement datalogging
    * Research other options for templates besides .docx files.
    * Research other options for certificates besides PDF files.
"""

from typing import *

from src.attendees.attendee_manager import Attendee, AttendeeManager

def createCertificate(in_path: str, out_path: str, attendees: AttendeeManager,
                     namingFunc: Callable[[Attendee], str] = None,
                     statusFunc: Callable[[Attendee, bool], None] = None,
                     overwrite: bool = True) -> List[Tuple[Attendee, Exception]]:
    """
    Creates and saves certificates given template and the attendee record.

    Args:
        in_path (str): The path to the template document.
        out_dir (str): The folder to save the certificate to.
        namingFunc (Callable[[Attendee], str]): What to name the certificate,
        excluding the file extension. Defaults to None, meaning certificates
        are automatically named.
        statusFunc (Callable[[Attendee, bool], None]): Status update function to
        inform caller of what certificates have been made. Must take in Attendee
        and whether it was successfully created (bool). Useful for user
        interfaces. If left as None, does nothing.
        overwrite (bool): Whether to overwrite certificate file that already
        exist, defaults to True.
    
    Returns:
        List of attendee-exception tuple of attendees that failed to create a
        certificate for. Returns an empty list if no errors occur.
    
    Raises:
        OSError if template file IO error occurs.
    """
    raise NotImplementedError