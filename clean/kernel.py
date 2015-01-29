import subprocess

#DISABLE ALL THE THINGS!
#=====================
#not exactly sure what these do
subprocess.call("sysctl kernel.randomize_va_space=1".split())
subprocess.call("sysctl net.ipv4.conf.all.rp_filter=1".split())
subprocess.call("sysctl net.ipv4.conf.all.accept_source_route=0".split())

subprocess.call("sysctl net.ipv4.icmp_echo_ignore_broadcasts=1".split())
subprocess.call("sysctl net.ipv4.conf.all.log_martians=1".split())
subprocess.call("sysctl net.ipv4.conf.default.log_martians=1".split())

subprocess.call("sysctl -w net.ipv4.conf.all.accept_redirects=0".split())
subprocess.call("sysctl -w net.ipv6.conf.all.accept_redirects=0".split())
subprocess.call("sysctl -w net.ipv4.conf.all.send_redirects=0".split())
subprocess.call("sysctl kernel.sysrq=0".split())

subprocess.call("sysctl net.ipv4.tcp_timestamps=0".split())
subprocess.call("sysctl net.ipv4.tcp_syncookies=1".split())
subprocess.call("sysctl net.ipv4.icmp_ignore_bogus_error_responses=1".split())
subprocess.call("sysctl -p".split())

print "done!"
