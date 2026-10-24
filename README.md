# h07x User Scrape

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=171717&height=160&section=header&text=h07x%20User%20Scrape&fontSize=38&fontColor=ffffff" width="100%" alt="h07x User Scrape">
</p><p align="center">
  <b>GitHub Profile Information Tool</b>
  <br>
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

Overview

h07x User Scrape is a Python-based command-line tool for retrieving publicly available information from GitHub user profiles.

The tool is designed to run in Termux and other Python-compatible environments.

Features

Depending on the current implementation, profile information may include:

- Username and profile URL
- Public biography and location
- Followers and following counts
- Public repository and Gist counts
- Account creation date
- Website and other profile information

Requirements

Dependency| Purpose
Python 3| Runtime environment
"requests"| HTTP requests to the GitHub API
Git| Clone and update the repository

"requests" is the Python package imported by the script. Git is only required for cloning or updating the project.

Installation

Termux

Update the package index and install the required tools:

pkg update
pkg install python git

Clone the repository:

git clone https://github.com/h07x/h07x-UserScrape.git
cd h07x-UserScrape

Install the Python dependency:

python -m pip install requests

Usage

Run the main script:

python h07x-UserScrape-Tool.py

Follow the interactive prompts displayed in the terminal.

Dependency Management

To check the installed version of "requests":

python -m pip show requests

To verify that Python can import it:

python -c "import requests; print(requests.__version__)"

If the import fails, install the dependency again:

python -m pip install requests

Troubleshooting

"ModuleNotFoundError: No module named 'requests'"

Install the missing dependency using the same Python interpreter that runs the script:

python -m pip install requests

Python version

Check the installed version:

python --version

Inspect the project files

ls -la

If additional modules are imported by the script, install their packages as required. Only dependencies confirmed by the source code should be added to the requirements list.

Repository

<p align="center">
  <a href="https://github.com/h07x/h07x-UserScrape">
    <img src="https://img.shields.io/badge/View%20Source-Code-8A2BE2?style=for-the-badge&logo=github" alt="View source code">
  </a>
</p>- Source: "h07x-UserScrape" (https://github.com/h07x/h07x-UserScrape)
- Main script: "h07x-UserScrape-Tool.py" (https://github.com/h07x/h07x-UserScrape/blob/main/h07x-UserScrape-Tool.py)
- API documentation: "GitHub REST API" (https://docs.github.com/en/rest)

Connect

<p align="center">
  <a href="https://www.instagram.com/https.not.viv/">
    <img src="https://img.shields.io/badge/Instagram-Profile-E4405F?style=flat-square&logo=instagram&logoColor=white" alt="Instagram">
  </a>
  <a href="https://discord.gg/tQ4mZstsxA">
    <img src="https://img.shields.io/badge/Discord-Community-5865F2?style=flat-square&logo=discord&logoColor=white" alt="Discord">
  </a>
</p>Disclaimer

This project is intended for working with publicly available GitHub information. Respect user privacy and GitHub API rate limits. Do not use the tool to attempt unauthorized access.

---

<p align="center">
  <sub>Developed by h07x</sub>
</p>