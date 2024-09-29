import dns.resolver
import whois
import sublist3r
import requests

# Helper function to get geolocation from IP addresses
def get_ip_geolocation(ip):
    """Fetch geolocation data for the IP address using ipinfo.io API."""
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        if response.status_code == 200:
            data = response.json()
            return {
                'IP': ip,
                'City': data.get('city'),
                'Region': data.get('region'),
                'Country': data.get('country'),
                'Org': data.get('org'),
                'Loc': data.get('loc'),  # Latitude and Longitude
            }
        else:
            return {'IP': ip, 'Error': 'Unable to fetch geolocation data'}
    except Exception as e:
        return {'IP': ip, 'Error': str(e)}

# Main lookup function to perform DNS, WHOIS, geolocation, and subdomain enumeration
def dns_whois_lookup(domain):
    """Retrieve DNS records, WHOIS information, IP geolocation, and subdomains."""
    dns_info = {}
    whois_info = None
    ip_geolocation = []
    subdomains = []

    # Helper function to limit string length
    def limit_string(s, max_length=1000):
        return s[:max_length] + '...' if len(s) > max_length else s

    # Function to resolve DNS records and handle errors
    def resolve_dns_record(record_type):
        try:
            answers = dns.resolver.resolve(domain, record_type)
            return [answer.to_text() for answer in answers]
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
            return f'No {record_type} records found'
        except Exception as e:
            return f'Error resolving {record_type} records: {str(e)}'

    try:
        # Resolve DNS records (A, AAAA, MX, NS, TXT)
        for record_type in ['A', 'AAAA', 'MX', 'NS', 'TXT']:
            dns_info[record_type] = resolve_dns_record(record_type)

        # If A records are present, perform IP geolocation lookup
        if isinstance(dns_info['A'], list):
            ip_geolocation = [get_ip_geolocation(ip) for ip in dns_info['A']]

        # Perform WHOIS lookup
        try:
            whois_info = whois.whois(domain)
        except Exception as e:
            whois_info = f"Error in WHOIS lookup: {str(e)}"

        # Perform subdomain enumeration
        try:
            subdomains = sublist3r.main(domain, 40, None, ports=None, silent=True, verbose=False, enable_bruteforce=False, engines=None)
        except Exception as e:
            subdomains = [f"Error enumerating subdomains: {str(e)}"]

        # Limit length of returned data
        dns_info = {k: limit_string(str(v)) for k, v in dns_info.items()}
        ip_geolocation = [{k: limit_string(str(v)) for k, v in geo.items()} for geo in ip_geolocation]
        subdomains = [limit_string(sub) for sub in subdomains[:100]]  # Limit number and length of subdomains

        return dns_info, whois_info, ip_geolocation, subdomains

    except Exception as e:
        # Handle any other exceptions
        return f"Error: {str(e)}", whois_info, ip_geolocation, subdomains

# Main function for user interaction
def main():
    print("Domain Lookup Utility")
    domain = input("Enter the domain name (e.g., example.com): ")

    # Perform the lookup
    try:
        dns_info, whois_info, ip_geolocation, subdomains = dns_whois_lookup(domain)

        # Display DNS records
        print("\nDNS Information:")
        for record_type, records in dns_info.items():
            print(f"{record_type} Records: {records}")

        # Display WHOIS information
        print("\nWHOIS Information:")
        print(whois_info)

        # Display IP geolocation
        print("\nIP Geolocation Information:")
        for geo in ip_geolocation:
            print(geo)

        # Display subdomains
        print("\nSubdomains:")
        for subdomain in subdomains:
            print(subdomain)

    except Exception as e:
        print(f"An error occurred during the lookup: {str(e)}")

if __name__ == "__main__":
    main()
