# Advanced Domain Lookup

This Python terminal-based utility allows users to perform domain lookups, retrieving DNS records, WHOIS information, IP geolocation, and subdomains. It leverages the `dns.resolver`, `whois`, and `sublist3r` libraries, providing streamlined information for cybersecurity professionals and enthusiasts.

- **👉 Checkout some more awesome tools at [GetCyber](https://getcyber.me/tools)**
- **👉 Subscribe to my YouTube Channel [GetCyber - YouTube](https://youtube.com/getCyber)**
- **👉 Discord Server [GetCyber - Discord](https://discord.gg/YUf3VpDeNH)**

## Features

- DNS Record Retrieval (A, AAAA, MX, NS, TXT)
- WHOIS Information
- IP Geolocation from `ipinfo.io`
- Subdomain Enumeration using Sublist3r

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Dan-Duran/Advanced-Domain-Lookup.git
   cd Advanced-Domain-Lookup
   ```

2. **Create a virtual environment:**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the utility, simply execute the Python script:

```bash
python domain_lookup.py
```

You will be prompted to enter a domain name, and the tool will output DNS records, WHOIS information, IP geolocation data, and a list of subdomains.

Example:

```bash
Enter the domain name (e.g., example.com): example.com
```

## Dependencies

- `dnspython`: For DNS record resolution
- `python-whois`: For WHOIS queries
- `sublist3r`: For subdomain enumeration
- `requests`: For fetching IP geolocation data from `ipinfo.io`

You can install these dependencies using the `requirements.txt` file provided.

## License

This project is licensed under the [MIT License](LICENSE).

## Disclaimer

This software is provided for educational and informational purposes only. The developer assumes no responsibility for the consequences of its use. Use this tool responsibly and in compliance with all applicable laws. The information retrieved by this tool should not be used for malicious purposes or any activities that may cause harm to any entities.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
