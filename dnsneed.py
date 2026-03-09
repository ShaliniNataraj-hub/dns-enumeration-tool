import dns.resolver
import dns.query
import dns.zone
import socket
import argparse

def dns_records(domain):

    record_types = ["A","MX","NS","TXT"]

    for r in record_types:

        try:
            answers = dns.resolver.resolve(domain,r)

            print(f"\n{r} Records:")

            for data in answers:
                print(data)

        except:
            print(f"{r} record not found")


def subdomain_enum(domain,wordlist):

    print("\nSubdomain Enumeration")

    with open(wordlist) as file:

        for sub in file:

            sub = sub.strip()
            target = sub + "." + domain

            try:

                ip = socket.gethostbyname(target)

                print(target,"->",ip)

            except:
                pass


def zone_transfer(domain):

    print("\nAttempting Zone Transfer")

    try:

        ns_records = dns.resolver.resolve(domain,'NS')

        for ns in ns_records:

            ns = str(ns.target)

            try:

                zone = dns.zone.from_xfr(dns.query.xfr(ns,domain))

                print("Zone Transfer Successful from",ns)

                for host in zone.nodes.keys():
                    print(host)

            except:

                print("Zone transfer failed for",ns)

    except:

        print("Could not retrieve name servers")


def port_scan(domain):

    print("\nPort Scan")

    ip = socket.gethostbyname(domain)

    ports = [21,22,25,53,80,110,443]

    for port in ports:

        s = socket.socket()
        s.settimeout(1)

        if s.connect_ex((ip,port)) == 0:

            print("Port",port,"OPEN")

        s.close()


parser = argparse.ArgumentParser()

parser.add_argument("-d","--domain",required=True)
parser.add_argument("--dns",action="store_true")
parser.add_argument("--sub",action="store_true")
parser.add_argument("--zone",action="store_true")
parser.add_argument("--scan",action="store_true")

args = parser.parse_args()

domain = args.domain

if args.dns:
    dns_records(domain)

if args.sub:
    subdomain_enum(domain,"wordlist.txt")

if args.zone:
    zone_transfer(domain)

if args.scan:
    port_scan(domain)