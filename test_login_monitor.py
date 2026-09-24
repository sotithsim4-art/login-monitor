import unittest

import login_monitor


class LoginMonitorTests(unittest.TestCase):
    def test_case_and_spaces_do_not_bypass_a_lock(self):
        attempts = {}
        for _ in range(3):
            login_monitor.login("admin", "nope", attempts)
        login_monitor.login("Admin", "nope", attempts)
        login_monitor.login(" admin ", "nope", attempts)
        self.assertEqual(attempts, {"admin": 3})

    def test_success_clears_only_that_account(self):
        attempts = {"admin": 2, "other": 1}
        login_monitor.login("Admin", login_monitor.DEMO_PASSWORD, attempts)
        self.assertEqual(attempts["admin"], 0)
        self.assertEqual(attempts["other"], 1)

    def test_blank_username_is_ignored(self):
        attempts = {}
        login_monitor.login("   ", "nope", attempts)
        login_monitor.login(None, "nope", attempts)
        self.assertEqual(attempts, {})


if __name__ == "__main__":
    unittest.main()
