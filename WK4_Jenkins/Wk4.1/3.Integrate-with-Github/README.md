# Description

This is to demo how to integrate Jenkins with a Github Orgnisation

## Pre-requisite

- Github Account
- Jenkins Server
- Fork <https://github.com/JiangRenDevOps/hello-Jenkinsfile> into your github account.

## Task

### Step 1: Go to Jenkins Dashboard and click on the “New Item ” link to create a new job highlighted in the red rectangle

![Alt text](images/integrate-with-github-org-01.png?raw=true)

### Step 2: Now do the following steps further for a selection of project

![Alt text](images/6-Selection-of-Project.jpeg?raw=true)

### Step 3: Now just scroll down and go to the Source Code Management section. Now, select the “Git ” option

![Alt text](images/8-Jenkins-github-integration-Source-Code-Management-section-using-Git-Plugin.jpeg?raw=true)

### Step 4: Now enter the repository URL as shown in the below image

![Alt text](images/9-Jenkins-github-integration-Configure-GitHub-repository-in-Jenkins-Build.png?raw=true)

### Step 5:  Now, go to the Build triggers section and select the option “GitHub hook trigger for GITScm polling”

![Alt text](images/gitscm.png?raw=true)

## How do I trigger a build automatically in Jenkins?

### Step 1: Go to the GitHub repository and click on the Settings link highlighted by the red rectangle

![Alt text](images/13-click-on-settings-button.png?raw=true)

### Step 2: Click on the Webhooks option listed and as highlighted below

![Alt text](images/14-Jenkins-github-integration-Click-on-webhooks.png?raw=true)

### Step 3:  As soon as we will click on Webhooks, we will redirect to the Webhooks page. Now, click on the “Add webhook”  button highlighted in the below image

This webhook will notify Jenkins when there is a push, PR or repository created.
![Alt text](images/15-Jenkins-github-integration-Add-webhook-in-GitHub.png?raw=true)

### Step 4: Now perform the below steps to setup webhooks in GitHub

- Put the Payload URL in the textbox. Kindly note that doesn’t forget to append text `/github-webhook/` at the last.
- Click on the “Just the push event” option.
- Please make sure that you check the “Active” checkbox.
- Click on the “Add webhook”  button.
![Alt text](images/19-Jenkins-github-integration-Webhook-configuration.png?raw=true)

### Step 5: Create a new branch

![Alt text](images/integrate-with-github-org-11.png?raw=true)

### Step 6: Modify README.md or add a file to the repo

![Alt text](images/integrate-with-github-org-13.png?raw=true)

### Step 7: In Jenkins, you should see a new build is triggerred

![Alt text](images/integrate-with-github-org-14.png?raw=true)

### Step 8: Create a PR

![Alt text](images/integrate-with-github-org-15.png?raw=true)

### Step 9: In Jenkins, you should see a new build is triggerred

![Alt text](images/21-Build-automatically-triggered.png?raw=true)

### Step 10: Use Jenkins Pipeline rather than Freestyle so you can execute the Jenkinsfile

> Note: any branch is */*.
