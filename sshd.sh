#! /bin/bash
# This script changes the ssh port for logins on CentOS 5 and 6
if [[ $EUID -ne 0 ]]; then
	echo "This script must be run as root"
	exit 2
fi
	
read -p "What would you like to change the port to? (Chose between 1024-65535) " sshportconfig
if (( ("$sshportconfig" > 1024) && ("$sshportconfig" < 65535) )); then
	cat >> /etc/ssh/sshd_config << EOL
Port $sshportconfig
PermitRootLogin no
AllowUsers ahmed
EOL
semanage port -a -t ssh_port_t -p tcp $sshportconfig
semanage port -m -t ssh_port_t -p tcp $sshportconfig
systemctl restart sshd 
	echo "--------------------------------------------------------------------"
	echo "SSH port has been changed to: $sshportconfig and only only ahmed has sudo privilege"
	echo "--------------------------------------------------------------------"
netstat -tlpn| grep ssh
firewall-cmd --add-port=$sshportconfig/tcp
firewall-cmd --remove-service=ssh
firewall-cmd --runtime-to-permanent
firewall-cmd --reload 
else
	echo "Port chosen is incorrect."
	exit 1
fi

exit 0