<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>DNS Enumeration Tool</title>
  <style>
    body {
      margin: 0;
      padding: 40px;
      background-color: #0d1117;
      color: #f0f6fc;
      font-family: Arial, sans-serif;
      line-height: 1.8;
    }

    .container {
      max-width: 1000px;
      margin: auto;
    }

    h1, h2 {
      color: #ffffff;
      border-bottom: 1px solid #30363d;
      padding-bottom: 10px;
      margin-top: 40px;
    }

    p, li {
      font-size: 18px;
      color: #e6edf3;
    }

    pre {
      background-color: #161b22;
      color: #f8f8f2;
      padding: 20px;
      border-radius: 8px;
      overflow-x: auto;
      font-size: 17px;
    }

    code {
      font-family: Consolas, monospace;
    }

    ul {
      padding-left: 25px;
    }

    .author {
      text-align: center;
      margin-top: 50px;
      font-size: 20px;
    }

    .footer {
      text-align: center;
      margin-top: 30px;
      color: #c9d1d9;
      font-size: 18px;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>DNS Enumeration Tool</h1>

    <h2>Project Overview</h2>
    <p>
      This project is a DNS Enumeration Command Line Interface (CLI) tool developed using Python.
      It helps security researchers, penetration testers, and network administrators gather DNS
      information about a target domain. The tool retrieves DNS records, performs subdomain discovery,
      attempts DNS zone transfers, and conducts basic port scanning.
    </p>
    <p>
      The main objective of this project is to automate DNS reconnaissance and assist in identifying
      potential misconfigurations or security weaknesses in DNS infrastructure.
    </p>

    <h2>Description</h2>
    <p>
      The DNS Enumeration Tool allows users to analyze DNS configurations of a target domain efficiently.
      By entering a domain name, the tool performs multiple reconnaissance tasks such as retrieving DNS
      records, discovering subdomains using a wordlist, scanning common network ports, and testing for
      zone transfer vulnerabilities.
    </p>
    <p>
      This tool is useful during the information-gathering phase of penetration testing and network security analysis.
    </p>

    <h2>Features</h2>
    <ul>
      <li>DNS Record Lookup (A, MX, NS, TXT)</li>
      <li>Subdomain Enumeration using wordlists</li>
      <li>DNS Zone Transfer Testing</li>
      <li>Basic Port Scanning</li>
      <li>Simple Command Line Interface</li>
      <li>Lightweight and platform independent</li>
    </ul>

    <h2>Installation</h2>
    <p>Clone the repository:</p>
    <pre><code>git clone https://github.com/yourusername/dns-enumeration-tool.git
cd dns-enumeration-tool</code></pre>

    <p>Install dependencies:</p>
    <pre><code>pip install -r requirements.txt</code></pre>

    <h2>Usage</h2>
    <p>Run DNS record lookup:</p>
    <pre><code>python dnsneed.py -d example.com --dns</code></pre>

    <p>Run subdomain enumeration:</p>
    <pre><code>python dnsneed.py -d example.com --sub</code></pre>

    <p>Run port scanning:</p>
    <pre><code>python dnsneed.py -d example.com --scan</code></pre>

    <p>Attempt zone transfer:</p>
    <pre><code>python dnsneed.py -d zonetransfer.me --zone</code></pre>

    <p>Run all modules together:</p>
    <pre><code>python dnsneed.py -d example.com --dns --sub --scan</code></pre>

    <h2>Folder Structure</h2>
    <pre><code>dns-enumeration-tool/
│
├── dnsneed.py
├── wordlist.txt
├── requirements.txt
└── README.md</code></pre>

    <h2>Example Output</h2>
    <pre><code>A Records:
104.18.27.120
104.18.26.120

NS Records:
hera.ns.cloudflare.com
elliott.ns.cloudflare.com

Subdomain Enumeration
www.example.com -> 104.18.26.120

Port Scan
Port 80 OPEN
Port 443 OPEN</code></pre>

    <h2>Author</h2>
    <p><strong>Shalini N</strong></p>

    <div class="footer">
      Made  by SHALINI N
    </div>
  </div>
</body>
</html>
