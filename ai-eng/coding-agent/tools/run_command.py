from subprocess import run, TimeoutExpired

from dapr_agents import tool


@tool
def run_command(command: str) -> str:
    """
    Execute a shell command and return the output.

    Args:
        command: The shell command to execute.

    Returns:
        The command output (stdout + stderr), or an error message.
    """
    try:
        result = run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=60
        )
        output = result.stdout
        if result.stderr:
            output += "\n" + result.stderr if output else result.stderr
        return output if output else "Command completed with no output"
    except TimeoutExpired:
        return "Error: Command timed out after 60 seconds"
    except Exception as e:
        return f"Error executing command: {str(e)}"
