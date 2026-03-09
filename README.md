DNS Enumeration Tool

A Python-based Command Line Interface (CLI) tool designed to perform DNS enumeration and basic network reconnaissance. The tool gathers DNS records, discovers subdomains, performs basic port scanning, and tests for DNS zone transfer vulnerabilities.

Features

DNS record lookup (A, MX, NS, TXT)

Subdomain enumeration using a wordlist

DNS zone transfer testing

Basic port scanning

Simple command-line interface

Lightweight and easy to use

Technologies Used

Python

dnspython

socket

argparse

colorama

Installation

Clone the repository:

git clone https://github.com/yourusername/dns-enumeration-tool.git
cd dns-enumeration-tool

Install required dependencies:

pip install -r requirements.txt
Usage
DNS Records Lookup
python dnsneed.py -d example.com --dns
Subdomain Enumeration
python dnsneed.py -d example.com --sub
Port Scanning
python dnsneed.py -d example.com --scan
Zone Transfer Test
python dnsneed.py -d zonetransfer.me --zone
Run All Modules
python dnsneed.py -d example.com --dns --sub --scan
Example Output
A Records:
104.18.27.120
104.18.26.120

NS Records:
hera.ns.cloudflare.com
elliott.ns.cloudflare.com

Subdomain Enumeration
www.example.com -> 104.18.26.120

Port Scan
Port 80 OPEN
Port 443 OPEN
Project Structure
dns-enumeration-tool
│
├── dnsneed.py
├── wordlist.txt
├── requirements.txt
└── README.md
