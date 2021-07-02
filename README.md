![*IET Logo missing*](https://github.com/Harrison-O/CertificateMaker/blob/readme/assets/IET_Logo_Blue_RGB.png "Blue IET Logo")

# Certificate Maker

## Table of Contents

**[Cover](#cover)**<br>
**[Project Gist](#project-gist)**<br>
**[Project Breakdown](#project-breakdown)**<br>
**[Project Usability Requirements](#project-usability-requirements)**<br>
**[Project Technical Requirements](#project-technical-requirements)**<br>

## Cover

**Organisation:** Curtin IET On Campus</br>
**Project start:** June 2021</br>
**Project Lead:** Harrison Outram</br>
**Collaborators:**</br>
* Elizabeth Stinton (2021 President)</br>
* Li Shen (2021 Vice-President)</br>
* Parakram Vishwakarma (2021 Events coordinator)</br>
* Ekaterina Grabovskaya (2021 Events coordinator)</br>

## Project Gist

### Problem
Making of certificates of attendance for event attendees is a tedious, time-consuming, and error prone process. Several steps are required to make these certificates, requiring Canva, Mailchimp, and some spreadsheet software (e.g. Excel). Takes at least 2 hours per 50 attendees for someone who knows what they are doing; **far** longer for someone who does not. Throughout the entire process, each certificate is checked thrice. Even then, there is a large room for human error, potentially resulting in some attendees receiving the wrong certificate or a typo.

### Solution

Create program to automate the process where possible. Must input CSV file of attendees, Mailchimp authorisation (e.g. API and server keys, or, preferrably, OAuth access), and certificate template. Outputs all certificates onto local machine, datalogs, failure/success report, updates CSV file with Mailchimp file URI, uploads certificates to Mailchimp, and updates Mailchimp contacts with certificate file URI.

## Project Breakdown

By using the Mailchimp API and various Python libraries, almost all of the manuals steps of the old solution can be automated. The program's steps are

1. Input an attendee record as a CSV.
2. Input a certificate template as a PDF.
3. Input Mailchimp authorisation from user.
4. Process attendee record, generating a certificate of attendance for each attendee using the template.
5. Upload certificates of attendance to Mailchimp, recording the responses.
6. Update attendee record with file URIs.
7. Update Mailchimp contacts with file URIs.
8. Output results and progress to user.

## Project stages

1. Create prototype for internal use only.
2. Create minimal viable product (MVP).
3. Send to other student clubs for feedback.
4. Refine product.
5. Get feedback from selected student clubs.
.. a. If feedback negative, go to step 4.
.. b. If feedback positive, go to step 6.
6. Release product to the public.

A full list of product requirements for the prototype, MVP, and professional product are available in the kickstart document.

## Project Standards

### Coding Standards

1. Must be written in Python 3.
2. All code must be written into decoupled submodules, excluding the `main` and user interface modules.
3. Must include Sphinx documentation for the MVP onwards.
4. Must include Google docstrings in source code where appropriate.
5. Comments must be included where it is not obvious as to what code is doing or why it is written the way it is.
6. Simple, short, and descriptive identifiers must be used.
7. Must include `requirements.txt` file.
8. All submodules must come with an exhaustive test script that tests the submodule with both valid and invalid data.
9. Error objects of the appropriate type must be raised/thrown when appropriate.
10. All parameter and return datatypes must be declared.
    * See the [typing library](https://docs.python.org/3/library/typing.html)
11. All functions/methods must be as short as possible.
    * More functions are preferred over longer functions.

### Version control standards

1. All code changes must go through a pull request.
2. All pull requests must go through a code review to ensure the above coding standards are abided by.
3. Pull request reviews must include ultra-specific criticism that makes it easy for the developer to fix them.
