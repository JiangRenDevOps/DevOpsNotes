# EKS
This is the handson to deploy a simple app to EKS. So you can get a feel.

# Prerequisite
Have AWS account

Warning:
- It is not free to use EKS. You pay $0.10 per hour for each Amazon EKS cluster that you create. Also, there is extra pricing if use Fargate.
  https://aws.amazon.com/eks/pricing/

## How to get started

https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html

1. Choose a way to get started:
- Getting started with eksctl (fastest and easiest)
  https://docs.aws.amazon.com/eks/latest/userguide/getting-started-eksctl.html 
  
- Getting started with the AWS Management Console
  https://docs.aws.amazon.com/eks/latest/userguide/getting-started-console.html 

2. Create a cluster using eksctl (Note it may take ~10mins)

3. Deploy app using kubectl

## Install and config ekscli
https://eksctl.io/

- Install https://docs.aws.amazon.com/eks/latest/userguide/eksctl.html
- Config `aws configure` with your own access id and key.
  https://console.aws.amazon.com/iam/home?region=ap-southeast-2#/security_credentials 

## Create a cluster in EKS

1. execute in terminal
```
eksctl create cluster \
--name eks-cluster \
--version 1.17 \
--region ap-southeast-2 \
--nodegroup-name linux-nodes \
--node-type t2.micro \
--nodes 3 \
--ssh-access \
--ssh-public-key <<your own key pair>> \
--managed
```

2. Take a break and wait for about 10mins

3. check EKS cluster after success

## Deploy the app

1. Create a namespace and deploy the sample app
```
kubectl create namespace eks-demo
kubectl apply -f https://k8s.io/examples/application/php-apache.yaml -n eks-demo
```

2. Get the resources
```
kubectl get all -n eks-demo

NAME                              READY   STATUS    RESTARTS   AGE
pod/php-apache-79544c9bd9-7j4nv   1/1     Running   0          77s

NAME                 TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)   AGE
service/php-apache   ClusterIP   10.100.59.226   <none>        80/TCP    77s

NAME                         READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/php-apache   1/1     1            1           77s

NAME                                    DESIRED   CURRENT   READY   AGE
replicaset.apps/php-apache-79544c9bd9   1         1         1       77s
```

3. Inspect there is not external Ip, so we can patch the service with a load balancer

```
kubectl -n eks-demo patch svc php-apache -p '{"spec": {"type": "LoadBalancer"}}'
```

4. Check the service again

```
kubectl get service -n eks-demo
NAME         TYPE           CLUSTER-IP      EXTERNAL-IP                                                                   PORT(S)        AGE
php-apache   LoadBalancer   10.100.59.226   a5ee699eec62a49178cd880a1cc131ab-223434949.ap-southeast-2.elb.amazonaws.com   80:32620/TCP   9m40s
```

5. Check the load balancer link

Q: Why it does not load?

6. Remove the resources and cluster if you do not want to continue.

```
kubectl delete deployment.apps/php-apache -n eks-demo
eksctl delete cluster eks-cluster
```

## What is next?
So the following can be worked as homework if you are interested.

### Install Metrics Server
https://docs.aws.amazon.com/eks/latest/userguide/metrics-server.html 

### Horizontal Pod Autoscaler 
https://docs.aws.amazon.com/eks/latest/userguide/horizontal-pod-autoscaler.html 

### Vertical Pod Autoscaler
https://docs.aws.amazon.com/eks/latest/userguide/vertical-pod-autoscaler.html 

### Cluster Autoscaler
https://docs.aws.amazon.com/eks/latest/userguide/cluster-autoscaler.html
