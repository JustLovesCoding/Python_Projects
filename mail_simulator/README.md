# Mail Simulator

[← Back to Python Projects](../README.md)

A small Python email simulation that models sending, receiving, reading, and deleting messages between users.

## Overview

This project demonstrates object-oriented programming in Python using a simple email system. It includes classes for users, inboxes, and messages, allowing two users to communicate through a simulated inbox.

## Features

- Create users with their own inbox
- Send emails to other users
- Store messages in each user's inbox
- Display a list of emails with read/unread status
- Read a specific email in full
- Delete messages from the inbox
- Track the timestamp of each sent message

## Project Files

- `main.py` — contains the email simulation logic and example usage

## Main Classes

### `Email`
Stores the sender, receiver, subject, body, timestamp, and read status.

### `User`
Represents a user in the system and includes methods to:

- send email
- check inbox
- read a specific email
- delete a message

### `Inbox`
Manages a list of email objects and provides functionality to:

- receive a new email
- list emails
- read an email by index
- delete an email by index

## Example Usage

```python
tory = User('Tory')
ramy = User('Ramy')

tory.send_email(ramy, 'Hello', 'Hi Ramy, just saying hello!')
ramy.check_inbox()
ramy.read_email(1)
```

## Run the Project

From the project folder:

```bash
python main.py
```

## What the Program Does

When executed, it creates two users, sends a couple of emails between them, displays the inbox, reads the first email, deletes it, and then prints the inbox again.

## Notes

This project is a simple console-based simulation intended to practice class design, object relationships, and basic inbox behavior in Python.
