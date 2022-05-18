# Description

This is to demo how to install Jenkins via Kubernetes Application

## Pre-requisite

- Google Cloud Platform account
- A Kubernete cluster (Ref: <https://github.com/JiangRenDevOps/DevOpsLectureNotes/blob/master/WK5-Kubernetes-GKE-CMS/2.GKE1.md>)

## Steps

### Step 1: Open GKE Application Tab
<https://console.cloud.google.com/kubernetes/application>

![Alt text](images/jenkins-installation-via-kubernetes-application-01.png?raw=true)

### Step 2: Click "Deploy from Marketspace" and search for Jenkins

![Alt text](images/jenkins-installation-via-kubernetes-application-02.png?raw=true)

### Step 3: Choose Jenkins and "Configure"

![Alt text](images/jenkins-installation-via-kubernetes-application-03.png?raw=true)

### Step 4: Deploy to the cluster

![Alt text](images/jenkins-installation-via-kubernetes-application-04.png?raw=true)

### Step 5: Wait util the application is deployed

![Alt text](images/jenkins-installation-via-kubernetes-application-05.png?raw=true)

### Step 6: You should see this screen when it's deployed

![Alt text](images/jenkins-installation-via-kubernetes-application-06.png?raw=true)

### Step 7: Open "Jenkins HTTP address" from the step above

You should see a screen to ask for "Adminstration password".
![Alt text](images/jenkins-installation-via-kubernetes-application-07.png?raw=true)

### Step 8: Go to GKE cluster tab and click "connect" button

![Alt text](images/jenkins-installation-via-kubernetes-application-08.png?raw=true)

### Step 9: Click "Run in Cloud Shell"

![Alt text](images/jenkins-installation-via-kubernetes-application-09.png?raw=true)

### Step 10: Get Initial Admin Password

Run below command to get password

```bash
kubectl exec jenkins-1-jenkins-0 cat /var/jenkins_home/secrets/initialAdminPassword
```

![Alt text](images/jenkins-installation-via-kubernetes-application-10.png?raw=true)

### Step 11: Use the password above to login to Jenkins

![Alt text](images/jenkins-installation-via-kubernetes-application-11.png?raw=true)

### Step 12: Choose suggested plugins or select plugins to install up to you

![Alt text](images/jenkins-installation-via-kubernetes-application-12.png?raw=true)

### Step 13: Wait a few minutes for plugins to get installed

![Alt text](images/jenkins-installation-via-kubernetes-application-13.png?raw=true)

### Step 14: Create your first admin user

![Alt text](images/jenkins-installation-via-kubernetes-application-14.png?raw=true)

### Step 15: Use the default instance configuration

![Alt text](images/jenkins-installation-via-kubernetes-application-15.png?raw=true)

### Step 16: Jenkins is ready

![Alt text](images/jenkins-installation-via-kubernetes-application-16.png?raw=true)

### Step 17: You should see this Jenkins screen

![Alt text](images/jenkins-installation-via-kubernetes-application-17.png?raw=true)
