## About the Project

The Estate Union Dues Tracker is a simple Python program designed to help a residents' association chairman keep track of members and their monthly union dues.

The program allows the chairman to:

* Register new members
* Record members' payments
* View all registered members
* Check who is up to date and who is owing
* View a member's payment history
* Keep the information after the program is closed and opened again
* Keep a readable activity log of registrations and payments

The main reason I built the program this way is because the data should not disappear when the program is closed.


### What each file does

**main.py**

This is the only file that I run directly. It contains the menu and handles the interaction with the user. The actual work is handled by functions inside the package.

**members.py**

This module handles member-related operations, such as registering a new member.

**payments.py**

This module handles recording payments, viewing payment history, and checking members' dues status.

**storage.py**

This module handles saving and loading the program's data. The data is stored in a JSON file so that it remains available after the program is closed.

**logger.py**

This module handles the activity diary. It records important events such as member registration and payments, together with the date and time.

****init**.py**

This file makes `estate_tracker` a Python package.


## How to Run the Program

Make sure Python is installed on the computer.

Open a terminal in the project folder:

```text
estate_dues_tracker
```

Then run:

```bash
python main.py
```

`main.py` is the only file that should be run directly.



## Data Persistence

The program uses a JSON data file to save the members and their payment information.

On the first run, the data file may not exist yet. In that case, the program starts with an empty set of records instead of crashing.

When information is added or changed, it is saved so that it can be loaded again the next time the program runs.



## Activity Log

The program also keeps an activity log in a plain text file.

The log records events such as:

```text
2026-08-24 18:20:10 - Registered member: M001 - John Doe
2026-08-24 18:25:42 - Payment recorded: M001 - August - ₦5000
```

The log is opened in append mode so that new events are added to the end of the file instead of deleting previous records.

The file can be opened with a normal text editor without running the Python program.

---

## Error Handling

The program also checks for some common problems.

If the data file does not exist, the program starts with fresh data.

If the saved JSON data is corrupted or cannot be read, the program displays a simple error message instead of showing a Python traceback and crashing.

Invalid values entered by the user, such as an amount that is not a number, are also handled where necessary.

---

## Python Concepts Used

Some of the main Python concepts used in this project are:

* Dictionaries
* Lists
* Functions
* Modules
* Packages
* Imports
* Loops
* Conditional statements
* File handling
* JSON
* Exception handling
* Date and time
* String formatting


## Design Approach

I separated the program into different modules so that each module has a clear responsibility.

Instead of putting all the code inside `main.py`, the menu calls functions from the appropriate modules.

For example:

* Member operations go to `members.py`
* Payment operations go to `payments.py`
* Saving and loading go to `storage.py`
* Activity logging goes to `logger.py`

This makes the program easier to understand and maintain.

---

## Testing

I tested the program by:

1. Running it without an existing data file.
2. Registering multiple members.
3. Recording a payment.
4. Closing and reopening the program.
5. Checking that the saved information was still available.
6. Checking the activity log.
7. Testing invalid input.
8. Testing what happens when the saved data cannot be read.

The most important test was closing the program and opening it again to confirm that the data was persistent.
