# Dapr Agents coding agent assignment

Your task is to make a coding agent using the starter provided in this repository.
The expectation is to use 2-4 hours. It should not be necessary to spend >4 hours.

## Pre-requisites

This starter assumes a running [ollama](https://ollama.com/download) with [llama3.2:latest](https://ollama.com/library/llama3.2:latest). This allows you to conduct the assignment without relying on external models.  
Feel free to change this to your liking.
  
You'll also need [the Dapr CLI](https://docs.dapr.io/getting-started/install-dapr-cli/) installed.

## Task 1

Get the agent running and decide on the way to run the agent.
Feel free to change the `./components` files to your liking.

### Deliverable
Be able to articulate _why_ this method was chosen for this specific type of agent.

## Task 2

Implement tools relevant for a coding agent. Suggestions for tools
1. Filesystem  
2. Pattern matching
3. File modification  
4. Git operations
5. Os commands

### Deliverable
Walk through and explain in detail the implemented  tool.  
Explain why this tool is relevant for a coding agent.  
Explain in detail how to code works and achieve the desired outcome.

## Task 3

Understand the code execution of the agent. What goes on under the hood in Dapr Agents (and the dependencies).

### Deliverable
Demo the agent.  
Explain what happens during the execution flow of the agent.  
