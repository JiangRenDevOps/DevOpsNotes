# Jenkins Basic Configurations

## Jenkins Home Directory

Jenkins needs some disk space to perform builds and keep archives. You can check this location from the configuration screen of Jenkins. By default, this is set to **~/.jenkins**, and this location will initially be stored within your user profile location. In a proper environment, you need to change this location to an adequate location to store all relevant builds and archives. You can do this in the following ways:

* Set "``JENKINS_HOME``" environment variable to the new home directory before launching the servlet container.

* Set "``JENKINS_HOME``" system property to the servlet container.

* Set JNDI environment entry "``JENKINS_HOME``" to the new directory.

The following example will use the first option of setting the "JENKINS_HOME" environment variable.

First create a new folder E:\Apps\Jenkins. Copy all the contents from the existing ~/.jenkins to this new directory.

Set the ``JENKINS_HOME`` environment variable to point to the base directory location where Java is installed on your machine. For example,

| OS      | Output |
| ------- | ------ |
| Windows | Set Environmental variable **JENKINS_HOME** to you’re the location you desire. As an example you can set it to E:\Apps\Jenkins |
| Linux   | export JENKINS_HOME =/usr/local/Jenkins or the location you desire. |

In the Jenkins dashboard, click ``Manage Jenkins`` from the left hand side menu. Then click on ``Configure System`` from the right hand side.

In the Home directory, you will now see the new directory which has been configured.

![Alt text](images/jenkins_config_home.png?raw=true)

To change your Jenkins home directory, please follow this doc: https://dzone.com/articles/jenkins-02-changing-home-directory.

## # of executors

This refers to the total number of concurrent job executions that can take place on the Jenkins machine. This can be changed based on requirements. Sometimes the recommendation is to keep this number the same as the number of CPU on the machines for better performance.

## Jenkins Location

By default, the Jenkins URL points to localhost. If you have a domain name setup for your machine, set this to the domain name else overwrite localhost with IP of machine. This will help in setting up slaves and while sending out links using the email as you can directly access the Jenkins URL using the environment variable **JENKINS_URL** which can be accessed as ``${JENKINS_URL}``.

## Global properties -> Environment Variables

This is used to add custom environment variables which will apply to all the jobs. These are key-value pairs and can be accessed and used in Builds wherever required.

![Alt text](images/jenkins_config_global_env.png?raw=true)

For example, if you want to add JDK configs, first, you need to find out the Java installation paths using the ``update-alternatives`` command:

```bash
sudo update-alternatives --config java
```

In our case, the installation paths are as follows:

* OpenJDK 11 is located at /usr/lib/jvm/java-11-openjdk-amd64/bin/java
* OpenJDK 8 is located at /usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java

Copy the installation path of your preferred installation. Next, open the ``/etc/environment`` file:

```bash
sudo nano /etc/environment
```

Add the following line, at the end of the file:

```bash
JAVA_HOME="/usr/lib/jvm/java-11-openjdk-amd64"
```

Make sure you replace the path with the path to your preferred Java version.

You can either log out and log in or run the following source command to apply the changes to your current session:

```bash
source /etc/environment
```

To verify that the JAVA_HOME environment variable is correctly set, run the following echo command :

```bash
echo $JAVA_HOME
```

```
[Output]
/usr/lib/jvm/java-11-openjdk-amd64
```

Alternatively, you can also add this path to Jenkins as it's Environment variables. Below screenshot is just an example:

![Alt text](images/jenkins_config_global_env_sample.png?raw=true)

## Email Notification

In the email Notification area, you can configure the SMTP settings for sending out emails. This is required for Jenkins to connect to the SMTP mail server and send out emails to the recipient list.
