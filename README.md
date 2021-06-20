![*IET Logo missing*](https://github.com/Harrison-O/CertificateMaker/blob/readme/assets/IET_Logo_Blue_RGB.png "Blue IET Logo")

# Certificate Maker

## Table of Contents

**[Cover](#cover)**<br>
**[Project Gist](#project-gist)**<br>
**[Project Breakdown](#project-breakdown)**<br>
**[Program Usability Requirements](#project-usability-requirements)**<br>
**[Program Technical Requirements](#project-technical-requirements)**<br>

## Cover

Organisation: Curtin IET On Campus</br>
Project start: 2021</br>
Project Lead: Harrison Outram</br>
Collaborators:</br>
* Elizabeth Stinton (President)</br>
* Li Shen (Vice-President)</br>
* Parakram Vishwakarma (Events coordinator)</br>
* Ekaterina Grabovskaya (events coordinator)</br>

## Project Gist

### Problem
Making of certificates of attendance for event attendees is a tedious, time-consuming, and error prone process. Several steps are required to make these certificates, requiring Canva, Mailchimp, and some spreadsheet software (e.g. Excel). Takes at least 2 hours per 50 attendees for someone who knows what they are doing; **far** longer for someone who does not. Throughout the entire process, each certificate is checked thrice. Even then, there is a large room for human error, potentially resulting in some attendees receiving the wrong certificate or a typo.

### Solution

Create program to automate the process where possible. Must input CSV file of attendees, Mailchimp authorisation (e.g. API and server keys, or, preferrably, OAuth access), and certificate template. Outputs all certificates onto local machine, datalogs, failure/success report, updates CSV file with Mailchimp file URI, uploads certificates to Mailchimp, and updates Mailchimp contacts with certificate file URI.

## Project Breakdown

### Old Solution

1. Get event attendance record from events team.
2. Review attendance record for anomalies (e.g. duplicate email addresses, missing names, etc.)
3. Clean attendance record.
4. Log into Canva.
5. Find certificate of attendance template.
6. For each attendee, write and download a certificate of attendance, making sure that the file naming convention is consistent, readable, simple, and unique for each attendee.
7. Double check that each certificate has been made and named correctly.
8. Redo any erroneous certificates.
9. Log out of Canva.
10. Log into Mailchimp.
11. Navigate to Content Studio.
12. Upload certificates of attendance.
13. For each certificate of attendance, copy and paste the Mailchimp generated URI into the attendance record as a new column (name it "file" or "certificate").
14. Double check that each URI has been assigned the correct attendee in the attendance record.
15. Using attendance record, update contacts in Mailchimp.
16. Create mock campaign to send to attendees.
17. For each attendee, check that the "Download Certificate of Attendance" button works and downloads the correct certificate.
18. Fix any erroneous certificates.
19. Delete mock campaign.
20. Write email template.
21. Get exec approval.
22. Send email.

### Proposed solution

By using the Mailchimp API and various Python libraries, steps 4-19 of the old solution can be automated or made redundant.

Will require script that can:
1. Input an attendee record as a CSV.
2. Input a certificate template as a PDF.
3. Input Mailchimp authorisation from user.
4. Process attendee record, generating a certificate of attendance for each attendee using the template.
5. Upload certificates of attendance to Mailchimp, recording the responses.
6. Update attendee record with file URIs.
7. Update Mailchimp contacts with file URIs.
8. Output results and progress to user.

## Program Usability Requirements

### Minimal Viable Product

For the sake of time, a minimal viable product (MVP) can be implemented first. The MVP must include:
1. Command line interface to run program.
2. Program must run with certificate template path, attendee record path, and Mailchimp API and server keys as command line arguments.
3. Generate a certificate of attendance for each attendee
    * Must be saved into a folder called `/certificates` in the current working directory.
    * Each certificate must be named based on the attendee's full name.
5. Upload certificates to Mailchimp, keeping track of which certificate belongs to who.
6. Update the attendance record with the certificate file URIs.
7. Update Mailchimp contacts with file URIs.
8. Inform user of what the program is currently doing
    * Can be a simple sentence, e.g. "Uploading certificates to Mailchimp"
9. Be able to process errors without crashing.
10. Must be able to continue processing certificates even if one fails.
11. Must inform user of which steps or certificates failed with an informative error message.
    * Can be outputted once program has finished everything.
12. Must be able to run on Windows, Mac, and Linux that can run Python 3.

For the sake of simplicity, the following assumptions can be made:
1. The certificate of attendance is known.
    * Only placeholder field is the attendee name.
    * Exact location of placeholder fields is known.
2. The attendance record contains no errors.

### Professional Product

Has all the criteria of MVP, and:
1. Can be run via an executable; no command line should be involved.
2. Should have a simple and inituitive GUI.
3. Can select where input files are located via file explorer.
4. Log everything to a log file, excluding debug messages.
5. Must use OAuth to get Mailchimp authorisation.
6. Should be able to inform the user of errors that occur in real time without interrupting background tasks.
7. Use appropriate colour coding and symbols to instantly inform the user of success/failure.
8. Must be able to instantly respond to user inputs without stuttering.

### Ideal Product

Has all criteria of professional product, and
1. Has ultra-specific error messages to inform user of what exactly went wrong
    * Must include how to fix issue where possible
2. Must include an installer with a build machine to create an executable.
3. Allows user to select what to log.
4. Allows user to select where to save log files to.
5. Must be able to save PDF report of what happened.
    * Must be able to select what goes on the PDF report.

## Project Technical Requirements

### Coding Standards

1. Must be written in Python 3.
2. All code must be written into decoupled submodules.
3. Must include Doxygen or Sphinx documentation.
4. Comments must be included where it is not obvious as to what code is doing or why it is written the way it is.
5. Simple, short, and descriptive identifiers must be used.
6. Must include `requirements.txt` file.
7. All submodules must come with an exhaustive test script that tests the submodule with both valid and invalid data.
8. Error objects of the appropriate type must be raised/thrown when appropriate.
9. All parameter and return datatypes must be declared.
    * See the (typing library)[https://docs.python.org/3/library/typing.html]
10. All functions/methods must be as short as possible.
    * More functions are preferred over longer functions.

### Version control standards

1. All code changes must go through a pull request.
2. All pull requests must go through a code review to ensure the above coding standards are abided by.
3. Pull request reviews must include ultra-specific criticism that makes it easy for the developer to fix them.
