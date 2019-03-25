# bp
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
8. Firewalld (port 8000 for app)
# firewall-cmd --permanent --add-port 8443/tcp --add-port 53/udp --add-port 8000/tcp
# firewall-cmd --reload
9. Start cluster
# oc cluster up
10. Login to oc
oc login -u system:admin
11. Deploy my app via hub.docker.com -> https://github.com/jusis707/bp Dockerfile
# oc new-app --docker-image=jusis707/bp --name=bp
12. Expose service 
# oc expose svc/bp
13.
# oc get pod | grep bp
14.
# oc get route bp
15. Check running app
curl http://hello-world-myproject.127.0.0.1.nip.io 8000
16. Mount persistent volume
# oc volume dc/hello-world --add --claim-size 100M --mount-path /mnt --name testvolume
17.
# oc get pvc
18.
# oc volume dc --all
19.
# oc get pods
20.
# oc rsh bp-3-hzdtj
21. Check /mnt 
# oc rsh bp-3-hzdtj ls -las /mnt
