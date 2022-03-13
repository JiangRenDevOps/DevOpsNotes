## CIDR - IPv4

stands for Classless Inter-Domain Routing -> help to define an IP range -> base IP/Subnet Mask

-> e.g. 10.0.0.0/24

subnet maks defines how many bits can change in the IP, what does it mean?

basically how many IP address in the range. For example,

- **/32 allows for 1 IP = 2^0**
- /31 allowsfor 2IP     = 2^1
- /30allowsfor  4IP     =2^2
- /29allowsfor  8IP     =2^3
- /28allowsfor  16IP    =2^4
- /27allowsfor  32IP    =2^5
- /26allowsfor  64IP    =2^6
- /25allowsfor  128IP   =2^7
- **/24         256IP    =2^8**
- **/16         65,536IP =2^16** the largest IPs available
- **/0          allIPs=2^32**

The max CIDR in AWS is /16

192.168.0.0/24= ..? -> the last two number can change

a tool to check https://www.ipaddressguide.com/cidr


### private IP allowed ranges

Private IP can only allow certain values
- 10.0.0.0 – 10.255.255.255 (10.0.0.0/8) <= in big networks
- 172.16.0.0 – 172.31.255.255 (172.16.0.0/12) <= default AWS one
- 192.168.0.0 – 192.168.255.255 (192.168.0.0/16) <= example: home networks

- All the rest of the IP on the internet are public IP
