# Accessing local cluster with ingress controller (Load Balancer)

## ClusterIP
A ClusterIP service is the default Kubernetes service. It gives you a service inside your cluster that other apps
inside your cluster can access. There is no external access.

Wait? what? How do I access the cluster from the internet then?

![Alt text](../images/cluster_proxy.png?raw=true)

Well, you certainly can access your cluster by set up a proxy:
```
kubectl proxy --port=8080
```
and then you can access your cluster via the API

```
http://localhost:8080/api/v1/proxy/namespaces/<NAMESPACE>/services/<SERVICE-NAME>:<PORT-NAME>/
```
However, there are a few scenarios that you would use this:
* Debugging your services, or connecting to them directly from your laptop for some reason 
  
* Allowing internal traffic, displaying internal dashboards, etc.

__Note: You should NOT use this to expose your service to the internet or use it for production services, because it 
requires you to run kubectl as an authenticated user.__


## NodePort
A NodePort service is the most primitive way to get external traffic directly to your service. NodePort, 
as the name implies, opens a specific port on all the Nodes (the VMs), and any traffic that is sent to this port is
forwarded to the service.

![Alt text](../images/cluster_nodeport.png?raw=true)

Basically, a NodePort service has two differences from a normal “ClusterIP” service. First, the type is “NodePort.”
There is also an additional port called the nodePort that specifies which port to open on the nodes.

There are many downsides to this method:
* You can only have one service per port
* You can only use ports 30000–32767
* If your Node/VM IP address change, you need to deal with that

If you are running a service that doesn’t have to be always available, or you are very cost sensitive, this method
will work for you. But again, not recommended for prod.

## Load Balancer

A LoadBalancer service is the standard way to expose a service to the internet. On GKE, this will spin up a Network
Load Balancer that will give you a single IP address that will forward all traffic to your service.

![Alt text](../images/cluster_loadbalancer.png?raw=true)

### When would you use this?
If you want to directly expose a service, this is the default method. All traffic on the port you specify will be 
forwarded to the service. This means you can send almost any kind of traffic to
it, like HTTP, TCP, UDP, Websockets, gRPC, or whatever. https://cloud.google.com/compute/docs/load-balancing/network/

The big downside is that each service you expose with a LoadBalancer will get its own IP address, and you have to pay
for a LoadBalancer per exposed service, which can get expensive!

## Ingress
Unlike all the above examples, Ingress is actually NOT a type of service. Instead, it sits in front of multiple services
and act as a “smart router” or entrypoint into your cluster.

You can do a lot of different things with an Ingress, and there are many types of Ingress controllers that have 
different capabilities.

The default GKE ingress controller will spin up an HTTP(S) Load Balancer for you.
https://cloud.google.com/load-balancing/docs/https
This will let you do both path based and subdomain based routing to backend services. For example, you can send
everything on foo.yourdomain.com to the foo service, and everything under the yourdomain.com/bar/ path to the bar
service.

![Alt text](../images/cluster_ingress.png?raw=true)

### When would you use this?
Ingress is probably the most powerful way to expose your services, but can also be the most complicated. There are many
types of Ingress controllers, from the Google Cloud Load Balancer, Nginx, Contour, Istio, and more. There are also 
plugins for Ingress controllers, like the cert-manager, that can automatically provision SSL certificates for your
services.

Ingress is the most useful if you want to expose multiple services under the same IP address, and these services all use
the same L7 protocol (typically HTTP). You only pay for one load balancer if you are using the native GCP integration,
and because Ingress is “smart” you can get a lot of features out of the box (like SSL, Auth, Routing, etc)

Ref: https://medium.com/google-cloud/kubernetes-nodeport-vs-loadbalancer-vs-ingress-when-should-i-use-what-922f010849e0


## Hands-on

Goal: Setup Ingress Controller instead of Port forwarding for example-voting-app

When reload the page, you should see different pods being accessed.

![Alt text](../images/pod1.png?raw=true)
![Alt text](../images/pod2.png?raw=true)


### Step 1. Switch the service type from NodePort to ClusterIP, remove nodePort and modify the port to 80

```
diff --git a/k8s-specifications/vote-service.yaml b/k8s-specifications/vote-service.yaml
index c9d4972..854fed1 100644
--- a/k8s-specifications/vote-service.yaml
+++ b/k8s-specifications/vote-service.yaml
@@ -6,12 +6,28 @@ metadata:
   name: vote
   namespace: vote
 spec:
-  type: NodePort
+  type: ClusterIP
   ports:
   - name: "vote-service"
-    port: 5000
+    port: 80
+    protocol: TCP
     targetPort: 80
-    nodePort: 31000
   selector:
     app: vote
-
```
after modification `k8s-specifications/vote-service.yaml` :
```
apiVersion: v1
kind: Service
metadata:
  labels:
    app: vote
  name: vote
  namespace: vote
spec:
  type: ClusterIP
  ports:
  - name: "vote-service"
    port: 80
    protocol: TCP
    targetPort: 80
  selector:
    app: vote
```


### Step 2. Specify the ingress controller configuration

Add the following to the `k8s-specifications/vote-service.yaml`


```
---
apiVersion: projectcontour.io/v1
kind: HTTPProxy
metadata:
  name: vote-proxy
  namespace: vote
  labels:
    app: vote
spec:
  virtualhost:
    fqdn: localhost
  routes:
  - services:
    - name: vote
      port: 80
    
```
Note that kind is not Ingress, as HTTPProxy provide richer experience of projectcontour. Explore the benefits here:
https://projectcontour.io/docs/main/config/fundamentals/

### Step 3. Create a `run.sh` file in the example-voting-app root folder (outside k8s-specifications)
We will need to 
* re-config our cluster
* install contour
* create a namespace
* create the nodes, pods and deploy all services
```
kind create cluster --config=config.yaml

kubectl apply -f https://projectcontour.io/quickstart/contour.yaml

kubectl create namespace vote

kubectl create -f k8s-specifications/
```

### Step 4. Add a config file in the example-voting-app root folder (outside k8s-specifications)
Since we don't have internet IP address available on our local machine, you need this for accessing the kind cluster
```
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
- role: control-plane
- role: worker
  extraPortMappings:
  - containerPort: 80
    hostPort: 80
    listenAddress: "0.0.0.0"
  - containerPort: 31001
    hostPort: 31001
    listenAddress: "0.0.0.0"
```

### Step 5. Chmod run.sh and run it
```
chmod u+x run.sh
./run.sh
```

### Step 5. Check Status
Check service status
```
kubectl get services --output wide -n vote
kubectl get services -o wide -n projectcontour
```
Check pod status
```
kubectl get pods --output wide -n vote
kubectl get pods -n projectcontour -o wide
```
Check logs of a particular service
```
kubectl logs svc/result -n vote
kubectl logs svc/contour -n projectcontour
kubectl logs svc/db -n vote
```
Check the HTTP Proxy status and config
```
kubectl get httpproxy -n vote
kubectl describe httpproxy vote-proxy -n vote
```
Check nodes
```
kubectl get nodes -n vote -o wide
kubectl describe node kind-worker -n vote
```

### Step 6. Identify Errors

The result page never works, what happened?
```
kubectl logs svc/result -n vote
```
It says
```
Waiting for db
```
Let us check the db logs
```
kubectl logs svc/db -n vote
```
It shows
```
FATAL:  password authentication failed for user "postgres"
DETAIL:  Connection matched pg_hba.conf line 95: "host all all all md5"
```
What do we do?

Let us firstly check if there is any open issue in the github

https://github.com/dockersamples/example-voting-app/issues/193

Looks like a workaround is given by setting an environment variable POSTGRES_HOST_AUTH_METHOD: "trust" for the db.

### Step 7. Fix the errors
Add the following lines to line 26 of `k8s-specifications/db-deployment.yaml`
```
        - name: POSTGRES_HOST_AUTH_METHOD
          value: "trust"
```
Save the file

### Step 8. Delete Cluster and Restart
Let us delete the current cluster
```
kind delete cluster
```
Let us restart
```
./run.sh
```

### Step 9. Viola
Once the containers are running, let us validate:
```
kubectl logs svc/db -n vote
```
You should see:
```
PostgreSQL init process complete; ready for start up.

LOG:  database system was shut down at 2022-03-12 03:54:55 UTC
LOG:  MultiXact member wraparound protections are now enabled
LOG:  autovacuum launcher started
LOG:  database system is ready to accept connections
```
Check:
```
kubectl logs svc/result -n vote
```
You should see:
```
App running on port 80
Connected to db
```
Open http://localhost/ you should be able to click on the votable item and your pod will change after reload.

Open http://localhost:31001/ and you should see a working version result page:
![Alt text](../images/result.png?raw=true)

The number of vote will remain 1 vote no matter how many times you reload your page. However, it will change when you
use a different browser to access. 

