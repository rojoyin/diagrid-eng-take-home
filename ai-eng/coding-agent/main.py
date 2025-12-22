#!/usr/bin/env python3
import logging

from dapr_agents import DurableAgent
from dapr_agents.llm import DaprChatClient
from dapr_agents.memory import ConversationDaprStateMemory
from dapr_agents.agents.configs import (
    AgentExecutionConfig,
    AgentMemoryConfig,
    AgentPubSubConfig,
    AgentRegistryConfig,
    AgentStateConfig,
)
from dapr_agents.storage.daprstores.stateservice import StateStoreService
from dapr_agents.workflow.runners import AgentRunner

from tools import read_file, write_file, list_directory, run_command


def main() -> None:
    logging.basicConfig(level=logging.INFO)

    agent = DurableAgent(
        name="Coding Agent",
        role="Coding Agent",
        goal="Assist with coding tasks and provide programming support.",
        instructions=[
            "Assist with coding tasks",
        ],
        llm=DaprChatClient(component_name='ollama'),
        pubsub = AgentPubSubConfig(
            pubsub_name="messagepubsub",
            agent_topic="agent.requests",
            broadcast_topic="agent.broadcast",
        ),
        state = AgentStateConfig(
            store=StateStoreService(store_name="workflowstatestore"),
        ),
        registry = AgentRegistryConfig(
            store=StateStoreService(store_name="registrystatestore"),
            team_name="default",
        ),
        execution = AgentExecutionConfig(max_iterations=3),
        memory = AgentMemoryConfig(
            store=ConversationDaprStateMemory(
                store_name="conversationstore",
                session_id="agent-session",
            )
        ),
        tools=[read_file, write_file, list_directory, run_command],
    )

    runner = AgentRunner()
    try:
        ######
        #
        # Choose how to run the agent by uncommenting one of the options below (1, 2 or 3).
        #
        ######

        # 1. .run()
        # -----------------------------
        # prompt = "Your prompt here"
        # result = await runner.run(
        #     agent,
        #     payload={"task": prompt},
        # )
        # print(f"\nFinal Result:\n{result}\n", flush=True)

        # 2. .serve()
        # -----------------------------
        runner.serve(agent, port=8001)

        # 3. .subscribe()
        # -----------------------------
        # from dapr_agents.workflow.utils.core import wait_for_shutdown
        # runner.subscribe(agent)
        # await wait_for_shutdown()

        print("Done ✅", flush=True)
    finally:
        runner.shutdown(agent)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
