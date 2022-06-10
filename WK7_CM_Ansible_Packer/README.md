# Description

This is to demo the generic usage of Ansible.

# Tasks

## Task #1: Install Ansible
Install Ansible, boto3 and botocore via pip3. We install boto3 because it's required by Ansible Inventory EC2 plugin.
```
pip3 install ansible boto3 botocore
```
Validate by executing `ansible --version` and check it's using python3.

You may need to add `export PATH=$HOME/.local/bin:$PATH` to your `~/.bashrc` or `~/.zshrc`

Alternatively, you can follow https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html

## Task #2: Create AWS EC2 instances in Sydney (ap-southeast-2) region to test
- Please create a ssh key in AWS. Suggest to import your ssh public key below directly.
```
cat ~/.ssh/id_rsa.pub
```


Make sure aws cli is configures

```
aws configure
aws sts get-caller-identity
```

You need the key name and VPC id for the next step.


Use terraform to create EC2 instances
```bash
cd ${your_repo_path}/WK7_CM_Ansible_Packer/terraform
terraform init
terraform validate

# change your key_name and vpc_id variable in main.tf
terraform apply

```

Check created instances.
## Task #3: Create an IAM user and configure three environment variables
Get the value from your AWS console.
```
export AWS_ACCESS_KEY=YOUR_AWS_ACCESS_KEY
export AWS_SECRET_KEY=YOUR_AWS_SECRET_KEY
export ANSIBLE_HOST_KEY_CHECKING=False
```



## Task #4: Run ad-hoc Ansible commands

Edit `hosts` file to add all host names.

```
ssh-add ~/.ssh/your_privatekey

cd ${your_repo_path}/WK7_CM_Ansible_Packer/ansible-playbooks/ansible-simple
ansible all -i hosts -u ubuntu -m ping
ansible web -i hosts -u ubuntu -m ping

# plugin aws

ansible all -i ../inventory.aws_ec2.yaml -u ubuntu -m ping

# inspect groups
ansible all -i ../inventory.aws_ec2.yaml -u ubuntu  -m debug -a 'var=groups.keys()'

# ping one group
ansible tag_web -i ../inventory.aws_ec2.yaml -u ubuntu  -m ping

ansible tag_web -i ../inventory.aws_ec2.yaml -u ubuntu  -m command -a "df -h"
ansible tag_redis -i ../inventory.aws_ec2.yaml -u ubuntu  -a "df -h" # command is the default module

ansible tag_redis -i ../inventory.aws_ec2.yaml -u ubuntu -m ansible.builtin.copy -a "src=/etc/hosts dest=/tmp/hosts"

ansible tag_redis -i ../inventory.aws_ec2.yaml -u ubuntu -a "cat /tmp/hosts"

```

about inventory: https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html

about ping module: https://docs.ansible.com/ansible/latest/collections/ansible/builtin/ping_module.html

about ansible plugins: https://docs.ansible.com/ansible/latest/plugins/plugins.html

about aws-ec2 plugin: https://docs.ansible.com/ansible/2.6/plugins/inventory/aws_ec2.html

all modules: https://docs.ansible.com/ansible/latest/collections/index_module.html

## Task #5: Simple playbook

Let's write a playbook to do the following

* install redis (apt-get update && apt-get install redis)
* start redis server (systemtcl start redis.service)

```bash

ansible-playbook -i ../inventory.aws_ec2.yaml site.yaml
ansible tag_redis -i ../inventory.aws_ec2.yaml -u ubuntu -a "systemctl status redis"


```

## Task #6: Install a docker role from galaxy to your local laptop
```

cd ${your_repo_path}/WK7_CM_Ansible_Packer/ansible-playbooks/ansible-playbook-plain

# get all facts ansible_distribution_release

ansible tag_redis -i inventory.aws_ec2.yaml -u ubuntu -m ansible.builtin.setup




ansible-galaxy install geerlingguy.docker
ansible-galaxy install geerlingguy.pip
```
More about galaxy: https://docs.ansible.com/ansible/latest/galaxy/user_guide.html

Alternatively, you can use `ansible-galaxy install -r requirements.yaml`

## Task #7: Read playbook under ansible-playbook-plain and execute

Read `site.yaml` under `ansible-playbook-plain`.
```
ansible-playbook -i ../inventory.aws_ec2.yaml site.yaml
```
More about play book: https://docs.ansible.com/ansible/latest/user_guide/playbooks.html

apt_repository module: https://docs.ansible.com/ansible/latest/collections/ansible/builtin/apt_repository_module.html

conditions: https://docs.ansible.com/ansible/latest/user_guide/playbooks_conditionals.html

variables: https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html

special variables: https://docs.ansible.com/ansible/latest/reference_appendices/special_variables.html


## Task #8: Read playbook under ansible-playbook-roles and execute
Read `site.yaml` under `ansible-playbook-roles`.
```
ansible-playbook -i ../inventory.aws_ec2.yaml site.yaml
```

roles: https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html

## Task #9: Install more software via Ansible and play around
Install sth like Jenkins, Kubernetes, wordpress, nginx etc.

# Homework

Learn packer and run packer examples in the `packer` folder.


Don't forget to delete.

```
terraform apply -destroy
```