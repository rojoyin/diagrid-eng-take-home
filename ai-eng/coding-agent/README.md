# Dapr Agents coding agent assignment

Your task is to make a coding agent using the starter provided in this repository.
The expectation is to use 2-4 hours. It should not be necessary to spend >4 hours.

## Resource
- [Dapr Agents docs](https://v1-16.docs.dapr.io/developing-applications/dapr-agents/)
- [Dapr Python SDK docs](https://docs.dapr.io/developing-applications/sdks/python)

## Pre-requisites

This starter assumes you are running the following:
- [Ollama](https://ollama.com/download) on port 11434 with [llama3.2:latest](https://ollama.com/library/llama3.2:latest).
- [Redis](https://redis.io/docs/getting-started/installation/) on port 6379 with no authentication.

You can modify the components directly in the `./components` directory if you need to change these configuration.

You will also need to install:
- [Dapr CLI](https://docs.dapr.io/getting-started/install-dapr-cli/)
- [Python](https://www.python.org/downloads/)

## Task 1

The first task is to edit the `main.py` and choose how the agent should run; `serve`, `run`, `subscribe` and then execute the program.

### Deliverable
Show a running agent and articulate _why_ you chose this method for the agent to run for this particular use case.

## Task 2

Implement `tools` relevant for an agent to assist a developer with coding tasks.

Suggestions for tools:
1. Filesystem operations
2. String manipulation
3. Git operations
4. OS operations

### Deliverable
Explain the details of the implementations and explain why the tool is relevant for a coding agent.

## Task 3

Demonstrate your understanding of the Dapr Agents framework, dependencies and the code execution of the agent.

### Deliverable
Demonstrate the agent using the implemented tool(s) to help you with a coding task.
Explain what is happening during the execution flow of the agent and how it is interacting with Dapr and it's components.
