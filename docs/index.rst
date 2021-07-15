.. Certificate Automater documentation master file, created by
   sphinx-quickstart on Tue Jul 13 00:33:39 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Certificate Automater's documentation!
=================================================

Contributors
------------

| **Organisation:** Curtin IET On Campus
| **Project start:** June 2021
| **Project Lead:** Harrison Outram
| **Collaborators:**
|     - Elizabeth Stinton (2021 President)
|     - Li Shen (2021 Vice-President)
|     - Parakram Vishwakarma (2021 Events coordinator)
|     - Rehaab Syed (2021 Marketing coordinator)

Problem
-------

Making of certificates of attendance for event attendees is a tedious, time-consuming, and error prone process. Several steps are required to make these certificates, requiring Canva, Mailchimp, and some spreadsheet software (e.g. Excel). Takes at least 2 hours per 50 attendees for someone who knows what they are doing; **far** longer for someone who does not. Throughout the entire process, each certificate is checked thrice. Even then, there is a large room for human error, potentially resulting in some attendees receiving the wrong certificate or a typo.

Solution
--------

Create program to automate the process where possible. Must input CSV file of attendees, Mailchimp authorisation (e.g. API and server keys, or, preferrably, OAuth access), and certificate template. Outputs all certificates onto local machine, datalogs, failure/success report, updates CSV file with Mailchimp file URI, uploads certificates to Mailchimp, and updates Mailchimp contacts with certificate file URI.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   attendees/attendees

.. toctree::
   :maxdepth: 1

   certificate_maker
   cli
   mailchimp_manager
   test_driver

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
