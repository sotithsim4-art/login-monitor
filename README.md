# Login Attempt Monitor

A Python tool that simulates login monitoring and detects brute force attacks by locking accounts after too many failed attempts.

## What it does
- Tracks failed login attempts per username
- Alerts when an account exceeds the maximum allowed attempts
- Locks the account to prevent further access
- Resets the counter on successful login

## How to run

```
python login_monitor.py
```

## Example

```
Enter username: admin
Enter password: wrongpassword
Access denied. Incorrect password. 2 attempt(s) remaining.

Enter username: admin
Enter password: wrongpassword
Access denied. Incorrect password. 1 attempt(s) remaining.

Enter username: admin
Enter password: wrongpassword
ALERT: Account 'admin' has been locked after 3 failed attempts.
```
