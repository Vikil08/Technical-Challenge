def hostFilter(url):
	u_host = url.split("://")[1].split("/")[0]
	if u_host not in uniqueHosts.keys():
		uniqueHosts[u_host] = [url]
	else:
		uniqueHosts[u_host].append(url)

urls = set()
hosts = {'NoMatchFound': []}

uniqueHosts = {}

with open('hosts.txt') as hostsFile:
	for line in hostsFile:
		if len(line.strip())>0:
			hosts[line.strip()] = []

with open('urls.txt') as urlsFile:
	for line in urlsFile:
		if len(line.strip())>0:
			urls.add(line.strip())

urls = list(urls)
for url in urls:
	chk = False
	for host in hosts:
		if(host in url):
			chk = True
			hosts[host].append(url)
			break
	if(not chk):
		hosts['NoMatchFound'].append(url)
		hostFilter(url)

print()
print("The count of URLs that match to hostnames: {}".format(len(urls)-len(hosts["NoMatchFound"])))
print()
print("The count of URLs that don't match to hostname: {} ".format(len(hosts["NoMatchFound"])))
print()
for host in hosts.keys():
	print("{}:- {}".format(host,len(hosts[host])))
print()
print()
print("Unique hostnames of NoMatchFound: ")
for host in uniqueHosts: 
	print("{} :- {}".format(host, len(uniqueHosts[host]))) 




