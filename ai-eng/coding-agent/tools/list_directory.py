import glob
import os

from dapr_agents import tool

@tool
def list_directory(dir_path: str) -> str:
    """
    List the content of a directory.

    Args:
        dir_path: The path to the directory to list. Can be absolute or relative.

    Returns:
        A list of the content of the dir_path, or an error message.
    """
    try:
        abs_path = os.path.abspath(dir_path)
        content = glob.glob(os.path.join(abs_path, '*'))
        return "\n".join(content) if content else "Empty directory"
    except PermissionError:
        return f"Permission denied: {dir_path}"
    except Exception as e:
        return f"Error listing directory: {dir_path}, {str(e)}"
