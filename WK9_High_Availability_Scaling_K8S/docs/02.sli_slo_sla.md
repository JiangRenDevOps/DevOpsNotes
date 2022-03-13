## SRE fundamentals: SLIs, SLAs and SLOs

### 1. Service-Level Objective (SLO)

####Background
SRE's goal: make sure our service is up and running 24/7 -> Key to success: make sure our availability is 24/7

`Availability`, in SRE terms, 
* defines whether a system is able to fulfill its intended function at a point in time. 
* In addition to being used as a reporting tool, the historical availability measurement can also describe the probability that your system will perform as expected in the future.

We need -> quantify/ set a numerical target for our availability. That target is called SLO.


### 2. Service-Level Agreement (SLA)

An SLA normally involves a promise to someone using your service that its availability SLO should meet a certain level over a certain period, and if it fails to do so then some kind of penalty will be paid. This might be a partial refund of the service subscription fee paid by customers for that period, or additional subscription time added for free. The concept is that going out of SLO is going to hurt the service team, so they will push hard to stay within SLO.

Let us look at a few example

AWS: https://aws.amazon.com/compute/sla/
Google Cloud: https://cloud.google.com/terms/sla/
Jira: https://www.atlassian.com/legal/sla/service-credits


### 3. Service-Level Indicator

We need precise measurements on the key metrics that could help us decide on the service availability percentage.

If it goes below a SLO, we have a problem.
If it goes beyond a SLO too much, we also have a problem.


### 4. How should we set SLI SLO SLA?

Well, you may think shouldn't we set the SLO to 100% then? 

However the fact is:

* The cost for maintaining a 100% SLO is way too high. 

* Even if cost is not an issue, every module in the service need to have redundancy and a way to failover, 
including hardware, networks etc, which makes the maintenance not easy.

Here is a short recipe:
1. Identify the system boundaries within our platform.
2. Identify the customer-facing capabilities that exist at each system boundary.
3. Articulate a plain-language definition of what it means for each capability to be available. ![Alt text](../images/plain_text.png?raw=true)
4. Define one or more SLIs for that definition.
5. Start measuring to get a baseline.
6. Define an SLO for each capability, and track how we perform against it.
7. Iterate and refine our system, and fine tune the SLOs over time.

Leave SLA to the legals or management teams.


## Examples:

###Legacy:

![Alt text](../images/legacy.png?raw=true)

![Alt text](../images/sharevsnonshare.png?raw=true)

###Frontend:

![Alt text](../images/frontend.png?raw=true)




###Hard dependency

![Alt text](../images/network.png?raw=true)

* If something goes wrong in the UI tier, it’ll be an isolated failure that should be easy for us to recover from.
* If our service tier goes down, the UI will be impacted—but we can implement some UI caching to reduce that impact.
* If the data tier goes down, the service tier and UI tier also go down, and the UI can’t recover until both the data tier and service tier come back online.
* If the network tier goes down, everything goes down, and we’ll need recovery time before the system is back online. And since systems don’t come back the instant a dependency recovers, our mean time to recovery (MTTR) increases per tier.

![Alt text](../images/hard_dependency.png?raw=true)


##Managing Risk 
Ref: https://landing.google.com/sre/sre-book/chapters/embracing-risk/

Unreliable systems can quickly erode users’ confidence, so we want to reduce the chance of system failure. However, experience shows that as we build systems, cost does not increase linearly as reliability increments—an incremental improvement in reliability may cost 100x more than the previous increment. The costliness has two dimensions:

###The cost of redundant machine/compute resources
The cost associated with redundant equipment that, for example, allows us to take systems offline for routine or unforeseen maintenance, or provides space for us to store parity code blocks that provide a minimum data durability guarantee.

###The opportunity cost
The cost borne by an organization when it allocates engineering resources to build systems or features that diminish risk instead of features that are directly visible to or usable by end users. These engineers no longer work on new features and products for end users.

In SRE, we manage service reliability largely by managing risk. We conceptualize risk as a continuum. We give equal importance to figuring out how to engineer greater reliability into Google systems and identifying the appropriate level of tolerance for the services we run. Doing so allows us to perform a cost/benefit analysis to determine, for example, where on the (nonlinear) risk continuum we should place Search, Ads, Gmail, or Photos. Our goal is to explicitly align the risk taken by a given service with the risk the business is willing to bear. We strive to make a service reliable enough, but no more reliable than it needs to be. That is, when we set an availability target of 99.99%,we want to exceed it, but not by much: that would waste opportunities to add features to the system, clean up technical debt, or reduce its operational costs. In a sense, we view the availability target as both a minimum and a maximum. The key advantage of this framing is that it unlocks explicit, thoughtful risktaking.

##Measuring Service Risk
As standard practice, we are often best served by identifying an objective metric to represent the property of a system we want to optimize. By setting a target, we can assess our current performance and track improvements or degradations over time. For service risk, it is not immediately clear how to reduce all of the potential factors into a single metric. Service failures can have many potential effects, including user dissatisfaction, harm, or loss of trust; direct or indirect revenue loss; brand or reputational impact; and undesirable press coverage. Clearly, some of these factors are very hard to measure. To make this problem tractable and consistent across many types of systems we run, we focus on unplanned downtime.

For most services, the most straightforward way of representing risk tolerance is in terms of the acceptable level of unplanned downtime. Unplanned downtime is captured by the desired level of service availability, usually expressed in terms of the number of "nines" we would like to provide: 99.9%, 99.99%, or 99.999% availability. Each additional nine corresponds to an order of magnitude improvement toward 100% availability. For serving systems, this metric is traditionally calculated based on the proportion of system uptime (see Time-based availability).

###Time-based availability

```
availability = uptime / ( uptime + downtime )
```

Using this formula over the period of a year, we can calculate the acceptable number of minutes of downtime to reach a given number of nines of availability. For example, a system with an availability target of 99.99% can be down for up to 52.56 minutes in a year and stay within its availability target; see Availability Table for a table.

A time-based metric for availability is usually not meaningful because we are looking across globally distributed services. Our approach to fault isolation makes it very likely that we are serving at least a subset of traffic for a given service somewhere in the world at any given time (i.e., we are at least partially "up" at all times). Therefore, instead of using metrics around uptime, we define availability in terms of the request success rate. Aggregate availability shows how this yield-based metric is calculated over a rolling window (i.e., proportion of successful requests over a one-day window).

###Aggregate availability

```
availability = successful requests / total requests
```
For example, a system that serves 2.5M requests in a day with a daily availability target of 99.99% can serve up to 250 errors and still hit its target for that given day.

In a typical application, not all requests are equal: failing a new user sign-up request is different from failing a request polling for new email in the background. In many cases, however, availability calculated as the request success rate over all requests is a reasonable approximation of unplanned downtime, as viewed from the end-user perspective.

Quantifying unplanned downtime as a request success rate also makes this availability metric more amenable for use in systems that do not typically serve end users directly. Most nonserving systems (e.g., batch, pipeline, storage, and transactional systems) have a well-defined notion of successful and unsuccessful units of work. Indeed, while the systems discussed in this chapter are primarily consumer and infrastructure serving systems, many of the same principles also apply to nonserving systems with minimal modification.

For example, a batch process that extracts, transforms, and inserts the contents of one of our customer databases into a data warehouse to enable further analysis may be set to run periodically. Using a request success rate defined in terms of records successfully and unsuccessfully processed, we can calculate a useful availability metric despite the fact that the batch system does not run constantly.

Most often, we set quarterly availability targets for a service and track our performance against those targets on a weekly, or even daily, basis. This strategy lets us manage the service to a high-level availability objective by looking for, tracking down, and fixing meaningful deviations as they inevitably arise. See Service Level Objectives for more details.


## Error budget and cost

Cost is often the key factor in determining the appropriate availability target for a service. In determining the availability target for each service, we ask questions such as:

If we were to build and operate these systems at one more nine of availability, what would our incremental increase in revenue be?
Does this additional revenue offset the cost of reaching that level of reliability?
To make this trade-off equation more concrete, consider the following cost/benefit for an example service where each request has equal value:

Proposed improvement in availability target: 99.9% → 99.99%
Proposed increase in availability: 0.09%
Service revenue: $1M
Value of improved availability: $1M * 0.0009 = $900

