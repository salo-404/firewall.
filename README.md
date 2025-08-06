🛡️ Spring4Shell Firewall Defense – Cybersecurity Incident Simulation
This project is part of a Cybersecurity Job Simulation I completed through Forage in August 2025. It simulates a real-world incident involving the Spring4Shell (CVE-2022-22965) vulnerability and demonstrates how a custom firewall can detect and mitigate exploitation attempts.

📌 Project Overview
The goal of this simulation was to identify and block malicious traffic targeting a vulnerable web application endpoint. I developed a custom Python-based HTTP firewall that monitors and filters incoming requests, detecting known exploit patterns and stopping them in real time.

🧰 Key Features
🔍 Threat Detection: Analyzes HTTP POST data for suspicious keys and payloads.

🔐 Firewall Defense: Blocks malicious requests using pattern-based rules.

💣 Exploit Prevention: Detects attempted remote code execution via Runtime.getRuntime() and similar signatures.

📈 Logging & Monitoring: Displays blocked attempts and reasons for blocking in the terminal.





🖼️ Demo
In the first screenshot, a suspicious POST request attempts to exploit the Spring4Shell vulnerability by injecting a payload with Runtime.getRuntime(). The custom firewall immediately detects this pattern and blocks the request, returning a 403 Forbidden response — effectively stopping a potential Remote Code Execution (RCE) attempt.

![noRMAL REQUEST ](https://github.com/user-attachments/assets/f087506f-6272-494b-bc2b-d97021a2d04b)



In contrast, the second screenshot shows a safe POST request with harmless data (username=test) sent to the server. The firewall recognizes it as safe and allows the request to pass through, returning a standard 200 OK response. This highlights the firewall’s ability to distinguish between normal and malicious activity with precision.
![Sus request](https://github.com/user-attachments/assets/fa01328b-fdca-4a75-91e8-ed7e0c473310)



🧪 Technologies Used
Python (firewall implementation)

http.server module for simulating vulnerable server

curl for simulating POST requests

Custom signature detection logic

📋 What I Did
Analyzed a simulated Spring4Shell attack targeting a JSP endpoint.

Identified suspicious payloads in POST data.

Wrote a custom firewall (firewall_server.py) to detect and block malicious requests.

Validated the firewall by simulating attacks (see screenshot).

Documented the incident with a detailed postmortem analysis.


📜 Certificate
[RNhbu8QnDzthwynEf_M6JGAwZ52SMusMEcK_cKqCaSyzkPoWXRdg5_1754434963290_completion_certificate.pdf](https://github.com/user-attachments/files/21616808/RNhbu8QnDzthwynEf_M6JGAwZ52SMusMEcK_cKqCaSyzkPoWXRdg5_1754434963290_completion_certificate.pdf)


