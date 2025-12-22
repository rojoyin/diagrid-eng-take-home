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

The method I chose is `serve` because it allows the agent to run as a web server and handle requests from the user.
The agent will run on port 8001 and will be accessible at `http://localhost:8001`. 

The way I see the flow of use is like this:
- The client is a plugin inside the user's IDE that allows the user to send messages via a text box.
- Once the client submits the task, the post request is sent creating a task instance.
- The UI shows a loading spinner and block sending further messages until the task is solved or expires.

The command to run this in local, with an environment variable to increase the timeout for the API as in local the llama
model was taking longer than a minute to execute.

```bash
DAPR_API_TIMEOUT_SECONDS=300 dapr run --app-id coding-agent --resources-path ./components --app-port 8001 -- uv run python main.py
```

You can access the API docs at `http://localhost:8001/docs`, where the POST endpoint `/run` is available to create 
a task instance, and the suggested body is:

```json
{"task": "Your task here"}
```
Create a task instance and you will receive a task id.
![img.png](img.png)

Check the task status and output.
![img_1.png](img_1.png)

## Task 2

Implement `tools` relevant for an agent to assist a developer with coding tasks.

Suggestions for tools:
1. Filesystem operations
2. String manipulation
3. Git operations
4. OS operations

### Deliverable
Explain the details of the implementations and explain why the tool is relevant for a coding agent.

To implement this, there are two main goals:
- Reduce the amount of code required when we need to add a new tool
- Keep each tool self-contained and easy to understand, disallowing the changing the code that is already written and is functional.

So to achieve these, I created a `tools` regular package whose `__init__.py` file imports all the tools from the `tools` directory,
each tool is a function that is decorated with the `@tool` decorator from the `dapr_agents` library, and then added to the agent.

It is assumed that the entry point of each tool is the function that is decorated with the `@tool` decorator and its 
name is the same as the module's name, this way the import in the `main.py` is simple and does not require any additional
configuration. Also, if some extra functions are needed to implement the actual functionality of the tool, they are 
contained in the same module as the tool.

## Task 3

Demonstrate your understanding of the Dapr Agents framework, dependencies and the code execution of the agent.

### Deliverable
Demonstrate the agent using the implemented tool(s) to help you with a coding task.
Explain what is happening during the execution flow of the agent and how it is interacting with Dapr and it's components.
