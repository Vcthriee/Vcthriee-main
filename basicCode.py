

import  dns.resolver

target_domain = 'youtube.com'
records_list = ['A','AAAA','CNAME','MX','TXT','SOA']

resolver = dns.resolver.Resolver()
for record_list in records_list:
    try:
        answer = resolver.resolve(target_domain, records_list)
    except dns.resolver.NoAnswer:
        continue

    print(f'{records_list} records for {target_domain}')
    for data in answer:
        print(f'{data}')  


#ai code
#import dns.resolver
#
#def dns_resolver(domain, record_type):
 #   resolver = dns.resolver.Resolver()
 #   try:
 #       answer = resolver.resolve(domain, record_type)
 #       for rdata in answer:
 #           print(f"{record_type} record: {rdata.to_text()}")
 #   except dns.resolver.NoAnswer:
 #       print(f"No {record_type} records found for {domain}")
 #   except dns.resolver.NXDOMAIN:
 #       print(f"{domain} does not exist")

#domain = ('bravort.com')
#record_types = ['A', 'AAAA', 'NS', 'MX', 'SOA', 'TXT']
#
#for record_type in record_types:
 #   dns_resolver(domain, record_type)
#    
#dns_resolver()