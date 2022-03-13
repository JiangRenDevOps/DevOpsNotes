# High Availability
High availability refers to systems that are durable and likely to operate continuously without failure for a long time. The term implies that parts of a system have been fully tested and, in many cases, that there are accommodations for failure in the form of redundant components.

# Failover
https://docs.rightscale.com/cm/designers_guide/cm-designing-and-deploying-high-availability-websites.html


# Hands-on
Voting App Example 1
https://github.com/docker/swarm-microservice-demo-v1

```
git clone https://github.com/docker/swarm-microservice-demo-v1
```

Since it is a old repo, it has a dependency error. We need to fix it by editing `vote-worker/Dockerfile`

Change from java to openjdk as below
```
FROM openjdk:7
```

Then run it

```
docker-compose -f docker-compose.yml -f docker-compose.override.yml up
```

After it is done, you should be able to visit 

vote app
```
http://localhost:8081
```

result app
```
http://localhost:8082
```

- Q: Let us try to understand what it does and how to spin it up?

- Q: Why do you see only 1 vote in one browser?
![Alt text](../images/one-vote.png?raw=true)

- Q: How would high availability help the App?

- Q: What other problems do you see with the App? Is it 100% available now? How to improve?
