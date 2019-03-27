# BP
Prerequisites:
Clean installation of Centos 7 (on virt-manager)

1. Update + tools
# yum update -y
# yum install -y wget git

2. Install docker
# yum install docker

3.Install oc client tools
 Download OpenShift Origin package
# wget https://github.com/openshift/origin/releases/download/v3.9.0/openshift-origin-client-tools-v3.9.0-191fece-linux-64bit.tar.gz 

4. Extract
# tar -zvxf openshift-origin-client-tools-v3.9.0-191fece-linux-64bit.tar.gz

5. Prepare
# cd openshift-origin-client-tools-v3.9.0-191fece-linux-64bit
# sudo cp oc /usr/local/bin/

6. Add insecure registry to docker daemon
sudo su -
cat << EOF > /etc/docker/daemon.json 
{
    "insecure-registries" : [ "172.30.0.0/16" ]
}
EOF

7. Reload and restart
# systemctl daemon-reload
# systemctl restart docker

8. Firewalld (port 5000 for app)
# firewall-cmd --permanent --add-port 8443/tcp --add-port 53/udp --add-port 5000/tcp
# firewall-cmd --reload

9. Start cluster
# oc cluster up

10. Login to oc
oc login -u system:admin

11. Deploy my app from https://github.com/jusis707/bp (Dockerfile)
# oc new-app https://github.com/jusis707/bp --name=bp

12. Mount persistent volume
# oc volume dc/bp --add --mount-path /mnt --name testvolume

13. Expose service 
# oc expose svc/bp

14. Check (in my case bp-2-hh8mc)
# oc get pod | grep bp

15. Check (in my case bp-myproject.127.0.0.1.nip.io)
# oc get route bp

16. Check running app ( /hello)

curl bp-myproject.127.0.0.1.nip.io/hello

17. Check
# oc get pvc

18. Check
# oc volume dc --all

19. Check
# oc get pods

20. Check persistant storage and timestamped file for update, updates every 10 secconds
# oc rsh bp-2-hh8mc ls -las /mnt
# oc rsh bp-2-hh8mc cat /mnt/stamp.txt

21. Check if app is running via Ansible
file bp1.yaml



