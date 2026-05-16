# AI Sandbox

An example repo for high quality SDLC with maximum use of AI coding agents.

## Principles
- Workflow is king - we want to tell our agents clearly and concisely how to work for best outcome
- Test first, test broadly - write tests to a point coverage that would be inefficent if a human were doing it, write them first to constrain the implementation
- Trust the model - model development is a humanity wide effort which will outpace our ability to create guardrails

## SDLC
1. Refine - turn a ticket into design and behaviours
2. Build - turn behaviours into working tests, implement code to make tests pass and refactor the implementation to better match the design without breaking tests
3. Integrate - combine the work with other work on main and make tests pass
4. Review - turn the integrated build into a pull request and fix based on feedback
5. Publish - merge the pull request, update versions and documentation and close the ticket 

## Skills

### Design
Read docs/architecture to get a set of constraints for the design
Read a ticket from docs/backlog
Write a set of behaviours in docs/spec/<ticket>

### Specify
Take a ticket from docs/backlog and produce additional behavioural scenarios in docs/spec

### Task
Make tasks from ticket

### Branch
Make an iteration branch in git named for the ticket eg. iteration/00001-Greeting

### Red
Create a test in test from a behavioural scenario and connect it to the scenario
Run all the tests and make sure only the new tests fail

### Green
Create code in src that meets the specification 
Run all the tests and make sure they all pass without changing them

### Refactor
Alter the implementation of the specification to better meet the design and architecture
Ensure all the tests pass without changing them

### Commit
Create a commit message that summarises the changes according to the template at docs/commit_message
Add a git commit that describes the changes that have been made

### Merge
Merge the main branch into the iteration branch
Run all the tests and trigger Green and Refactor as needed

### Push
Create the branch in the origin repo for the iteration branch

### Raise
Create a pull request in the origin repo for the iteration branch targetting the main branch

### Fix
Take a review comment in the pull request and trigger Red, Green, Refactor, Commit and Push as necessary

### Version
Take the iteration and current version and increment the version triggering Commit and Push as necessary

### Document
Take the version, ticket, review and commit messages and turn them into a document stored in docs/version/<version_number>

### Publish 
Take the iteration branch and push it to the main branch
