# Homework

1. Complete Scenario 1-4 in the slides.
2. Launch a EC2 instance, then setup a periodic job on your local machine that:

- runs every 5 minutes
- scan the log message that is produced on this EC2 machine since last report was successfully generated
- collect every line of the log message that include string "error" (case insensitive). consider using regex.
- aggregated the collected result into a file and store in your local machine, with query timestamp shown in the file name

Before you start on above work, take a moment to think about following:
- How do you implement the "since last report successfully generated" logic? do you need to implement any additional layer to support this logic? how many different ways can you think of to implement this? which is better/worse in what scenario?
- For the script that you're writing, consider making it generic so that we are not hardcoding any values (e.g. the string "error" we are looking for). Take out common modules that could be re-used and make it into a function.
