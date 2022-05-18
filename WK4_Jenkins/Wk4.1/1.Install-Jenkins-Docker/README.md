# Description

This is to guide how to install Jenkins and run it in a Docker container.

## Pre-requisite

* Software: Docker

## Steps

### 1. Create a folder to hold Jenkins data

```bash
mkdir jenkins_home
cd jenkins_home
```

### 2. Start a Jenkins container

```bash
docker run --name jenkins \
           -u root \
           -d \
           -v $(pwd):/var/jenkins_home \
           -v /var/run/docker.sock:/var/run/docker.sock \
           -p 80:8080 \
           -p 50000:50000 \
           jenkinsci/blueocean
```

> Note:
>
> * `-u root` configures to run Jenkins by root user.
> * `-d` detaches the container
> * `-v $(pwd):/var/jenkins_home` mounts the current directory to Jenkins home inside the container
> * `-v /var/run/docker.sock:/var/run/docker.sock` mounts Docker socks
> * `-p 80:8080` maps port 80 in the host to port 8080 inside the container
> * `-p 50000:50000` maps ports 50000 which is the default port for angent registration
> * `jenkinsci/blueocean` is the image maintained by `jenkinsci`.
> * If you have error with port 80, please change it to 8080 or other port numbers.

### 3. Open <http://127.0.0.1> and you should see screen below

![Alt text](images/docker-install-01.png?raw=true)

### 4. Get your password by opening `secrets/initialAdminPassword` file in the directory you created in the first step

```bash
sudo cat secrets/initialAdminPassword
```

### 5. Continue installation in step #3 with password from step #4

You should see screen below after full installation.
![Alt text](images/docker-install-02.png?raw=true)
