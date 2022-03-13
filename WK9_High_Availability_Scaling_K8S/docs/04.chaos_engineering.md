#Chaos Engineering

With the rise of microservices and distributed cloud architectures, the web has grown increasingly complex. We all depend on these systems more than ever, yet failures have become much harder to predict.

These failures cause costly outages for companies. The outages hurt customers trying to shop, transact business, and get work done. Even brief outages can impact a company's bottom line, so the cost of downtime is becoming a KPI for many engineering teams. For example, in 2017, 98% of organizations said a single hour of downtime would cost their business over $100,000. One outage can cost a single company millions of dollars. The CEO of British Airways recently explained how one failure that stranded tens of thousands of British Airways (BA) passengers in May 2017 cost the company 80 million pounds ($102.19 million USD).

Companies need a solution to this challenge—waiting for the next costly outage is not an option. To meet the challenge head on, more and more companies are turning to Chaos Engineering.

#Chaos Engineering is Preventive Medicine

Chaos Engineering is a disciplined approach to identifying failures before they become outages. By proactively testing how a system responds under stress, you can identify and fix failures before they end up in the news.

Chaos Engineering lets you compare what you think will happen to what actually happens in your systems. You literally “break things on purpose” to learn how to build more resilient systems.

#A Brief History
Chaos Engineering first became relevant at internet companies that were pioneering large scale, distributed systems. These systems were so complex that they required a new approach to test for failure.

##2010
The Netflix Eng Tools team created Chaos Monkey. Chaos Monkey was created in response to Netflix’s move from physical infrastructure to cloud infrastructure provided by Amazon Web Services, and the need to be sure that a loss of an Amazon instance wouldn’t affect the Netflix streaming experience.

![Alt text](../images/chaos_money.png?raw=true)

##2011
The Simian Army was born. The Simian Army added additional failure injection modes on top of Chaos Monkey that would allow testing of a more complete suite of failure states, and thus build resilience to those as well. “The cloud is all about redundancy and fault-tolerance. Since no single component can guarantee 100% uptime (and even the most expensive hardware eventually fails), we have to design a cloud architecture where individual components can fail without affecting the availability of the entire system” (Netflix, 2011).

##2012
Netflix shared the source code for Chaos Monkey on Github, saying that they “have found that the best defense against major unexpected failures is to fail often. By frequently causing failures, we force our services to be built in a way that is more resilient” (Netflix, 2012).

##2014
Netflix decided they would create a new role: the Chaos Engineer. Bruce Wong coined the term, and Dan Woods shared it with the greater engineering community via Twitter. Dan Woods explained, “I learned more about Chaos Engineering from Kolton Andrus than anyone else, he called it failure injection testing".

In October of 2014, while Gremlin co-founder Kolton Andrus was at Netflix, his team announced Failure Injection Testing (FIT), a new tool that built on the concepts of the Simian Army, but gave developers more granular control over the “blast radius” of their failure injection. The Simian Army tools had been so effective that in some instances they created painful outages, causing many Netflix developers to grow wary of them. FIT gave developers control over the scope of their failure so they could realize the insights of Chaos Engineering, but mitigate potential downside.

#What are the Principles of Chaos Engineering?
Chaos Engineering involves running thoughtful, planned experiments that teach us how our systems behave in the face of failure.

These experiments follow three steps:



1. You start by forming a hypothesis about how a system should behave when something goes wrong.

2. Then, you design the smallest possible experiment to test it in your system.

3. Finally, you measure the impact of the failure at each step, looking for signs of success or failure. When the experiment is over, you have a better understanding of your system's real-world behavior.

#Which companies practice Chaos Engineering?
Many larger tech companies practice Chaos Engineering to better understand their distributed systems and microservice architectures. The list includes Twilio, Netflix, LinkedIn, Facebook, Google, Microsoft, Amazon, and many others. The list is always growing.

But more traditional industries, like banking and finance, have caught on to Chaos Engineering, too. For example, in 2014, the National Australia Bank migrated from physical infrastructure to Amazon Web Services and used Chaos Engineering to dramatically reduce incident counts.

The Chaos Engineering Slack Community has created a diagram that tracks known Chaos Engineering tools and known engineers working on Chaos Engineering.


#How do you plan for your first chaos experiments?
##Planning your First Experiment
One of the most powerful questions in Chaos Engineering is “What could go wrong?”. By asking this question about our services and environments, we can review potential weaknesses and discuss expected outcomes. Similar to a risk assessment, this informs priorities about which scenarios are more likely (or more frightening) and should be tested first. By sitting down as a team and whiteboarding your service(s), dependencies (both internal and external), and data stores, you can formulate a picture of “What could go wrong?”. When in doubt, injecting a failure or a delay into each of your dependencies is a great place to start.

##Creating a Hypothesis
You have an idea of what can go wrong. You have chosen the exact failure to inject. What happens next? This is an excellent thought exercise to work through as a team. By discussing the scenario, you can hypothesize on the expected outcome before running it live. What will be the impact to customers, to your service, or to your dependencies?

##Measuring the Impact
To understand how your system behaves under stress, you need to measure your system’s availability and durability. It is good to have a key performance metric that correlates to customer success (such as orders per minute, or stream starts per second). As a rule of thumb, if you ever see an impact to these metrics, you want to halt the experiment immediately. Next is measuring the failure itself where you want to verify (or disprove) your hypothesis. This could be the impact on latency, requests per second, or system resources. Lastly, you want to survey your dashboards and alarms for unintended side effects.

##Have a Rollback Plan
Always have a backup plan in case things go wrong, but accept that sometimes even the backup plan can fail. Talk through how you’re going to revert the impact. If you’re running commands by hand, be thoughtful not to break ssh or control plane access to your instances. One of the core aspects of Gremlin is safety. All of our attacks can be reverted immediately, allowing you to safely abort and return to steady state if things go wrong.

##Go fix it!
After running your first experiment, hopefully, there is one of two outcomes: either you’ve verified that your system is resilient to the failure you introduced, or you’ve found a problem you need to fix. Both of these are good outcomes. On one hand, you’ve increased your confidence in the system and its behavior, and on the other you’ve found a problem before it caused an outage.

##Have Fun
Chaos Engineering is a tool to make your job easier. By proactively testing and validating your system’s failure modes you will reduce your operational burden, increase your availability, and sleep better at night.

#Why would you break things on purpose?
It's helpful to think of a vaccine or a flu shot where you inject yourself with a small amount of a potentially harmful foreign body in order to prevent illness. Chaos Engineering is a tool we use to build such an immunity in our technical systems by injecting harm (like latency, CPU failure, or network black holes) in order to find and mitigate potential weaknesses.

These experiments have the added benefit of helping teams build muscle memory in resolving outages, akin to a fire drill (or changing a flat tire, in the Netflix analogy). By breaking things on purpose we surface unknown issues that could impact our systems and customers.


