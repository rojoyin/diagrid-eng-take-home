from subprocess import run

from dapr_agents import tool


@tool
def git_commit(message: str) -> str:
    """
    Stage all changes and commit with the given message.

    Args:
        message: The commit message.

    Returns:
        Success message or error.
    """
    try:
        run(["git", "add", "."], check=True)
        result = run(
            ["git", "commit", "-m", message],
            capture_output=True,
            text=True
        )
        return result.stdout if result.returncode == 0 else result.stderr
    except Exception as e:
        return f"Error: {str(e)}"