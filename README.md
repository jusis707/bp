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

7. systemctl daemon-reload and # systemctl restart docker
8. Firewalld
--- firewall-cmd --permanent --add-port 8443/tcp --add-port 53/udp --add-port 8000/tcp
--- firewall-cmd --reload
9. STart cluster
# oc cluster up
10. Login to oc
oc login -u system:admin
11. Deploy my app via hub.docker.com -> https://github.com/jusis707/bp Dockerfile
# oc new-app --docker-image=jusis707/bp --name=bp
12. Expose service 
# oc expose svc/bp
oc get pod | grep bp
oc get route bp
Check running app
curl http://hello-world-myproject.127.0.0.1.nip.io
???oc volume dc/hello-world --add --claim-size 100M --mount-path /mnt --name testvolume
oc get pvc
oc volume dc --all
oc get pods

oc get pods
oc rsh bp-3-hzdtj

oc set volume dc/bp --add --name=tmp-mount --claim-name=data --type pvc --claim-size=20M --mount-path /mnt
oc rsh dummy-1-9j3p3 ls -las /mnt




