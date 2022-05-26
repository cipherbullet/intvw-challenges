# energi

## Rules
You can copy, search, google, duckduckgo, stackoverflow, github or otherwise source your answers without losing marks, however - If you
copy something verbatim you must reference it (for example in an inline comment) - If there are no comments explaining what it does you must
add some - You should strive to test that what you’ve copied to ensure it works and fulfills the objective

Generally speaking, there will be marks for just achieving anything at all (unless you copied it without referencing), plus some for each sub
requirement, and then a few for style and explanation. Please don’t spend too much time. A couple of hours should suffice - maybe a little more if
you have to pick stuff up as you go along.

**Questions 1-3 are mandatory** - you can skip any of the subsequent questions, but you need to write a short explanation as to why (e.g. I’ve
never used this technology, and it’s not on my CV; or I spent too much time on the other questions).

## Challenges
**1. Docker Whale**
Write a Dockerfile to run Energi v3.1.2 in a container. It should somehow verify the checksum of the downloaded release

(there’s no need to build the project), run as a normal user, it should run the client, and print its output to the console.

https://wiki.energi.world/en/downloads/core-node

The build should be security conscious, and ideally pass a container image security test such as ECR, or Trivy. **[20 pts]**

**2. K8S Awesomness**
Write a Kubernetes StatefulSet to run the above, using persistent volume claims and resource limits. **[10 pts]**

**3. All the continuouses**
Write a simple build and deployment pipeline for the above using groovy / Jenkinsfile, Travis CI or Gitlab CI. **[15 pts]**

**4. Script kiddies**
Source or come up with a text manipulation problem and solve it with at least two of awk, sed, tr. and / or grep. Check the question below first though, maybe. **[10 pts]**

**5. Script grown-ups**
Solve the problem in question 4 using any programming language of your choice. **[15 pts]**

**6. Terraform lovers**
write a Terraform module that creates the following resources in IAM: - A role, with no permissions, which can be

assumed by users within the same account - A policy, allowing users / entities to assume the above role - A group, with the above policy
attached - A user, belonging to the above group - All four entities should have the same name, or be similarly named in some meaningful
way given the context e.g. prod-ci-role, prod-ci-policy, prod-ci-group, prod-ci-user; or just prod-ci. Make the suffixes toggleable, if you
wish. **[20 pts]**

## Evaluation
Either submit your work by email as an attachment or provide a link to an online source code repository such as Github or Gitlab. **10
points are reserved for style, and substance.** Total is 100. Pass mark is 50.
Good luck!

