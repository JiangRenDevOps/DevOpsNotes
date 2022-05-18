# Jenkins Basic Management

## System Jenkins -- Configure Global Security

After Jenkins is installed, you should properly assign permissions to your accounts/groups, otherwise the accounts may not able to perform the task.

Under **Manage Jenkins** -> **Configure Global Security** -> **Authorization**, select ``Matrix-based security``, add your admin account as a user, and then grant all permissions.

![Alt text](images/jenkins_config_matrix_permission.png?raw=true)

Select **Apply** and then **Save**.

> NOTE: You must first click Apply (Application), and then click Save (Save), otherwise the permissions set will not work.

There is no group support for the built-in Jenkins user database. Group support is only usable when integrating Jenkins with LDAP or Active Directory.

## Plug-in Management

Jenkins can be seen as a framework that is able to integrate with anything you want, enabling the company's entire continuous integration system. Plugins can be installed as needed, or through scripts.

Under **Manage Jenkins** -> **Manage Plugins**, you can manage the updates and installs.

![Alt text](images/jenkins_config_manage_plugins.png?raw=true)

Let's try to install **Azure CLI** to your Jenkins as a plugin.

Search "**Azure CLI**" from the search bar and select **Available**, then tick the only one from the result list, click "**Install without restart**".

The plugin can be easily installed.

![Alt text](images/jenkins_config_manage_plugins_install.png?raw=true)

## Global Tool Configuration

Maven, JDK, Git, etc. are the most common and popular tools and installed with your Jenkins by default.

Navigate to **Manage Jenkins** -> **Global Tool Configuration**, here you will be able to manage them.

![Alt text](images/jenkins_config_global_tool_config.png?raw=true)

Take Java as an example, you may configure it like below example:

> NOTE: This is just an example to demostrate how to configure. You may not need it.

![Alt text](images/jenkins_config_global_tool_config_java_example.png?raw=true)

