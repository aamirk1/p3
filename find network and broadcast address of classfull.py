ip = input("Enter IP: ")
ipsplit = ip.split(".")

ipfirst = ipsplit[0]
ipsecond = ipsplit[1]
ipthird = ipsplit[2]
ipforth = ipsplit[3]

int_ip = int(ipfirst)

if int_ip>=0 and int_ip <=127:
    print("Class Of IP: Class A")
    print("Subnet Mask: 255.0.0.0")
    NetworkAdd = ipfirst + "."+ "0.0.0"
    print("Network Address: ",NetworkAdd)
    BroadcastAdd = ipfirst + "."+ "255.255.255"
    print("Broadcast Network: ",BroadcastAdd)
    totalhostbit = 3*8
    print("Total no of Host Bit: ",totalhostbit)
    noOfHost = (pow(2,totalhostbit)-2)
    print("Number Of Host: ",noOfHost)

elif int_ip>=128 and int_ip <=191:
    print("Class Of IP: Class B")
    print("Subnet Mask: 255.255.0.0")
    NetworkAdd = ipfirst + "."+ipsecond+".0.0"
    print("Network Address: ",NetworkAdd)
    BroadcastAdd = ipfirst + "."+ipsecond+".255.255"
    print("Broadcast Network: ",BroadcastAdd)
    totalhostbit = 2*8
    print("Total no of Host Bit: ",totalhostbit)
    noOfHost = (pow(2,totalhostbit)-2)
    print("Number Of Host: ",noOfHost)

elif int_ip>=192 and int_ip <=223:
    print("Class Of IP: Class C")
    print("Subnet Mask: 255.255.255.0")
    NetworkAdd = ipfirst + "."+ipsecond + "."+ipthird + ".0"
    print("Network Address: ",NetworkAdd)
    BroadcastAdd = ipfirst + "."+ipsecond + "."+ipthird + ".255"
    print("Broadcast Network: ",BroadcastAdd)
    totalhostbit = 1*8
    print("Total no of Host Bit: ",totalhostbit)
    noOfHost = (pow(2,totalhostbit)-2)
    print("Number Of Host: ",noOfHost)
    
elif int_ip>=224 and int_ip <=239:
    print("Class Of IP: Class D")
elif int_ip>=240 and int_ip <=255:
    print("Class Of IP: Class E")
else:
    print("Invalid IP Address")
    