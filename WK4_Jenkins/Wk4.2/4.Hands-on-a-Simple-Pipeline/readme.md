# Hands on a Simple Pipeline

Now, let's try to create a pipeline to build an application. Jenkins is the Continuous Integration and Continuous Delivery (CI/CD) solution for any language, application, or platform. However, you need to remeber that different languages and platforms you working on have their specific requirements on building tools, and you need to configure your Jenkins yourself.

In this hands-on, we are going to configure your Jenkins environment to support and run a simple CI pipeline for an application.

## Prerequisites

* Your Jenkins

## Common Programming Languages

To set up a build pipeline, you need to know what is the programming language and it's runtime.

Below are some examples of languages and their extensions:

|Language|Code File|Project/Solution File|
|---|---|---|
|Java|.java, .do, .action, .jsp|.pom|
|DotNet|.cs, .aspx|.csproj, .sln|
|Go|.go|go.mod|
|NodeJS|.js|package.json|
|Bash|.sh||
|PowerShell|.ps||
|Python|.py||
|Web|.html, .css, .js||
|PHP|.php, .phtml||
|Ruby|.rb, .rhtml||

## Create Your Build Pipeline

We use this project to build a pipeline for one of it's API applications.

* Repo: https://github.com/RayMaAU/openhack-devops-team

Under the ``apis``, there are 4 applications. In this task, you are required to set up a build pipeline for one of them as you like:

* poi
* trips
* user-java
* userprofile

![Alt text](./images/github-apis.jpg?raw=true)

## Hands-On

Now, let's do hands on task. The goal is to select a API application from the above four as you like, and set up a **BUILD** pipeline in your Jenkins to have a successful build.

> NOTE:
>
> * Please ignore the Dockerfile under each API folder.
> * If you are `NOT` familiar with code test, you can ignore them.

### Task 1

Figure out the language used by the API you choosed and answering following questions:

1. What is the language?
2. What framework/SDK/runtime I may need?
3. What version?
4. How is the process to build this language?

### Task 2

Configure your Jenkins pipeline running environment, by installing any required:

* SDK?
* Framework?
* Build tool?
* Test tool (if you want to run tests)?
* other tools you may need?

### Task 3

Create a Jenkins **Pipeline**, and author your pipeline script.

![Alt text](./images/create-pipeline.jpg?raw=true)

Remember to pull the source code from GitHub first.

You are NOT required to deploy/publish the artifacts to anywhere, but please print the file list at the end of your pipeline task.

Generally, your pipeline should follow below stages and steps, however, you may `NOT` need them all for some programming languages:

```sh
pipeline {
    agent any

    stages {
        stage('Git checkout') {
            steps{
                // Get source code from a GitHub repository
            }
        }
        
        stage('Build') {
            steps{
                // Do your build task
            }
        }
        
        stage('Test') {
            steps{
                // Run unit tests, integration tests, and/or e2e tests
            }
        }
        
        stage('Publish') {
            steps{
                // Publish your artifacts to somewhere.
                // However, in our hands-on, you just need to print the artifact list by Linux command 'ls -la'
            }
        }

        post {
            always { 
                echo 'I will always say Hello again!'
            }
        }
    }
}
```

## Expected Result

The expected result for your pipeline(s) is/are:

If you build...

### **poi**

Build

```cmd
Build succeeded.
0 Warning(s)
0 Error(s)
```

UnitTest

```cmd
Passed!  - Failed:     0, Passed:    17, Skipped:     0, Total:    17, Duration: 1 s - /var/lib/jenkins/workspace/api-poi/apis/poi/tests/UnitTests/bin/Release/netcoreapp3.1/UnitTests.dll (netcoreapp3.1)
```

IntegrationTest

```cmd
Failed!  - Failed:     1, Passed:     0, Skipped:     0, Total:     1, Duration: < 1 ms - /var/lib/jenkins/workspace/api-poi/apis/poi/tests/IntegrationTests/bin/Release/netcoreapp3.1/IntegrationTests.dll (netcoreapp3.1)
```

> NOTE
>
> * Integration test is failed as expected as we don't have backend database and other components running.
> * Therefore, please don't include the IntegrationTest in your pipeline.

### **user-java**

Test

```cmd
Results :

Tests run: 7, Failures: 0, Errors: 0, Skipped: 0
```

Build

```cmd
[INFO] --------------
[INFO] BUILD SUCCESS
[INFO] --------------
```

### **trips**

Build

```sh
NO OUTPUT
```

UnitTest

```sh
ok    github.com/Azure-Samples/openhack-devops-team/apis/trips/tripsgo    0.014s
```

IntegrationTest

```sh
FAIL    github.com/Azure-Samples/openhack-devops-team/apis/trips/tripsgo    0.018s
```

> NOTE
>
> * Integration test is failed as expected as we don't have backend database and other components running.
> * Therefore, please don't include the IntegrationTest in your pipeline.

### **userprofile**

npm install

```sh
up to date, audited 448 packages in 20s
```

Tests

```sh
> mydriving-user-api@1.0.0 test
> tape 'tests/**/*.js' | tap-junit --output reports --name userprofile-report

Tap-Junit: Finished! userprofile-report.xml created at -- reports
```

npm coverage

```sh
> mydriving-user-api@1.0.0 cover
> nyc tape -- 'tests/**/*.js' --cov

TAP version 13
# /healthcheck/user
ok 1 No parse error
ok 2 Valid swagger api
# test get operation
ok 3 null
ok 4 should be truthy
ok 5 should be truthy
ok 6 No error
ok 7 Ok response status
ok 8 Valid response
ok 9 No validation errors

1..9
# tests 9
# pass  9

# ok
```
