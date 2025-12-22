import os

from dapr_agents import tool

@tool
def read_file(file_path: str) -> str:
    """
    Read the contents of a file at the specified path.

    Args:
        file_path: The path to the file to read. Can be absolute or relative.

    Returns:
        The contents of the file as a string.
    """
    try:
        abs_path = os.path.abspath(file_path)
        with open(abs_path, 'r', encoding='utf-8') as f:
            return f.read()
    except PermissionError:
        return f"Permission denied: {file_path}"
    except Exception as e:
        return f"Error reading file: {file_path}, {str(e)}"
