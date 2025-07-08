# Credential Brute-Force Attack Simulation Tool (Python)

This is a Python-based tool that simulates credential brute-force attacks against a test login page. It was designed for educational and learning purposes, implementing features that mirror real-world attacker behavior, including logging, response analysis, and rate limiting detection.

---

## 🛠 Features

- 🔁 Iterates through multiple usernames and passwords
- 🧠 Detects success via response pattern matching
- 🚦 Handles HTTP status codes including rate limiting (429)
- 📄 Logs all attempts with timestamps and outcomes
- 🎨 Color-coded terminal output for easy reading
- 🧪 Designed to test and practice brute-force detection on local test applications

---

## 📂 Project Structure

├── web-brute.py # Main brute-force script
├── top-100.txt # Password list
├── brute_attempts.log # Logged attempts
└── README.md # This file

---

## 🚀 Getting Started

### 📦 Requirements

- Python 3.7+
- Install dependencies:

```bash
pip install requests termcolor
▶️ Running the Tool
Run a local web app on http://127.0.0.1:5000 with a login form
(You can use a Flask app with username/password fields for testing.)

Place your password list in top-100.txt

Run the script:

python3 web-brute.py

💡 Learning Reflection
This project started as a simple credential brute-force tester. With AI assistance, I enhanced it by adding advanced features such as:

Color-coded output for better UX

Full logging with timestamps

Response handling for rate limiting (HTTP 429)

These additions improved both the tool's realism and my understanding of web application security and scripting techniques.

⚠️ Disclaimer
This tool is intended for ethical and educational purposes only.
Use only on systems you own or are explicitly authorized to test.

🧠 Key Skills Demonstrated
Web application security testing

HTTP request/response handling

Automation scripting and logging

Rate limiting detection

Terminal UX (CLI design and readability)

📜 License
MIT License
