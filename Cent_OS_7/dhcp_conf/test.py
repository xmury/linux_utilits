print ("Hello. This is dhcp configuer. Let's go!")

subnet = input("subnet id: ")
mask = input("subnet mask: ")

range_begin = input("range begin: ")
range_end = input("range end:   ")

domain_servers = input("domain servers (1 or 2, across ' '):")
domain_name = input("domain name: ")

def_lease_time = input("default lease time : ")
max_lease_time = input("max lease time     : ")