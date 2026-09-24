# Login Attempt Monitor

A Python tool that simulates login monitoring and detects brute force attacks by locking accounts after too many failed attempts.

## What it does
- Tracks failed login attempts per username
- Alerts when an account exceeds the maximum allowed attempts
- Locks the account to prevent further access
- Resets the counter on successful login
- Treats `Admin` and `admin` as the same account, and remembers the lock after the program closes

The demo password is `SecurePass123!`. It is not printed when the program starts.

Broken and improved with Grok Build. Changing capitalization used to open a fresh set of attempts.

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
Access denied. Incorrect password. 0 attempt(s) remaining.
ALERT: Account 'admin' has been locked after 3 failed attempts.

Enter username: Admin
Enter password: wrongpassword
ALERT: Account 'Admin' is locked due to too many failed attempts.
```
