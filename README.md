# h07x User Scrape

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=171717&height=160&section=header&text=h07x%20User%20Scrape&fontSize=38&fontColor=ffffff" width="100%" alt="h07x User Scrape">
</p><p align="center">
  <strong>GitHub Profile Information Tool</strong><br>
  Python · GitHub REST API · Termux
</p><p align="center">
  <a href="https://github.com/h07x/h07x-UserScrape">
    <img src="https://img.shields.io/badge/Repository-h07x--UserScrape-8A2BE2?style=flat-square&logo=github" alt="Repository">
  </a>
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
  </a>
  <a href="https://docs.github.com/en/rest">
    <img src="https://img.shields.io/badge/API-GitHub%20REST-181717?style=flat-square&logo=github" alt="GitHub REST API">
  </a>
</p>---

# Overview

h07x User Scrape is a Python command-line tool for retrieving publicly available information from GitHub profiles.

# Features

- Username and profile URL
- Public biography and location
- Followers and following counts
- Public repository and Gist counts
- Account creation date
- Website and profile information

Available features depend on the current implementation.

# Requirements

- Python 3
- "requests"
- Git (for cloning and updating the repository)
- Internet connection

# Installation

Termux

Install the required packages:

pkg update
pkg install python git

Clone the repository:

git clone https://github.com/h07x/h07x-UserScrape.git
cd h07x-UserScrape

Install the Python dependency:

python -m pip install requests

Usage

Run the script:

python h07x-UserScrape-Tool.py

Follow the instructions displayed in the terminal.

Dependency Management

Check the installed version of "requests":

python -m pip show requests

Verify that the module can be imported:

python -c "import requests; print(requests.__version__)"

To install dependencies from a requirements file, create "requirements.txt" with:

# requests

Then run:

python -m pip install -r requirements.txt

Troubleshooting

"ModuleNotFoundError: No module named 'requests'"

Install the missing module:

python -m pip install requests

Check your Python version

python --version

Inspect project files

ls -la

Links

<p align="center">
  <a href="https://github.com/h07x/h07x-UserScrape">
    <img src="https://img.shields.io/badge/Source%20Code-Repository-8A2BE2?style=for-the-badge&logo=github" alt="Source code">
  </a>
  <a href="https://github.com/h07x/h07x-UserScrape/blob/main/h07x-UserScrape-Tool.py">
    <img src="https://img.shields.io/badge/View-Python%20Script-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python script">
  </a>
</p><p align="center">
  <a href="https://www.instagram.com/https.not.viv/">
    <img src="https://img.shields.io/badge/Instagram-Profile-E4405F?style=flat-square&logo=instagram&logoColor=white" alt="Instagram">
  </a>
  <a href="https://discord.gg/tQ4mZstsxA">
    <img src="https://img.shields.io/badge/Discord-Community-5865F2?style=flat-square&logo=discord&logoColor=white" alt="Discord">
  </a>
</p>Disclaimer

This project is intended for retrieving publicly accessible GitHub information. Respect user privacy and GitHub API rate limits. Do not use the tool for unauthorized access.

---

<p align="center">
  <sub>Developed by h07x</sub>
</p>