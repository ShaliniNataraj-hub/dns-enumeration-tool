<!DOCTYPE html>
<html>
<head>
</head>

<body>

<h1>DNS Enumeration Tool</h1>

<h2>Project Overview</h2>
<p>
This project is a DNS Enumeration Command Line Interface (CLI) tool developed using
Python. It helps security researchers, penetration testers, and network administrators
gather DNS information about a target domain. The tool retrieves DNS records,
performs subdomain discovery, attempts DNS zone transfers, and conducts basic
port scanning.
</p>

<h2>Description</h2>
<p>
The DNS Enumeration Tool allows users to analyze DNS configurations of a target
domain efficiently. By entering a domain name, the tool performs multiple
reconnaissance tasks such as retrieving DNS records, discovering subdomains using
a wordlist, scanning common network ports, and testing for zone transfer
vulnerabilities.
</p>

<h2>Folder Structure</h2>
<pre>
dns-enumeration-tool/
├── dnsneed.py
├── wordlist.txt
├── requirements.txt
└── README.md
</pre>

<h2>Packages and Modules</h2>
<ul>
<li><b>dnspython:</b> Used for querying DNS records and performing DNS operations.</li>
<li><b>socket:</b> Used for resolving hostnames and basic port scanning.</li>
<li><b>argparse:</b> Used for command-line argument handling.</li>
<li><b>colorama:</b> Used for colored terminal output.</li>
</ul>

<h2>Requirements</h2>
<p>
To run this project, Python must be installed on your system. Install the required
dependencies listed in the <code>requirements.txt</code> file before execution.
</p>

<h2>Configuration</h2>
<p>
The project uses a wordlist file for subdomain enumeration. You can edit the
<code>wordlist.txt</code> file and add subdomain names such as:
</p>

<pre>
www
mail
ftp
api
dev
test
admin
portal
support
blog
</pre>

<h2>Installation</h2>
<ol>
<li>Clone the repository:</li>
</ol>

<pre><code>git clone https://github.com/yourusername/dns-enumeration-tool.git</code></pre>

<ol start="2">
<li>Navigate to the project directory:</li>
</ol>

<pre><code>cd dns-enumeration-tool</code></pre>

<ol start="3">
<li>Install dependencies:</li>
</ol>

<pre><code>pip install -r requirements.txt</code></pre>

<h2>How to Run</h2>
<p>Run DNS record lookup:</p>
<pre><code>python dnsneed.py -d example.com --dns</code></pre>

<p>Run subdomain enumeration:</p>
<pre><code>python dnsneed.py -d example.com --sub</code></pre>

<p>Run port scanning:</p>
<pre><code>python dnsneed.py -d example.com --scan</code></pre>

<p>Attempt DNS zone transfer:</p>
<pre><code>python dnsneed.py -d zonetransfer.me --zone</code></pre>

<p>Run multiple modules together:</p>
<pre><code>python dnsneed.py -d example.com --dns --sub --scan</code></pre>

<h2>Example Output</h2>
<pre>
A Records:
104.18.27.120
104.18.26.120

MX Records:
0 .

NS Records:
hera.ns.cloudflare.com.
elliott.ns.cloudflare.com.

TXT Records:
"v=spf1 -all"

Subdomain Enumeration
www.example.com -> 104.18.26.120

Port Scan
Port 80 OPEN
Port 443 OPEN
</pre>

<h2>Author</h2>
<p><b>Shalini N</b></p>

<hr>

<p align="center">Made by Shalini N</p>

</body>
</html>
