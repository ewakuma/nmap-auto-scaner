import nmap
import os

def run_nmap_scan(server_address, nmap_args):
    nm = nmap.PortScanner()
    nm.scan(hosts=server_address, arguments=nmap_args)

    if os.path.exists('nmap_result.txt'):
        with open('nmap_result.txt', 'r') as f:
            old_result = f.read().splitlines()
    else:
        old_result = []

    with open('nmap_report.txt', 'r') as f:
        new_result = f.read().splitlines()

    with open('nmap_result.txt', 'w') as f:
        f.write('\n'.join(new_result))

    critical_changes = set()
    for port in set(new_result).difference(set(old_result)):
        if 'open' in port:
            critical_changes.add(port)

    return critical_changes, old_result, new_result
