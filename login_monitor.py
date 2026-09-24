import hmac
import json
from pathlib import Path

MAX_ATTEMPTS = 3
DEMO_PASSWORD = "SecurePass123!"
ATTEMPTS_FILE = Path(__file__).with_name("login_attempts.json")


def normalize_username(username):
    if not isinstance(username, str):
        return ""
    return username.strip().casefold()


def passwords_match(given, expected):
    if not isinstance(given, str):
        return False
    return hmac.compare_digest(given.encode("utf-8"), expected.encode("utf-8"))


def load_attempts(path=ATTEMPTS_FILE):
    try:
        stored = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    if not isinstance(stored, dict):
        return {}
    attempts = {}
    for name, count in stored.items():
        if isinstance(name, str) and isinstance(count, int) and count >= 0:
            attempts[normalize_username(name)] = count
    return attempts


def save_attempts(attempts, path=ATTEMPTS_FILE):
    Path(path).write_text(json.dumps(attempts, indent=2), encoding="utf-8")


def login(username, password, attempts):
    name = normalize_username(username)
    if name == "":
        print("Enter a username.")
        return attempts

    display = username.strip()
    if attempts.get(name, 0) >= MAX_ATTEMPTS:
        print(f"ALERT: Account '{display}' is locked due to too many failed attempts.")
        return attempts

    if passwords_match(password, DEMO_PASSWORD):
        print(f"Access granted. Welcome, {display}!")
        attempts[name] = 0
        return attempts

    attempts[name] = attempts.get(name, 0) + 1
    remaining = MAX_ATTEMPTS - attempts[name]
    print(f"Access denied. Incorrect password. {remaining} attempt(s) remaining.")
    if attempts[name] >= MAX_ATTEMPTS:
        print(f"ALERT: Account '{display}' has been locked after {MAX_ATTEMPTS} failed attempts.")
    return attempts


if __name__ == "__main__":
    print("Login Monitor Demo")
    print("------------------")
    print("Failed attempts are saved and are not reset by changing capitalization.")
    print()
    attempts = load_attempts()
    while True:
        username = input("Enter username (or 'quit' to exit): ")
        if username.strip().casefold() == "quit":
            break
        password = input("Enter password: ")
        login(username, password, attempts)
        save_attempts(attempts)
        print()
