import subprocess

print "Cyberpatriot script starting..."

#REMOVE NFS
#=====================
subprocess.call("apt-get --yes purge nfs-kernel-server nfs-common portmap rpcbind autofs".split())